## 9. Disposability

> **Maximize robustness with fast startup and graceful shutdown.**

- Disposable project means that the app is easy to deploy and start, and can be stopped at moment's notice (when they receive SIGTERM).
- Short startup time enable fast elastic scaling, rapid deployment of code or config changes, and robustness of production deploys.

Processes shut down gracefully when they receive a SIGTERM signal from the process manager and should be robust against sudden death in case of underlying hardware failure.


### [Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}

```
