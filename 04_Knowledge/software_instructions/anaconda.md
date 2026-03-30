# Conda 使用手册

> 适用对象：日常 Python 开发、数据科学、机器学习、离线部署维护人员。  
> 关键词：环境隔离、包管理、可复现、镜像源、排障。

---

## 1. Conda 是什么

Conda 是一个**跨平台的包管理 + 环境管理工具**，常见于以下发行版：

- **Anaconda**：预装大量科学计算包，安装体积大，开箱即用。
- **Miniconda**：仅包含 Conda 最小核心，按需安装，轻量。
- **Miniforge / Mambaforge**：社区路线，通常默认使用 conda-forge 生态。

Conda 的核心价值：

1. **环境隔离**：不同项目可以使用不同 Python 版本与依赖组合。
2. **可复现**：通过 `environment.yml` / 显式导出文件重建环境。
3. **跨语言依赖支持**：不仅是 Python 包，也能管理 C/C++ 库等二进制依赖。

---

## 2. 安装与初始化

### 2.1 查看 Conda 是否可用

```bash
conda --version
```

### 2.2 初始化 Shell（首次安装后常见）

```bash
conda init
# 然后重启终端，或执行：
source ~/.bashrc
```

> 若你使用 zsh，请改为 `source ~/.zshrc`。

### 2.3 更新 Conda

```bash
conda update -n base -c defaults conda
```

---

## 3. 环境管理（最常用）

### 3.1 查看已有环境

```bash
conda env list
# 或
conda info --envs
```

### 3.2 创建环境

```bash
# 创建 Python 3.11 环境
conda create -n py311 python=3.11
```

### 3.3 激活 / 退出环境

```bash
conda activate py311
conda deactivate
```

### 3.4 删除环境

```bash
conda remove -n py311 --all
```

### 3.5 克隆环境

```bash
conda create -n py311-copy --clone py311
```

---

## 4. 包管理

### 4.1 安装包

```bash
# 在当前激活环境安装
conda install numpy pandas

# 指定环境安装
conda install -n py311 scipy matplotlib
```

### 4.2 指定版本安装

```bash
conda install python=3.10
conda install "numpy>=1.26,<2.0"
```

### 4.3 升级包

```bash
conda update numpy
conda update --all
```

### 4.4 卸载包

```bash
conda remove numpy
```

### 4.5 搜索包

```bash
conda search scikit-learn
```

---

## 5. channel（软件源）与镜像配置

Conda 会从 channel 下载包，常见 channel：

- `defaults`（官方默认）
- `conda-forge`（社区生态，包更新通常更快）

### 5.1 查看当前 channel

```bash
conda config --show channels
```

### 5.2 添加 conda-forge

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### 5.3 使用国内镜像（示例）

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

> 若网络策略变化，请以镜像站官方文档为准。

---

## 6. pip 与 conda 混用建议

可混用，但建议遵循顺序：

1. 优先用 `conda install` 安装能在 conda 中找到的包。
2. 缺失包再用 `pip install`。
3. 尽量在同一环境里减少反复交叉升级（避免依赖冲突）。

推荐做法：

```bash
conda create -n proj python=3.11
conda activate proj
conda install numpy pandas
pip install some-package-not-in-conda
```

---

## 7. 导出与复现环境（团队协作重点）

### 7.1 导出 environment.yml（推荐）

```bash
conda env export -n py311 > environment.yml
```

使用导出文件创建环境：

```bash
conda env create -f environment.yml
```

### 7.2 仅导出显式包（更严格复现）

```bash
conda list --explicit > spec-file.txt
conda create -n py311-rebuild --file spec-file.txt
```

### 7.3 更新已存在环境

```bash
conda env update -n py311 -f environment.yml --prune
```

---

## 8. 常见工作流示例

### 8.1 新项目快速开始

```bash
conda create -n demo python=3.11 -y
conda activate demo
conda install -y numpy pandas jupyterlab
python -V
conda list
```

### 8.2 数据科学常用环境（示例）

```bash
conda create -n ds python=3.11 -y
conda activate ds
conda install -y numpy pandas scipy scikit-learn matplotlib seaborn jupyterlab
```

---

## 9. 故障排查

### 9.1 激活命令不可用

现象：`conda activate` 报错。  
处理：

```bash
conda init
source ~/.bashrc
```

### 9.2 解依赖很慢

可尝试：

- 配置更快的 channel / 镜像。
- 开启严格优先级：

```bash
conda config --set channel_priority strict
```

- 使用 `mamba`（兼容 conda 命令，解依赖更快）：

```bash
conda install -n base -c conda-forge mamba
mamba install numpy pandas
```

### 9.3 环境损坏或冲突严重

建议直接重建：

```bash
conda deactivate
conda remove -n bad-env --all
conda create -n bad-env python=3.11
```

### 9.4 证书/网络问题

优先检查代理、防火墙、公司网络策略，再检查 `.condarc` 配置是否错误。

---

## 10. `.condarc` 示例

```yaml
channels:
  - conda-forge
  - defaults
channel_priority: strict
show_channel_urls: true
auto_activate_base: false
```

说明：

- `auto_activate_base: false` 可避免每次打开终端自动进入 base 环境。

---

## 11. 最佳实践（建议收藏）

1. **一个项目一个环境**，不要所有项目共用 base。
2. 固定关键版本（Python、核心框架）。
3. 通过 `environment.yml` 进行版本管理并提交到仓库。
4. 混用 pip 时，先 conda 后 pip。
5. 环境过旧或冲突太多时，优先重建而非硬修。

---

## 12. 常用命令速查

```bash
# 查看 conda 版本
conda --version

# 查看环境
conda env list

# 创建环境
conda create -n myenv python=3.11

# 激活/退出
conda activate myenv
conda deactivate

# 安装/卸载包
conda install numpy
conda remove numpy

# 导出/复现环境
conda env export -n myenv > environment.yml
conda env create -f environment.yml

# 删除环境
conda remove -n myenv --all
```

---

如果你希望，我可以继续给你补一版：

- **Windows 专用 Conda 手册**（含 PowerShell、CMD、VSCode 解释器联动）
- **企业离线环境 Conda 手册**（离线包、私有 channel、内网部署）
- **Conda + CUDA + PyTorch/TensorFlow 手册**（GPU 开发场景）
