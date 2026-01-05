# argparse 基础用法（你以后最常翻）

## 最小可用示例（位置参数 + 可选参数）
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo CLI")
    parser.add_argument("input", help="input file path")
    parser.add_argument("-o", "--output", default="out.txt", help="output file path")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")

    args = parser.parse_args()
    print(args.input, args.output, args.verbose)

if __name__ == "__main__":
    main()
```

运行：
```bash
python cli.py data.txt -o result.txt -v
```

## 位置参数 vs 可选参数
- 位置参数：不带 `-`，按顺序出现（通常必填）
- 可选参数：带 `-`/`--`，可任意顺序出现

## 常用字段
- `help`：帮助文案
- `default`：默认值
- `type`：自动转换（int/float/Path）
- `required=True`：仅用于可选参数

## 布尔开关（store_true）
```python
parser.add_argument("--dry-run", action="store_true")
```
- 不写：False
- 写了：True
