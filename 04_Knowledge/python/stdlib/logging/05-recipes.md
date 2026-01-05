# logging 常用配方

## 1) 添加 run_id（简单方式：logger.info 带字段）
```python
logger.info("start run_id=%s workdir=%s", run_id, workdir)
```

## 2) 把日志同时写文件（简化版）
```python
import logging
from pathlib import Path

def setup_logging_to_file(logfile: Path, verbosity: int) -> None:
    level = logging.INFO if verbosity >= 1 else logging.WARNING
    handlers = [logging.StreamHandler(), logging.FileHandler(logfile, encoding="utf-8")]
    logging.basicConfig(level=level, handlers=handlers,
                        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
```

## 3) 子模块降噪
```python
logging.getLogger("urllib3").setLevel(logging.WARNING)
```
