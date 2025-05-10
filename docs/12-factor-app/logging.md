## 11. Logging

> **Treat logs as event streams**

Logs provide visibility into the behavior of a running app. In server-based environments they are commonly written to a file on disk (a “logfile”); but this is only an output format.

Logs are the stream of aggregated, time-ordered events collected from the output streams of all running processes and backing services. Logs in their raw form are typically a text format with one event per line (though backtraces from exceptions may span multiple lines). Logs have no fixed beginning or end, but flow continuously as long as the app is operating.

`logging-config.py`
```python
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
```


### Loguru

Loguru intends to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers

Installation: `pip install loguru`

```python
from loguru import logger

class Calculator:
    @staticmethod
    def add(a, b):
        logger.info(f"Adding {a} with {b}")
        return a + b
```

File Configuration: Add the following to the package __init__.py  which defines when to start overwriting your logs

```python
from loguru import logger

logger.add("logs/critical.log", level="CRITICAL", rotation="10MB")
logger.add("logs/error.log", level="ERROR", rotation="10MB")
logger.add("logs/warning.log", level="WARNING", rotation="10MB")
logger.add("logs/info.log", level="INFO", rotation="10MB")
logger.add("logs/debug.log", level="DEBUG", rotation="10MB")
```

</details>
