
# Pull Request

## 1. 概要（Summary）
- 这次改动做了什么？一句话说明即可。

## 2. 变更类型（Type）
- [ ] feat（新功能）
- [ ] fix（修复问题）
- [ ] refactor（重构，不改变功能）
- [ ] perf（性能优化）
- [ ] docs（文档）
- [ ] test（测试）
- [ ] build/ci（构建或CI）
- [ ] chore（杂项）

## 3. 影响范围（Scope / Modules）
- [ ] projects
- [ ] images
- [ ] repo
- [ ] components
- [ ] detection
- [ ] report
- [ ] notification
- [ ] rbac
- [ ] deployment
- [ ] docs
- [ ] other: __________

## 4. 背景与原因（Context）
- 为什么要做这个改动？（问题/需求/客户反馈/技术债）

## 5. 方案说明（Solution / Approach）
- 关键设计点（1-3条即可）
- 是否引入新依赖？是否影响部署？

## 6. 测试与验证（How to Test）
- [ ] 本地验证通过
- [ ] Docker/离线环境验证通过（如适用）
- 验证步骤（可复制）：
  1.
  2.
  3.

- 关键接口/页面：
  - URL / API：
  - 预期结果：

## 7. 截图 / 日志（Evidence）
- 截图：
- 关键日志：

## 8. 风险评估（Risk）
- 风险点：
- 影响面：
- 监控/回滚策略：

## 9. 兼容性与迁移（Compatibility / Migration）
- [ ] 无数据库变更
- [ ] 有数据库变更（说明 migration 与回滚方案）
- [ ] 有配置变更（说明新增/修改的环境变量或配置项）
- [ ] 有接口变更（说明影响调用方）

## 10. 关联 Issue / 工单
- Closes #____
- Related #____

## 11. 自检清单（Pre-merge Checklist）
- [ ] `git status` 无多余文件（临时文件/日志/数据目录未提交）
- [ ] `.gitignore` 已覆盖新增的本地/生成文件
- [ ] 无敏感信息（密码、Token、私钥、客户数据）
- [ ] 关键逻辑有必要的日志/注释
- [ ] 通过最小可用测试（能启动/核心流程可走通）
