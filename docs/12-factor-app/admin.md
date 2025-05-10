## 12. Admin processes

> **Run admin/management tasks as one-off processes**

The process formation is the array of processes that are used to do the app’s regular business (such as handling web requests) as it runs. Separately, developers will often wish to do one-off administrative or maintenance tasks for the app, such as:

- Schedule Model Training/Update
- Running database migrations (e.g. manage.py migrate in Django, rake db:migrate in Rails).
- Running one-time scripts committed into the app’s repo

`train_model.py`
```python
import os
from pathlib import Path
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_PATH = MODEL_DIR / "iris_dtree.joblib"


def train_and_save_model():
    """Loads iris data, trains a simple model, and saves it."""
    print("Loading data...")
    iris = load_iris()
    X, y = iris.data, iris.target
    # Using target names for clarity in prediction later if needed
    # target_names = iris.target_names

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Training Logistic Regression model...")
    # Simple model, less sensitive to feature scaling for this dataset
    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=41,
    )
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Model trained. Test Accuracy: {accuracy*100:.4f}%")

    # Ensure the save directory exists
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Saving model to: {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    print("Model saved successfully.")


if __name__ == "__main__":
    train_and_save_model()

```
```bash
docker exec -it <container_name> bash -c "cd /app && python scripts/train_model.py"
```

One-off admin processes should be run in an identical environment as the regular long-running processes of the app. They run against a release, using the same codebase and config as any process run against that release. Admin code must ship with application code to avoid synchronization issues. The same dependency isolation techniques should be used on all process types
