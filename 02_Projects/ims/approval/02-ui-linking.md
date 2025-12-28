# 审批入口与页面链接规范（UI Linking）

## 入口原则
- 通知点击必须能“落到可操作的审批界面”
- 个人主页/项目列表/弹框：保持同一个路由体系

## 推荐做法
- 给审批页面一个稳定 URL（例：/projects/user/ 或 /projects/approvals/）
- 通知 link_url 指向稳定页面 + query 参数定位项目
  - 例：/projects/approvals/?project_id=123

## 弹框与页面的连接
- 如果审批是在“个人主页项目弹框”里完成：
  - 需要一个可路由的页面容器（不是纯静态 html 文件名）
  - 通过 query 参数自动打开对应项目的弹框
