# 常见坑 & 如何测试 CLI

## 常见坑（Top 10）
1. `required=True` 只对**可选参数**有效
2. 位置参数 `nargs="*"` 容易吞掉后续参数
3. `store_true` 默认 False，别误以为“默认 True”
4. 子命令忘了 `required=True`，导致无命令不报错
5. 子命令没 `set_defaults(func=...)`，dispatch 会失败
6. `type=int` 遇到空字符串会报错（预期内）
7. `choices` 的错误信息可读性一般（可加 help 提示）
8. help 里例子建议用 `epilog` + RawTextHelpFormatter
9. 同名参数冲突：多个子命令不要复用同一个短参数而语义不同
10. 解析时机：`parse_args()` 会立刻消费 argv，别在 import 时执行

## 如何测试 CLI（无第三方）
- 把 parser 构建成函数：`build_parser()`
- 测试时传入参数列表：`parser.parse_args(["train","--epochs","10"])`

示例：
```python
def test_train_parser():
    parser = build_parser()
    args = parser.parse_args(["train", "--epochs", "10"])
    assert args.epochs == 10
    assert args.command == "train"
```

## 建议：给每个子命令写 1 个解析测试
收益很高：避免发布后参数破坏。
