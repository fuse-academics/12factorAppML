from pydantic import BaseModel


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }


class PredictionCreate(Iris):
    predicted_class: str


class PredictionResponse(PredictionCreate):
    id: int

    class Config:
        from_attributes = True
