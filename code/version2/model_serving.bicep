// Bicep template for Managed Model Serving and Inference
param location string = resourceGroup().location
param endpointName string

// Note: The resource type 'Microsoft.MachineLearningServices/workspaces/onlineEndpoints@2022-09-01' does not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
resource amlEndpoint 'Microsoft.MachineLearningServices/workspaces/onlineEndpoints@2022-09-01' = {
  name: endpointName
  location: location
  properties: {
    computeType: 'Managed'
  }
}

output amlEndpointId string = amlEndpoint.id
