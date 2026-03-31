# uv Python 环境管理使用说明（工程实践版）

## 1. uv 是什么

`uv` 是 Astral 提供的 Python 包与项目管理工具，主打**快**和**统一工作流**：
- 可以管理 Python 版本；
- 可以创建和管理虚拟环境；
- 可以替代常见 `pip` / `pip-tools` / `virtualenv` 场景；
- 在项目模式下自动维护锁文件（`uv.lock`）与环境同步。

> 适用人群：日常做 Python 开发、需要多项目隔离环境、希望提升依赖可复现性的人。

---

## 2. 安装 uv

> 推荐以官方文档为准，以下给出常见方式。

### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows PowerShell
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装后验证：
```bash
uv --version
```

---

## 3. 两种常见使用模式

uv 有两条主线，建议按场景选择：

### 模式 A：项目模式（推荐）
用于有 `pyproject.toml` 的工程开发。核心命令：
- `uv init` 初始化项目；
- `uv add` 添加依赖；
- `uv lock` 生成/更新锁文件；
- `uv sync` 同步环境；
- `uv run` 在受控环境中执行命令。

特点：
- 默认管理 `.venv`；
- 自动确保“声明依赖 → 锁文件 → 虚拟环境”一致；
- 团队协作可复现性更好。

### 模式 B：pip 兼容模式
用于迁移旧项目或临时脚本。核心命令：
- `uv venv` 创建虚拟环境；
- `uv pip install` 安装包；
- `uv pip compile` 生成 requirements 锁定文件；
- `uv pip sync` 按锁文件精确同步环境。

特点：
- 上手接近 pip 生态；
- 更容易逐步替换旧流程。

---

## 4. 快速开始（项目模式）

### 4.1 新建项目
```bash
mkdir demo-uv && cd demo-uv
uv init
```

### 4.2 指定 Python 版本并创建环境
```bash
uv venv --python 3.12
```

> 在项目模式下，uv 通常会将环境放在项目根目录 `.venv`。

### 4.3 添加依赖
```bash
uv add requests
uv add --dev pytest ruff
```

### 4.4 运行命令
```bash
uv run python -c "import requests; print(requests.__version__)"
uv run pytest
uv run ruff check .
```

### 4.5 锁定与同步
```bash
uv lock
uv sync
```

团队协作时建议：
- 提交 `pyproject.toml` 与 `uv.lock`；
- 不提交 `.venv`。

---

## 5. 典型日常命令清单

### 依赖管理
```bash
uv add fastapi
uv remove fastapi
uv add "pydantic>=2,<3"
```

### 升级策略
```bash
uv lock --upgrade
uv lock --upgrade-package requests
```

### 环境同步
```bash
uv sync
uv sync --frozen   # 使用现有锁文件，不更新
uv sync --locked   # 要求锁文件与配置匹配
```

### 执行工具（无需全局安装）
```bash
uvx ruff --version
uvx black --version
```

---

## 6. 迁移已有 pip 项目

假设你有 `requirements.in` / `requirements.txt`：

### 6.1 创建虚拟环境
```bash
uv venv
source .venv/bin/activate   # Windows 使用 .venv\Scripts\activate
```

### 6.2 生成锁定文件（类似 pip-compile）
```bash
uv pip compile requirements.in -o requirements.txt
```

### 6.3 精确同步环境（类似 pip-sync）
```bash
uv pip sync requirements.txt
```

### 6.4 或直接安装
```bash
uv pip install -r requirements.txt
```

> 差异提示：`install` 不会自动删除多余包；`sync` 会让环境更贴近“声明即现实”。

---

## 7. 常见问题与排查

### Q1：为什么执行 `uv pip install` 提示找不到虚拟环境？
uv 默认要求在虚拟环境内操作依赖。先执行：
```bash
uv venv
```
然后激活环境再安装，或在项目模式使用 `uv add/uv sync/uv run`。

### Q2：什么时候用 `uv run`，什么时候 `python` 直接跑？
- 在项目中推荐始终 `uv run ...`，可保证依赖已同步；
- 临时调试在已激活 `.venv` 里可直接 `python ...`。

### Q3：`uv.lock` 要不要提交？
建议提交。它记录精确解析结果，能提升跨机器一致性。

### Q4：和 Conda 能共存吗？
可以。uv 能识别已激活环境；但工程上建议“一个项目一套明确流程”，避免混用造成定位困难。

---

## 8. 推荐团队规范（可直接落地）

1. 新项目统一 `uv init`；
2. 依赖变更只用 `uv add/remove`，避免手改导致漂移；
3. CI 中执行：
   ```bash
   uv lock --check
   uv sync --frozen
   uv run pytest
   ```
4. 统一提交：`pyproject.toml` + `uv.lock`；
5. `.venv`、缓存目录加入 `.gitignore`。

---

## 9. 最小实践模板

```bash
# 1) 初始化
uv init myapp && cd myapp

# 2) 创建环境（可选指定版本）
uv venv --python 3.12

# 3) 添加依赖
uv add fastapi uvicorn
uv add --dev pytest ruff

# 4) 开发运行
uv run uvicorn myapp:app --reload

# 5) 测试与检查
uv run pytest
uv run ruff check .
```

---

## 10. 在我项目中的用法 / 经验

- **原则**：业务项目优先使用“项目模式”，遗留项目采用“pip 兼容模式”渐进迁移。
- **收益**：减少“我本地能跑、你那边不行”的依赖漂移问题。
- **建议**：把 `uv sync --frozen && uv run pytest` 固化进 CI，稳定性提升明显。
