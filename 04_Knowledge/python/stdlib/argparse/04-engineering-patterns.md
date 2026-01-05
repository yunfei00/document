# argparse 工程规范（统一标准）

## 统一要求
1. 所有 CLI 都支持：
   - `-v/-vv` 控制日志级别
   - `--workdir` 指定工作目录（Path）
2. 参数命名：CLI 用 kebab-case；dest 用 snake_case
3. argparse 只负责参数定义与校验；业务逻辑放 commands

## 建议目录结构
```text
cli/
├─main.py
├─parser.py
└─commands/
   ├─train.py
   └─eval.py
```

## -v 规则
- 0：WARNING
- 1：INFO
- 2+：DEBUG
