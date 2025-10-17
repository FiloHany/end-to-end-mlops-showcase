import mlflow
import logging
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("mlops.log"),
        logging.StreamHandler()
    ]
    )
logging.info("Starting training script")


logging.info("Loading dataset")
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
logging.info("Dataset loaded and split into train and test sets")
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    logging.info("Model training completed")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model accuracy: {accuracy}")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("accuracy", accuracy)
    
    mlflow.sklearn.log_model(model, "model")
    logging.info("Model logged to MLflow")
    print(f"Model accuracy: {accuracy}")
    logging.info("Training script completed")