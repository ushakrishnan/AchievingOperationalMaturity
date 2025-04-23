# Version 3: Open Source for Portability Across All Hyperscalers

This folder contains the implementation of Version 3, which focuses on using open-source tools and frameworks to ensure portability across all hyperscalers. The components are designed to be vendor-agnostic, leveraging open-source technologies for infrastructure, data processing, model development, serving, and monitoring.

## Key Components

1. **Infrastructure & Orchestration**
   - Provision VMs using open-source virtualization tools like KVM or Xen.
   - Use Docker or Podman for containerization with Nvidia Container Toolkit for GPU acceleration.

2. **Data Preparation, Validation, and Augmentation**
   - Data preparation with Apache Spark or Dask.
   - Data validation using Great Expectations.
   - Data augmentation with Albumentations and AugLy.
   - Synthetic data generation using SDV (Synthetic Data Vault).

3. **Data Ingestion, Lineage, and Contracts**
   - Data storage with MinIO or Apache Hadoop.
   - Data processing with Apache Spark or Dask.

4. **Model Development**
   - Jupyter Notebooks with TensorFlow, PyTorch, and Nvidia RAPIDS.
   - Model training with TensorFlow or PyTorch using Nvidia CUDA.

5. **Model Serving and Inference**
   - Deploy models using Triton Inference Server on Kubernetes.
   - Use Kong or Traefik as API gateways.

6. **Guardrails, Privacy & Governance**
   - Prompt protection with Guardrails AI or Rebuff.
   - PII redaction using Presidio.
   - Access control with Keycloak and OPA.

7. **LLMOps & Evaluation**
   - Prompt observability with LangSmith or PromptLayer.
   - Experiment tracking with MLflow or WandB.
   - LLM evaluation using TruLens, Ragas, or LLMUnit.

8. **Monitoring, Observability & Cost**
   - Monitoring with Prometheus and Grafana.
   - Cost management with Kubecost.

## How to Use

Each component is implemented in its respective subfolder. Follow the instructions in the subfolders to set up and run the components.

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