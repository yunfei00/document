# 日志结构建议

默认（人类可读）至少包含：
- time / level / module / message

示例：
`2026-01-05 18:01:02 | INFO | nfs_scanner.app | starting`

何时考虑 JSON：
- 需要集中式采集与字段检索（ELK 等）
