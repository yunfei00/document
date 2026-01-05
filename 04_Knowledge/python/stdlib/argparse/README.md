# argparse（Python 标准库 CLI 解析器）

`argparse` 是 Python 标准库里构建 CLI 的默认选择：稳定、零依赖、适合长期维护。

## 适用场景
- 工具型命令：数据生成、训练/评估、导入导出、离线部署脚本
- 企业内网/离线交付：不方便引入第三方依赖（click/typer）
- 需要子命令：`tool train ...` / `tool eval ...`

## 推荐你固定的工程范式
- `cli/parser.py`：只定义参数与子命令注册
- `cli/commands/*.py`：每个命令提供 `register()` + `run()`
- `cli/main.py`：入口，负责 logging/config/workdir 初始化与 dispatch

## 文件索引
- 00-overview.md：概念与适用场景
- 01-basic-usage.md：最常用写法（位置参数/可选参数）
- 02-advanced-usage.md：nargs/action/choices/互斥组/自定义 type
- 03-subcommands.md：子命令范式（set_defaults(func=...)）
- 04-engineering-patterns.md：工程规范（统一标准）
- 05-recipes.md：常用配方（你会反复复制）
- 06-pitfalls-and-tests.md：常见坑 + 如何测试 CLI
