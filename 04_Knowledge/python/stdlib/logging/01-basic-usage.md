# logging 基础用法

模块级 logger（标准写法）：
```python
import logging
logger = logging.getLogger(__name__)

def run():
    logger.info("start")
```

常用级别：
- debug/info/warning/error/exception
