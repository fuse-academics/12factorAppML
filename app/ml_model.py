import numpy as np
import os
from pathlib import Path
from functools import lru_cache
from .logging_config import logger
import joblib

MODEL_PATH_ENV = os.environ.get("MODEL_PATH", "./models/iris_dtree.joblib")
MODEL_PATH = Path(MODEL_PATH_ENV)

IRIS_CLASS_NAMES = ["setosa", "versicolor", "virginica"]


@lru_cache(maxsize=1)  # Cache the loaded model to avoid reloading on every call
def load_model():
    """Loads the trained model from disk. Cached for efficiency."""
    if not MODEL_PATH.exists():
        logger.error(f"Model file not found at {MODEL_PATH}")
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    try:
        model = joblib.load(MODEL_PATH)
        logger.info(f"Model loaded successfully from {MODEL_PATH}")
        return model
    except Exception as e:
        logger.error(f"Error loading model from {MODEL_PATH}: {e}", exc_info=True)
        raise


def predict_iris(features: np.ndarray) -> str:
    model = load_model()
    prediction = model.predict(features)[0]
    return IRIS_CLASS_NAMES[prediction]
