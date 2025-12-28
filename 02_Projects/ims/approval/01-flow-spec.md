# 审批流程规范（状态机）

## 状态定义（示例）
- DRAFT（草稿/未提交）可选
- PENDING（待审批）
- APPROVED（已通过）
- REJECTED（已拒绝）
- CANCELED（已撤回）可选

## 触发与动作
- 创建项目 → PENDING
- 审批通过 → APPROVED（记录审批意见、审批人、时间）
- 审批拒绝 → REJECTED（同上）

## 数据字段建议
- applicant（申请人）
- approver（审批人）
- approve_comment（审批意见）
- approve_time
- status
- status_history（可选）

## 幂等与重复提交
- 防止重复审批
- 防止重复通知（dedup_key）
