# CLI 设计原则

1. CLI 是第一层 API（对人/对脚本）
2. help 必须可独立阅读
3. argparse 只做解析，业务逻辑不得写在 parser.py
4. 子命令统一 `set_defaults(func=...)`
5. 参数发布后避免破坏性修改（新增优于改名）
