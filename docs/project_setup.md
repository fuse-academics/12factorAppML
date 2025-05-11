---

## 📁 Project Structure

```
├── .github/               # GitHub-specific files (e.g., workflows, issue templates)
├── app/                   # Main application package
│   ├── __init__.py        # App package initializer
│   ├── crud.py/              # CRUD operations
│   ├── database.py/          # Database connection and models
│   ├── logging-config.py/    # Logging configuration
│   ├── main.py            # Application entry point
│   ├── ml-model.py/          # ML model inference logic
│   ├── models.py/            # ORM models
│   └── schemas.py/           # Pydantic schemas for request/response validation
├── data/
│   └── iris.db            # SQLite database file
├── docs/
│   └── index.md           # Documentation homepage (used by MkDocs)
├── env/                   # Environment-specific files or configurations
├── models/
│   └── iris_dtree.joblib  # Serialized ML model
├── scripts/
│   └── train_model.py     # Script to train and save the ML model
├── tests/
│   └── test.py            # Basic test(s) for the application
├── .Dockerfile            # Dockerfile for building the application image
├── .env                   # Environment variable definitions
├── .gitignore             # Git ignore file
├── docker-compose.yml     # Docker Compose configuration
└── mkdocs.yml             # MkDocs configuration for documentation
```

---
