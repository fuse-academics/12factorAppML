## Welcome to AI Fellowship 2025 Session

Welcome to the AI Fellowship 2025! This project demonstrates a minimal FastAPI application for classifying Iris flower species. The app follows the [12-Factor App](https://12factor.net/) methodology and is ideal for learning how to deploy scalable, maintainable machine learning APIs.

[**Python Ecosystem: Building a Twelve-Factor App**](https://docs.google.com/presentation/d/1LBbLwuu_I_SQEXBKM5zXfXhSn6_cSTMcFUWklmp2-AI/edit?usp=sharing)

## Demo Application

**[Click here to access the Iris Classification FastAPI App](https://aifellowship.regmiaayush.com.np/docs)**

This link opens the live API with Swagger documentation, where you can test the `/predict` and `/predictions` endpoint.

---

## Project Overview

This is a FastAPI-based microservice for predicting Iris flower species based on the sepal and petal measurements.

## Local Setup
```bash
# Cloning the repository
git clone https://github.com/fuse-academics/12factorAppML.git
cd 12factorAppML

# Creating and Activating Virtual Environment
python -m venv env
source env/bin/activate

# Installing dependencies
pip install -r requirements.txt

# Running docker-compose for building the application
docker compose up --build
```

```
#.env
# Add this to the .env file
DATABASE_URL = sqlite:///./data/iris.db
LOG_LEVEL = DEBUG
ENVIRONMENT = development # Staging and Production
MODEL_PATH = ./models/iris_dtree.joblib
PORT = 9000
HOST = 0.0.0.0
```