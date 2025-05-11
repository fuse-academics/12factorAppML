from sqlalchemy.orm import Session
from . import models, schemas

def create_prediction(db: Session, prediction: schemas.PredictionCreate):
    db_prediction = models.Prediction(**prediction.model_dump())
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def get_predictions(db: Session):
    return db.query(models.Prediction).all()