# Version 2: SaaS-Like Supported Platforms and Solutions

This folder contains Bicep templates for deploying an end-to-end ML and LLM platform using managed services for simplicity and scalability. Each file corresponds to a specific component of the platform.

## Files and Their Purpose

1. **gpu_vm.bicep**
   - Provisions a managed AKS cluster with Nvidia GPU support for infrastructure and orchestration.

2. **data_pipeline.bicep**
   - Sets up Azure Data Factory for managed data preparation and validation.

3. **model_training.bicep**
   - Creates an Azure Machine Learning workspace and GPU-enabled compute cluster for managed model development.

4. **model_serving.bicep**
   - Deploys a managed Azure ML Endpoint for model serving and inference.

5. **monitoring.bicep**
   - Configures a Log Analytics workspace for managed monitoring and observability.

## How to Use These Files

1. **Prerequisites**:
   - Ensure you have the Azure CLI installed and authenticated.
   - Install the Bicep CLI or use Azure CLI with Bicep support.

2. **Deployment Steps**:
   - Navigate to the `version2` folder.
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

3. **model_serving.bicep**:
   - The resource type `Microsoft.MachineLearningServices/workspaces/onlineEndpoints@2022-09-01` does not have types available for validation in Bicep. Ensure all properties are correctly defined before deployment.

4. **monitoring.bicep**:
   - The resource type `Microsoft.OperationalInsights/workspaces@2022-09-01` does not have types available for validation in Bicep. Ensure all properties are correctly defined before deployment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.