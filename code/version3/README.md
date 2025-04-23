# Version 3: Open Source for Portability Across All Hyperscalers

This folder contains the implementation of Version 3, which focuses on using open-source tools and frameworks to ensure portability across all hyperscalers. The components are designed to be vendor-agnostic, leveraging open-source technologies for infrastructure, data processing, model development, serving, and monitoring.

## Key Components

1. **Infrastructure & Orchestration**
   - Provision VMs using open-source virtualization tools like KVM or Xen.
   - Use Docker or Podman for containerization with Nvidia Container Toolkit for GPU acceleration.
   - Kubernetes setup includes autoscaling and load balancing.

2. **Data Preparation, Validation, and Augmentation**
   - Data preparation with Apache Spark or Dask.
   - Data validation using Great Expectations, including schema validation.
   - Data augmentation with Albumentations and AugLy.
   - Synthetic data generation using SDV (Synthetic Data Vault).

3. **Data Ingestion, Lineage, and Contracts**
   - Data storage with MinIO or Apache Hadoop.
   - Data processing with Apache Spark or Dask.

4. **Model Development**
   - Jupyter Notebooks with TensorFlow, PyTorch, and Nvidia RAPIDS.
   - Model training with TensorFlow or PyTorch using Nvidia CUDA.
   - Mixed precision training for performance optimization.

5. **Model Serving and Inference**
   - Deploy models using Triton Inference Server on Kubernetes.
   - Use Kong or Traefik as API gateways.
   - Multi-model serving support added to FastAPI application.

6. **Guardrails, Privacy & Governance**
   - Prompt protection with Guardrails AI or Rebuff.
   - PII redaction using Presidio, with enhanced logging and testing configurations.
   - Access control with Keycloak and OPA.

7. **LLMOps & Evaluation**
   - Prompt observability with LangSmith or PromptLayer, including observability logging.
   - Experiment tracking with MLflow or WandB.
   - LLM evaluation using TruLens, Ragas, or LLMUnit, with tracking logging added.

8. **Monitoring, Observability & Cost**
   - Monitoring with Prometheus and Grafana, integrated with Kubernetes.
   - Cost management with Kubecost.

## Recent Updates

- **Infrastructure Enhancements**:
  - Added GPU acceleration support in `provision_vms.sh`.
  - Integrated Kubernetes autoscaling and load balancing setup.

- **Data Pipeline Improvements**:
  - Added distributed processing with Dask in `data_preparation.py`.
  - Included data augmentation and synthetic data generation examples.

- **Model Training Enhancements**:
  - Introduced mixed precision training in `train_model.py` for performance optimization.

- **Model Serving Updates**:
  - Added multi-model serving capability to `serve_model.py`.

- **Privacy and Governance**:
  - Enhanced Presidio and Guardrails AI configurations with logging and testing instructions.

- **LLMOps Improvements**:
  - Added observability logging to PromptLayer integration.
  - Introduced tracking logging in TruLens evaluation script.

- **Monitoring Setup**:
  - Documented Prometheus, Grafana, and Kubecost setup in this README.

## How to Use

Each component is implemented in its respective subfolder. Follow the instructions in the subfolders to set up and run the components.

### Infrastructure Setup
1. Run the `provision_vms.sh` script to provision VMs with GPU acceleration and Kubernetes setup.
2. Apply Kubernetes manifests for autoscaling and load balancing.

### Data Pipeline
1. Use `data_preparation.py` for data cleansing, augmentation, and synthetic data generation.
2. Validate datasets with `data_validation.py` using Great Expectations.

### Model Training
1. Train models using `train_model.py` with mixed precision training enabled.
2. Use Jupyter Notebooks for experimentation.

### Model Serving
1. Deploy models using `serve_model.py` or Triton Inference Server.
2. Use Kubernetes for scalable deployment.

### Monitoring and Observability
1. Deploy Prometheus and Grafana:
   ```bash
   kubectl apply -f prometheus-grafana.yaml
   ```
2. Deploy Kubecost:
   ```bash
   kubectl apply -f kubecost.yaml
   ```
3. Access dashboards:
   - Prometheus: `http://<prometheus-url>`
   - Grafana: `http://<grafana-url>`
   - Kubecost: `http://<kubecost-url>`

## Known Issues

1. **Dependency Installation**:
   - Ensure all required Python packages are installed. Missing dependencies can cause import errors.
   - Use the `pip install` commands mentioned in the scripts to resolve dependency issues.

2. **Infrastructure Setup**:
   - Administrative privileges are required to run the `provision_vms.sh` script.
   - Ensure the host machine supports virtualization and has sufficient resources for VM provisioning.

3. **Data Pipeline**:
   - Large datasets may cause memory issues during data preparation or validation. Consider using distributed processing frameworks like Apache Spark.
   - Data validation may fail if the schema or expectations are not properly defined in Great Expectations.

4. **Model Training**:
   - Ensure the training dataset is available and correctly formatted.
   - GPU acceleration requires compatible hardware and drivers (e.g., Nvidia CUDA).

5. **Model Serving**:
   - Ensure the trained model file (`mnist_model.pth`) exists before running the serving script.
   - Use the correct API endpoints as defined in the FastAPI application.
   - Verify that the serving environment has sufficient resources (e.g., memory, GPU).

6. **General Troubleshooting**:
   - Check log files for detailed error messages.
   - Ensure all environment variables are correctly set as per the documentation.
   - For any unresolved issues, open a GitHub issue or contact the maintainers.