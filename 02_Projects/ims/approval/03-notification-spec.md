# 审批通知规范

## 通知类型
- SYSTEM：系统提示
- APPROVAL：审批通知（待办）
- RESULT：审批结果（通过/拒绝）

## 通知内容建议
- title：项目审批/审批通过/审批拒绝
- content：包含项目名、申请人、时间、意见（如有）
- link_url：跳转到审批页面或项目详情

## 去重策略（重要）
- dedup_key：建议为 `approval:project:<id>:pending`

## 谁收谁发
- 待审批：发给审批人（管理员/指定角色）
- 审批结果：发给申请人
