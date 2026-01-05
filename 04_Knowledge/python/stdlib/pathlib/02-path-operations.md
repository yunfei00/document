# Path 常用操作速查

创建目录：
```python
Path("out").mkdir(parents=True, exist_ok=True)
```

读写文本：
```python
Path("a.txt").write_text("hi", encoding="utf-8")
txt = Path("a.txt").read_text(encoding="utf-8")
```

遍历：
```python
for f in Path("data").glob("**/*.csv"):
    print(f)
```
