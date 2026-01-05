# pathlib 工程规范

1. CLI 解析路径参数时用 `type=Path`
2. 内部函数参数统一用 Path（不要混用 str）
3. 对外接口需要 str 时在边界转换：`str(path)`
4. 写文件前确保目录存在（mkdir parents）
