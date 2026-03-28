# Next.js 手册（工程实践版）

> 适用版本：Next.js 14/15（以 App Router 为主）
> 
> 目标读者：希望从 0 到可上线，建立一套可维护 Next.js 项目实践的开发者。

---

## 1. Next.js 是什么

Next.js 是基于 React 的全栈框架，核心价值在于：

- **同时支持前端渲染与服务端能力**（SSR、SSG、ISR、RSC、API）
- **约定式路由**，降低项目组织复杂度
- **内置工程化能力**，比如代码分割、图片优化、字体优化、打包优化
- **面向生产**：缓存、流式渲染、边缘运行时、性能指标等

一句话：Next.js 不只是“React 路由框架”，而是“可直接交付 Web 产品”的全栈基础设施。

---

## 2. 快速开始

### 2.1 创建项目

```bash
npx create-next-app@latest my-next-app
```

创建时建议选择：

- TypeScript：✅
- ESLint：✅
- App Router：✅
- src/ 目录：按团队习惯
- Tailwind CSS：按项目需要

### 2.2 启动开发

```bash
cd my-next-app
npm run dev
```

访问 `http://localhost:3000`。

### 2.3 常用脚本

```bash
npm run dev     # 开发模式
npm run build   # 生产构建
npm run start   # 启动生产服务
npm run lint    # 代码检查
```

---

## 3. 项目结构（App Router）

一个常见、可维护的结构：

```txt
src/
  app/
    layout.tsx
    page.tsx
    (marketing)/
      about/page.tsx
    (dashboard)/
      dashboard/page.tsx
    api/
      users/route.ts
  components/
  lib/
  services/
  hooks/
  styles/
  types/
```

说明：

- `app/`：路由与页面入口（App Router）
- `layout.tsx`：共享布局
- `page.tsx`：具体页面
- `route.ts`：Route Handlers（服务端 API）
- `lib/`：工具函数（格式化、校验、封装）
- `services/`：业务接口调用层

---

## 4. 路由系统核心

### 4.1 文件即路由

- `app/page.tsx` → `/`
- `app/blog/page.tsx` → `/blog`
- `app/blog/[slug]/page.tsx` → `/blog/:slug`

### 4.2 动态路由

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogDetail({ params }: { params: { slug: string } }) {
  return <div>文章：{params.slug}</div>
}
```

### 4.3 路由分组与私有段

- `(group)`：用于组织目录，不出现在 URL
- `_folder`：私有目录，不作为路由

### 4.4 并行路由和拦截路由

适合复杂后台（弹窗详情、主页面 + 侧边详情）。

- 并行路由：`@slot`
- 拦截路由：`(.)`、`(..)`

建议：只在“体验价值明显”场景使用，避免团队理解成本过高。

---

## 5. 渲染与数据获取

Next.js 的关键是“按页面特征选择渲染策略”。

### 5.1 常见渲染方式

- **SSR**：每次请求服务端渲染，适合实时数据
- **SSG**：构建时静态生成，适合文档/营销页
- **ISR**：静态页定时增量更新，适合资讯类页面
- **CSR**：浏览器端获取数据，适合强交互区域

### 5.2 App Router 中的数据获取

在 Server Component 里可直接 `await fetch()`：

```tsx
export default async function Page() {
  const res = await fetch('https://api.example.com/posts', {
    next: { revalidate: 60 },
  })
  const posts = await res.json()

  return <pre>{JSON.stringify(posts, null, 2)}</pre>
}
```

### 5.3 缓存策略（非常重要）

常用选项：

- `cache: 'force-cache'`：默认缓存（偏静态）
- `cache: 'no-store'`：每次都拉最新（偏动态）
- `next: { revalidate: 60 }`：ISR，每 60 秒可更新

工程建议：

1. 先明确页面业务属性（实时/准实时/低频更新）
2. 再选缓存策略
3. 对高频接口增加服务端聚合层，避免前端直接打爆后端

---

## 6. Server Components 与 Client Components

### 6.1 默认是 Server Component

优势：

- 减少客户端 JS 体积
- 更利于首屏性能
- 可安全访问服务端资源

### 6.2 何时使用 Client Component

文件顶部添加：

```tsx
'use client'
```

适用于：

- 需要 `useState/useEffect`
- 需要浏览器 API（`window`、`localStorage`）
- 强交互组件（拖拽、富文本编辑、复杂图表）

原则：

- 页面框架尽量 Server
- 交互局部下沉 Client
- 不要把整个页面都变成 Client

---

## 7. 表单与 Server Actions（现代推荐）

Server Actions 允许在服务端直接处理表单提交，减少传统 API 样板代码。

```tsx
// app/actions.ts
'use server'

