import pytest
import sys
import os
from fastapi.testclient import TestClient
from app.main import app
from app import database, models, schemas, crud
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(test_db):
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[database.get_db] = override_get_db
    return TestClient(app)


@pytest.fixture
def seed_test_data(db_session):
    sample_data = [
        schemas.PredictionCreate(
            sepal_length=5.1,
            sepal_width=3.5,
            petal_length=1.4,
            petal_width=0.2,
            predicted_class="setosa",
        ),
        schemas.PredictionCreate(
            sepal_length=7.0,
            sepal_width=3.2,
            petal_length=4.7,
            petal_width=1.4,
            predicted_class="versicolor",
        ),
    ]
    for data in sample_data:
        crud.create_prediction(db_session, data)
    return sample_data


@pytest.mark.asyncio
async def test_predict_iris(client):
    response = client.post(
        "/predict/",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["predicted_class"] in ["setosa", "versicolor", "virginica"]
    assert response_data["sepal_length"] == 5.1
    assert response_data["sepal_width"] == 3.5
    assert response_data["petal_length"] == 1.4
    assert response_data["petal_width"] == 0.2
    assert isinstance(response_data["id"], int)


@pytest.mark.asyncio
async def test_get_predictions(client, seed_test_data):
    response = client.get("/predictions/")
    assert response.status_code == 200
    predictions = response.json()
    assert isinstance(predictions, list)
    assert len(predictions) >= 2  # At least the seeded data
    assert predictions[0]["predicted_class"] == "setosa"
    assert predictions[1]["predicted_class"] == "setosa"
