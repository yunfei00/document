# npm 使用手册（Node.js 包管理）

## 1. npm 是什么

npm（Node Package Manager）是 Node.js 官方默认的包管理工具，用于：

- 安装和管理第三方依赖包
- 管理项目脚本（`npm run`）
- 发布和维护自己的包
- 管理多环境依赖（开发、生产、可选依赖）

npm 随 Node.js 一起安装，安装 Node.js 后一般即可直接使用。

---

## 2. 安装与版本检查

### 2.1 安装 Node.js（含 npm）

- 官网下载并安装 LTS 版本：<https://nodejs.org/>
- 建议团队统一 Node.js 大版本，避免“我这能跑你那不能跑”。

### 2.2 检查版本

```bash
node -v
npm -v
```

### 2.3 升级 npm

```bash
npm install -g npm@latest
```

> 说明：升级 npm 前，建议先确认当前 Node.js 版本是否支持最新 npm。

---

## 3. 基础概念

### 3.1 `package.json`

项目清单文件，记录：

- 项目元信息（名称、版本、描述）
- 依赖（dependencies / devDependencies）
- 脚本（scripts）
- 入口、仓库、许可证等

初始化项目：

```bash
npm init
# 快速默认初始化
npm init -y
```

### 3.2 `package-lock.json`

锁定依赖树的精确版本，保证多人协作和 CI 环境可复现安装结果。

> 建议：**提交到 Git**，不要随意删除。

### 3.3 `node_modules`

依赖包安装目录，通常较大，不建议提交到仓库（应加入 `.gitignore`）。

---

## 4. 常用命令速查

### 4.1 安装依赖

```bash
# 安装到 dependencies
npm install axios

# 安装到 devDependencies
npm install -D typescript

# 全局安装（慎用，优先项目本地安装）
npm install -g pnpm
```

### 4.2 卸载依赖

```bash
npm uninstall axios
npm uninstall -D typescript
```

### 4.3 更新依赖

```bash
npm update
npm update axios
```

### 4.4 查看依赖

```bash
npm list
npm list --depth=0
npm outdated
```

### 4.5 运行脚本

`package.json`：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "vitest"
  }
}
```

运行方式：

```bash
npm run dev
npm run build
npm test
```

> `npm test`、`npm start` 可省略 `run`，其他脚本建议统一用 `npm run xxx`。

---

## 5. 依赖类型说明

### 5.1 `dependencies`

生产环境运行时必需依赖（如 `express`、`react`）。

### 5.2 `devDependencies`

仅开发/构建/测试阶段使用（如 `eslint`、`vite`、`jest`、`typescript`）。

### 5.3 `peerDependencies`

用于声明“宿主项目需要提供的依赖版本范围”，常见于插件或组件库。

### 5.4 `optionalDependencies`

可选依赖，安装失败通常不会阻塞主流程。

---

## 6. 团队协作最佳实践

### 6.1 使用 `npm ci` 做稳定安装

```bash
npm ci
```

特点：

- 严格按照 `package-lock.json` 安装
- 速度通常快于 `npm install`
- 若锁文件与 `package.json` 不一致会直接失败（利于 CI 提前发现问题）

### 6.2 Node 版本对齐

可在项目根目录增加 `.nvmrc`：

```txt
20
```

团队配合 `nvm use` 统一 Node 版本。

### 6.3 锁文件管理

- 锁文件冲突时，不建议手工逐行拼接
- 推荐：切回分支分别执行安装后重新生成，再做功能验证

---

## 7. 镜像源与网络配置

### 7.1 查看当前源

```bash
npm config get registry
```

### 7.2 设置官方源

```bash
npm config set registry https://registry.npmjs.org/
```

### 7.3 临时使用镜像安装

```bash
npm install --registry=https://registry.npmmirror.com
```

> 建议优先使用官方源；遇到网络慢或超时，再选择可信镜像。

---

## 8. 安全与审计

### 8.1 漏洞扫描

```bash
npm audit
```

### 8.2 自动修复

```bash
npm audit fix
```

> `npm audit fix --force` 可能引入破坏性升级，务必结合测试再使用。

### 8.3 安全建议

- 只安装可信包，留意下载量和维护活跃度
- 锁定关键依赖版本
- 在 CI 中加入 `npm audit` 或 SCA 扫描

---

## 9. 发布你的 npm 包（基础流程）

### 9.1 登录账号

```bash
npm login
```

### 9.2 检查包名与内容

```bash
npm whoami
npm pack --dry-run
```

### 9.3 发布

```bash
npm publish
```

若是组织作用域包（如 `@org/pkg`）首次发布常用：

```bash
npm publish --access public
```

### 9.4 版本管理

```bash
# patch/minor/major
npm version patch
npm version minor
npm version major
```

---

## 10. 常见问题排查

### 10.1 `node-gyp` 编译失败

原因通常是本地编译链缺失（Python、C/C++ 构建工具）。

处理建议：

- 安装平台对应构建工具
- 优先选择有预编译二进制的包版本
- 对齐 Node 版本（某些原生模块对 Node 版本敏感）

### 10.2 安装慢 / 超时

- 检查网络与 DNS
- 切换可用镜像源
- 清缓存后重试：

```bash
npm cache verify
npm cache clean --force
```

### 10.3 依赖冲突（peer dependency）

- 优先升级到兼容版本
- 避免长期依赖 `--legacy-peer-deps`
- 在 PR 中记录冲突原因与处理方案

### 10.4 “在我机器上可运行”

排查顺序：

1. Node 版本是否一致
2. 是否使用了 `npm ci`
3. 锁文件是否最新且已提交
4. 是否存在全局包干扰（`npm -g list --depth=0`）

---

## 11. 推荐工作流（前端/Node 项目）

1. 初始化项目：`npm init -y`
2. 安装依赖：`npm i xxx` / `npm i -D xxx`
3. 配置脚本：`dev/build/test/lint`
4. 开发阶段：`npm run dev`
5. 提交前：`npm run test && npm run build`
6. CI 中使用：`npm ci`
7. 定期执行：`npm outdated` + `npm audit`

---

## 12. 附录：高频命令一览

```bash
# 初始化
npm init -y

# 安装 / 卸载
npm i <pkg>
npm i -D <pkg>
npm un <pkg>

# 脚本
npm run <script>
npm test

# 依赖检查
npm list --depth=0
npm outdated

# 稳定安装
npm ci

# 安全审计
npm audit
npm audit fix

# 配置
npm config get registry
npm config set registry https://registry.npmjs.org/
```
