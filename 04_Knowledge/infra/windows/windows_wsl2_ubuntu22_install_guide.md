# Windows 安装 WSL2 + Ubuntu 22.04 实战指南

> 适用于：Windows 10 / Windows 11
>
> 目标：在 Windows 上稳定安装 **WSL2 + Ubuntu 22.04 LTS**，用于开发、工程、模型训练与 Docker 场景

---

## 一、快速结论（最简单方案）

在 **管理员 PowerShell** 中执行：

```powershell
wsl --install -d Ubuntu-22.04
```

该命令会自动完成：

* 启用 WSL
* 启用虚拟机平台
* 安装 WSL2
* 安装 Ubuntu 22.04 LTS

⚠️ 执行完成后 **必须重启 Windows**，重启后 Ubuntu 会自动启动并进入初始化流程。

---

## 二、安装前的必要条件检查（必须确认）

### 1. Windows 版本要求

* Windows 10：21H2 及以上
* Windows 11：任意版本

查看方式：

```powershell
winver
```

---

### 2. CPU 虚拟化支持

* Intel：VT-x
* AMD：SVM

检查方式（PowerShell）：

```powershell
systeminfo | findstr /i "虚拟化"
```

期望输出包含：

```
已启用虚拟化: 是
```

---

### 3. BIOS 中开启虚拟化

常见路径：

* Advanced / Advanced BIOS
* CPU Configuration
* Intel Virtualization / SVM Mode → Enabled

如未开启，WSL2 将无法运行。

---

## 三、稳妥的分步安装方式（推荐归档保存）

当一键安装失败或需要更可控的过程时，使用以下步骤。

### Step 1：启用系统功能

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

👉 执行完成后 **重启 Windows**。

---

### Step 2：设置默认 WSL 版本为 2

```powershell
wsl --set-default-version 2
```

---

### Step 3：安装 Ubuntu 22.04

```powershell
wsl --install -d Ubuntu-22.04
```

或通过 Microsoft Store 搜索 **Ubuntu 22.04 LTS** 安装。

---

## 四、Ubuntu 首次启动初始化

首次启动 Ubuntu 会提示创建 Linux 用户：

```text
Enter new UNIX username:
Enter new UNIX password:
```

说明：

* 该用户是 Linux 内部用户
* 与 Windows 用户无关

---

## 五、确认 WSL2 是否生效（关键验证）

在 PowerShell 中执行：

```powershell
wsl -l -v
```

期望输出示例：

```text
NAME            STATE           VERSION
Ubuntu-22.04    Running         2
```

若 VERSION 为 1，可手动切换：

```powershell
wsl --set-version Ubuntu-22.04 2
```

---

## 六、WSL2 必做优化配置（强烈建议）

### 1. 更新 Ubuntu 系统

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 2. 安装基础开发工具

```bash
sudo apt install -y \
  build-essential \
  git \
  curl \
  wget \
  vim \
  htop \
  unzip
```

---

### 3. 文件系统使用建议（性能关键）

推荐：

* 项目放在 Linux 文件系统中

  ```bash
  ~/projects
  ```

不推荐：

* 在 `/mnt/c` 下进行大量 IO 操作

原因：

* `/mnt/c` 属于跨系统文件访问
* IO 性能可能下降 3～10 倍

---

### 4. 配置 WSL2 资源限制（防止吃满 Windows 资源）

在 Windows 用户目录创建文件：

```text
C:\Users\<你的用户名>\.wslconfig
```

示例配置：

```ini
[wsl2]
memory=16GB
processors=8
swap=8GB
localhostForwarding=true
```

应用配置：

```powershell
wsl --shutdown
```

重新打开 Ubuntu 即可生效。

---

### 5. Docker + WSL2（可选但强烈推荐）

* 安装 Docker Desktop
* 设置中启用：

  * Use WSL 2 based engine
  * Ubuntu-22.04 集成

适用于：

* Docker
* docker-compose
* GPU / CPU 混合开发环境

---

## 七、典型使用场景（工程向）

WSL2 + Ubuntu 22.04 特别适合以下场景：

* Python / PyTorch / CPU 或 GPU 训练
* 数据生成与离线计算
* Django / FastAPI 后端服务
* Docker / Docker Compose
* 工程级 Linux 环境模拟

---

## 八、常见问题与避坑总结

* 未开启 BIOS 虚拟化
* Windows 版本过低
* 在 `/mnt/c` 下跑高 IO 任务
* 未限制 WSL 内存导致系统卡顿
* 使用过时的 WSL1 教程

---

## 九、归档说明

本文档适合作为：

* 个人知识库归档
* 工程环境初始化文档
* 团队 WSL2 安装规范

建议文件名：

```text
windows_wsl2_ubuntu22_install_guide.md
```

---

**文档版本**：v1.0
**最后更新**：2026-01
