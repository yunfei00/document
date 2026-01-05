# pathlib 基础用法

```python
from pathlib import Path
p = Path("data") / "raw" / "a.txt"
print(p.name, p.suffix, p.parent)
```
