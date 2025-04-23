# Version 1: Full Control and Customization

This folder contains Bicep templates for deploying an end-to-end ML and LLM platform with full control and customization. Each file corresponds to a specific component of the platform.

## Files and Their Purpose

1. **gpu_vm.bicep**
   - Provisions GPU-optimized virtual machines (VMs) for running AI workloads.
   - Includes secure configurations and autoscaling options.

2. **data_pipeline.bicep**
   - Sets up data preparation, validation, and augmentation pipelines.
   - Provisions Azure Storage and Data Factory resources.

3. **model_training.bicep**
   - Creates an Azure Machine Learning workspace and GPU-enabled compute cluster for model development.

4. **model_serving.bicep**
   - Deploys an Azure Kubernetes Service (AKS) cluster and inference server for model serving and inference.

5. **monitoring.bicep**
   - Configures monitoring and observability using Azure Monitor and Log Analytics.

## How to Use These Files

1. **Prerequisites**:
   - Ensure you have the Azure CLI installed and authenticated.
   - Install the Bicep CLI or use Azure CLI with Bicep support.

2. **Deployment Steps**:
   - Navigate to the `version1` folder.
   - Deploy each Bicep file using the following command:
     ```bash
     az deployment group create --resource-group <RESOURCE_GROUP> --template-file <FILE_NAME>
     ```
   - Replace `<RESOURCE_GROUP>` with your Azure resource group name and `<FILE_NAME>` with the name of the Bicep file.

3. **Order of Deployment**:
   - Deploy `gpu_vm.bicep` first to set up the infrastructure.
   - Deploy `data_pipeline.bicep` for data preparation.
   - Deploy `model_training.bicep` for model development.
   - Deploy `model_serving.bicep` for model serving.
   - Deploy `monitoring.bicep` for monitoring and observability.

## Additional Information

- **Security**: All templates follow Azure best practices for security, including encryption and role-based access control (RBAC).
- **Customization**: Modify the parameters in each Bicep file to suit your specific requirements.
- **Support**: For issues or questions, refer to the main repository's documentation or contact the maintainer.

## Known Issues

1. **data_pipeline.bicep**:
   - The resource type `Microsoft.DataFactory/factories@2022-09-01` does not have types available for validation in Bicep. Ensure all properties are correctly defined before deployment.

2. **model_training.bicep**:
   - The resource types `Microsoft.MachineLearningServices/workspaces@2022-09-01` and `Microsoft.MachineLearningServices/workspaces/computes@2022-09-01` do not have types available for validation in Bicep. Ensure all properties are correctly defined before deployment.

3. **monitoring.bicep**:
   - The resource types `Microsoft.OperationalInsights/workspaces@2022-09-01` and `Microsoft.Insights/components@2022-09-01` do not have types available for validation in Bicep. Ensure all properties are correctly defined before deployment.

## Suggested Improvements for Code Files

### Infrastructure
- **`gpu_vm.bicep`**:
  - Provisions GPU-optimized VMs for AI workloads.
  - **Improvements**:
    - Add support for Kubernetes orchestration.
    - Include GPU monitoring tools like Nvidia DCGM.

### Data Pipeline
- **`data_pipeline.bicep`**:
  - Sets up data preparation, validation, and augmentation pipelines.
  - **Improvements**:
    - Add support for distributed data processing frameworks like Apache Spark.
    - Integrate data validation tools like Great Expectations.

### Model Training
- **`model_training.bicep`**:
  - Creates an Azure Machine Learning workspace and GPU-enabled compute cluster.
  - **Improvements**:
    - Add mixed precision training support.
    - Include experiment tracking tools like MLflow.

### Model Serving
- **`model_serving.bicep`**:
  - Deploys an Azure Kubernetes Service (AKS) cluster and inference server for model serving and inference.
  - **Improvements**:
    - Add multi-model serving capabilities.
    - Integrate with an API gateway for secure access.

### Monitoring
- **`monitoring.bicep`**:
  - Configures monitoring and observability using Azure Monitor and Log Analytics.
  - **Improvements**:
    - Add support for Prometheus and Grafana for real-time monitoring.
    - Include cost management tools like Kubecost.

## License

This project is licensed under the MIT License. See the LICENSE file for details.