# 环境变量

建议加前缀：NFS_ / IMS_
示例：
```python
import os
from pathlib import Path
workdir = Path(os.getenv("NFS_WORKDIR", "./workdir"))
```
