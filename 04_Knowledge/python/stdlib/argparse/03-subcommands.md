# argparse 子命令（git 风格）

## 推荐范式：set_defaults(func=...)
```python
import argparse

def cmd_train(args):
    print("train", args.epochs, args.lr)

def cmd_eval(args):
    print("eval", args.ckpt)

def main():
    parser = argparse.ArgumentParser(prog="tool")
    sub = parser.add_subparsers(dest="command", required=True)

    p_train = sub.add_parser("train", help="train a model")
    p_train.add_argument("--epochs", type=int, default=50)
    p_train.add_argument("--lr", type=float, default=1e-3)
    p_train.set_defaults(func=cmd_train)

    p_eval = sub.add_parser("eval", help="evaluate")
    p_eval.add_argument("--ckpt", required=True)
    p_eval.set_defaults(func=cmd_eval)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
```

## 设计建议
- 子命令必须 `required=True`
- 子命令函数签名统一 `func(args)`
- argparse 只做参数解析，业务逻辑放到 commands/service
