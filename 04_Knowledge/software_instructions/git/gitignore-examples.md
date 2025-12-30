
# .gitignore 详细说明与示例（工程版）

> 目的：告诉 Git **哪些文件不要进入仓库**（临时文件、日志、产物、数据目录、密钥等）。  
> 关键点：`.gitignore` 只对 **未被跟踪的文件** 生效；已经提交过的文件不会被它“自动移除”。

---

## 1. 基本语法规则

### 1.1 忽略文件后缀
```gitignore
*.log
*.tmp
*.zip
```

### 1.2 忽略目录
```gitignore
__pycache__/
media/
data/
```

### 1.3 只忽略某个目录下的匹配
```gitignore
build/*.zip
logs/*.log
```

### 1.4 任意层级匹配（** 常用于 node_modules）
```gitignore
**/node_modules/
```

### 1.5 反向规则（例外：!）
```gitignore
.env            # 忽略所有 .env
!.env.example   # 但保留示例文件进入仓库
```

### 1.6 以 / 开头（从仓库根目录匹配）
```gitignore
/staticfiles/
```

---

## 2. 常见工程模板（可直接复制）

### 2.1 Python / Django（含交付产物）
```gitignore
# Python
__pycache__/
*.py[cod]
*.so
*.egg-info/
dist/
build/
.pytest_cache/
.mypy_cache/

# Virtual env
.venv/
venv/
.env
.env.*

# Django
db.sqlite3
media/
staticfiles/
*.log

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Delivery artifacts
downloads/
reports/
*.tar
*.tar.gz
*.zip

# Secrets / keys
*.pem
*.key
*.p12
id_rsa
id_ed25519
cosign.key
```

### 2.2 前端（Node）
```gitignore
node_modules/
dist/
.vite/
*.log
```

### 2.3 通用（日志、缓存、临时文件）
```gitignore
*.log
*.tmp
*.swp
*.bak
.cache/
tmp/
```

---

## 3. 常见坑：加了 .gitignore 但文件还是被提交了

原因：这些文件 **之前已经被 Git 跟踪**。

### 3.1 停止跟踪（保留本地文件）
```bash
git rm -r --cached <path>
git add .gitignore
git commit -m "chore: stop tracking ignored files"
```

例子：你曾经误提交 `media/`，现在要让它不再被跟踪：
```bash
git rm -r --cached media/
git commit -m "chore: stop tracking media directory"
```

---

## 4. 建议你“强制不入库”的清单（特别适合商业交付）

### 4.1 密钥/凭据（坚决不入库）
- 私钥：`*.key` `id_rsa` `id_ed25519` `cosign.key`
- 证书私钥包：`*.p12` `*.pfx`
- `.env` 里的 token/password

建议：入库 `.env.example`，不入库 `.env`：
```gitignore
.env
!.env.example
```

### 4.2 运行数据与客户数据
- `/data/` `/media/` `/reports/` `/downloads/`
- 客户配置、客户日志、导出报告（除非是示例数据）

---

## 5. 推荐实践：一条命令先查“有哪些未跟踪文件”
```bash
git status
```

如果你发现有大量临时产物，优先：
1) 加 `.gitignore`
2) 再考虑 `git clean -fdn`（预览）→ `git clean -fd`（清理）
