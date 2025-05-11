from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database, ml_model
from .logging_config import logger
import numpy as np

app = FastAPI(title="Iris Classification API")

models.Base.metadata.create_all(bind=database.engine)


@app.post("/predict/", response_model=schemas.PredictionResponse)
async def predict_iris(iris: schemas.Iris, db: Session = Depends(database.get_db)):
    logger.info(f"Received prediction request: {iris}")
    try:
        features = np.array(
            [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
        )
        prediction = ml_model.predict_iris(features)
        prediction_data = schemas.PredictionCreate(
            sepal_length=iris.sepal_length,
            sepal_width=iris.sepal_width,
            petal_length=iris.petal_length,
            petal_width=iris.petal_width,
            predicted_class=prediction,
        )
        db_prediction = crud.create_prediction(db, prediction_data)
        logger.info(f"Prediction stored: {prediction}")
        return db_prediction
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/predictions/", response_model=List[schemas.PredictionResponse])
async def get_predictions(db: Session = Depends(database.get_db)):
    logger.info("Fetching all predictions")
    predictions = crud.get_predictions(db)
    return predictions
