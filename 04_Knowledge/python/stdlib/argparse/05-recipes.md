# argparse 常用配方（复制即用）

## 1) Path 参数
```python
from pathlib import Path
parser.add_argument("--workdir", type=Path, default=Path("./workdir"))
```

## 2) -v / -vv
```python
parser.add_argument("-v", "--verbose", action="count", default=0)
```

## 3) 多个输入（至少 1 个）
```python
parser.add_argument("inputs", nargs="+")
```

## 4) 多选 + 累加（--include a b --include c）
```python
parser.add_argument("--include", nargs="+", action="extend", default=[])
```

## 5) append 标签（--tag a --tag b）
```python
parser.add_argument("--tag", action="append")
```

## 6) 子命令 register/run 模板
```python
# commands/foo.py
def register(subparsers):
    p = subparsers.add_parser("foo", help="do foo")
    p.add_argument("--x", type=int, default=1)
    p.set_defaults(func=run)

def run(args):
    ...
```
