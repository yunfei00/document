# argparse 标准

必须支持：
- `-v/-vv`（日志级别）
- `--workdir`（Path）

子命令标准：
- `add_subparsers(required=True)`
- 每个命令：`register(subparsers)` + `run(args)`
- 注册时：`p.set_defaults(func=run)`
