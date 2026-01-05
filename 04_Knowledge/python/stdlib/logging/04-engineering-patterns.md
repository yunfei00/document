# logging 工程规范（建议强制）

1. 禁止 print（测试脚本除外）
2. 模块级 logger：`logger = logging.getLogger(__name__)`
3. 入口层统一配置，不允许各模块重复 basicConfig
4. except 中用 `logger.exception(...)`
5. 日志写事实，不写情绪
