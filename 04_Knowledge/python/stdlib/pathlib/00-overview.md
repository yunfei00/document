# pathlib 概览

为什么用 Path：
- 可读性强：`Path("a") / "b"`
- 跨平台：自动处理分隔符
- 操作集中：exists/mkdir/read_text/write_text/glob

与 os.path：
- 工程建议统一用 Path
- 与旧接口交互在边界处 `str(path)`
