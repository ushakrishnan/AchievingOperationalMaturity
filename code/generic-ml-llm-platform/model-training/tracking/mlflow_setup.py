import mlflow
from mlflow.tracking import MlflowClient

def setup_mlflow_tracking():
    # Set up MLflow tracking URI
    mlflow.set_tracking_uri("http://mlflow-server:5000")

    # Example experiment setup
    experiment_name = "LLM Training Experiment"
    client = MlflowClient()

    # Create or get the experiment
    experiment_id = client.create_experiment(experiment_name) if not client.get_experiment_by_name(experiment_name) else client.get_experiment_by_name(experiment_name).experiment_id

    print(f"MLflow tracking set up with URI: http://mlflow-server:5000 and experiment: {experiment_name}")

    return experiment_id

def log_sample_run(experiment_id):
    # Log a sample run
    with mlflow.start_run(experiment_id=experiment_id):
        mlflow.log_param("learning_rate", 0.001)
        mlflow.log_metric("accuracy", 0.95)
        mlflow.log_artifact("model_checkpoint.pt")

if __name__ == "__main__":
    experiment_id = setup_mlflow_tracking()
    log_sample_run(experiment_id)