export async function createTodo(formData: FormData) {
  const title = String(formData.get('title') || '')
  // 1) 校验
  // 2) 写数据库
  // 3) revalidatePath('/todos')
}
```

```tsx
// app/todos/page.tsx
import { createTodo } from '../actions'

export default function TodoPage() {
  return (
    <form action={createTodo}>
      <input name="title" placeholder="输入待办" />
      <button type="submit">提交</button>
    </form>
  )
}
```

建议搭配：

- `zod` 做输入校验
- 统一错误返回结构
- `revalidatePath/revalidateTag` 做增量刷新

---

## 8. Route Handlers（API）

位置：`app/api/**/route.ts`

```tsx
// app/api/health/route.ts
export async function GET() {
  return Response.json({ ok: true, timestamp: Date.now() })
}
```

适用场景：

- Webhook 接收
- 提供给第三方的后端接口
- 不适合写到 Action 的通用 API

---

## 9. 中间件（Middleware）

`middleware.ts` 可用于：

- 登录态初筛
- A/B Test 分流
- 国际化路由重写

注意：

- 运行在 Edge 环境，避免重型依赖
- 只做轻逻辑，复杂逻辑下沉到后端/API

---

## 10. 性能优化清单

### 10.1 图片与字体

- 使用 `next/image`
- 使用 `next/font`（避免字体闪烁）

### 10.2 JS 体积控制

- 优先 Server Components
- 大组件动态加载 `dynamic()`
- 删除无用依赖

### 10.3 渲染性能

- 合理使用 `Suspense` + 流式渲染
- 避免在顶层布局阻塞慢请求
- 对高耗时组件做分段加载

### 10.4 缓存与重验证

- 页面缓存 + 数据缓存组合设计
- 写操作后显式 `revalidatePath` 或 `revalidateTag`

---

## 11. 鉴权与安全

推荐方案：

- 鉴权：Auth.js / Clerk / 自建 JWT Session
- 权限：RBAC（角色）+ 资源级校验
- 安全：
  - 所有输入都校验（zod/class-validator）
  - 关键操作加 CSRF/重放防护
  - 敏感配置放 `.env`，禁止暴露到客户端

不要做：

- 只在前端判断权限
- 在 Client 组件内持有敏感服务端密钥

---

## 12. 工程规范建议

### 12.1 分层

- `components/`：UI 组件
- `services/`：请求编排
- `repositories/`（可选）：数据访问
- `domain/`（可选）：核心业务规则

### 12.2 代码约定

- API 响应结构统一
- 错误码统一
- 日志字段统一（traceId、userId、latency）

### 12.3 质量保障

- ESLint + Prettier
- 单测（Vitest/Jest）
- E2E（Playwright/Cypress）
- CI 必过后再合并

---

## 13. 部署与运行

常见部署：

- Vercel：开箱即用，最省心
- Docker + Node Runtime：自托管可控
- Edge Runtime：低延迟，但注意依赖兼容

上线前检查：

1. `npm run build` 无报错
2. 关键路由压测通过
3. 错误监控（Sentry）与日志可观测
4. 环境变量最小化暴露
5. 回滚方案可执行

---

## 14. 常见坑位速查

1. **把整个页面都写成 `'use client'`** → 首屏 JS 爆炸
2. **缓存策略没定义** → 数据“忽新忽旧”
3. **在 Middleware 做重逻辑** → 延迟升高
4. **Server/Client 边界不清** → Hydration 报错
5. **表单无校验直接入库** → 安全风险

---

## 15. 一个可落地的学习路径（2~4 周）

### 第 1 周：框架基础

- 路由、布局、动态路由
- Server/Client 组件边界
- Route Handlers 与基本 API

### 第 2 周：数据与缓存

- SSR/SSG/ISR 区别
- `fetch` 缓存策略
- `revalidatePath/revalidateTag`

### 第 3 周：业务能力

- 鉴权接入
- 表单 + Server Actions
- 错误处理、日志与监控

### 第 4 周：工程化

- 测试体系
- CI/CD
- 性能与安全专项优化

---

## 16. 建议的技术栈组合（参考）

- 框架：Next.js + TypeScript
- UI：Tailwind CSS + shadcn/ui
- 状态：React Query（客户端数据）+ Server Components（服务端数据）
- 校验：zod
- 数据库：PostgreSQL + Prisma
- 鉴权：Auth.js
- 监控：Sentry

---

## 17. 在我项目中的用法 / 经验（模板）

可按下面格式补充你自己的沉淀：

- 项目类型：
- 主要渲染策略：
- 缓存策略：
- 鉴权方案：
- 踩坑记录：
- 下一步优化：

---

如果你愿意，我可以继续给你补一版：

1. **“Next.js 企业级目录规范模板”**（可直接复制到项目）
2. **“Next.js 性能排查 checklist”**（线上问题快速定位）
3. **“Next.js + Auth.js + Prisma 最小可用脚手架说明”**。
