# argparse 高级用法（容易忘/容易踩坑）

## nargs：参数个数控制
- `nargs=2`：必须两个值
- `nargs="?"`：0 或 1 个
- `nargs="*"`：0 到多个
- `nargs="+"`：1 到多个

```python
parser.add_argument("files", nargs="+")          # 至少一个
parser.add_argument("--ids", nargs="*", type=int) # 可多个
```

## action：收集/计数/布尔
### count（-v -vv -vvv）
```python
parser.add_argument("-v", "--verbose", action="count", default=0)
```

### append（允许多次出现）
```python
parser.add_argument("--tag", action="append")  # --tag a --tag b -> ["a","b"]
```

## choices：限定可选值
```python
parser.add_argument("--mode", choices=["train", "eval"], required=True)
```

## mutually_exclusive_group：互斥参数
```python
mx = parser.add_mutually_exclusive_group(required=True)
mx.add_argument("--cpu", action="store_true")
mx.add_argument("--gpu", action="store_true")
```

## 自定义 type：更好的错误信息
```python
import argparse

def positive_int(s: str) -> int:
    v = int(s)
    if v <= 0:
        raise argparse.ArgumentTypeError("must be > 0")
    return v

parser.add_argument("--workers", type=positive_int)
```

## 常见坑（重点）
1. `required=True` 只对 **可选参数**有效；位置参数天然必填（除非 `nargs="?"`）
2. `nargs="*"` 容易“吞掉”后续位置参数，位置参数慎用
3. `store_true` 默认 False，别忘了默认值逻辑
