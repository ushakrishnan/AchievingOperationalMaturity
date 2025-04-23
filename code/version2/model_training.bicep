// Bicep template for Managed Model Development
// Note: The resource types 'Microsoft.MachineLearningServices/workspaces@2022-09-01' and 'Microsoft.MachineLearningServices/workspaces/computes@2022-09-01' do not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
param location string = resourceGroup().location
param workspaceName string
param computeName string

resource amlWorkspace 'Microsoft.MachineLearningServices/workspaces@2022-09-01' = {
  name: workspaceName
  location: location
  properties: {}
}

resource amlCompute 'Microsoft.MachineLearningServices/workspaces/computes@2022-09-01' = {
  name: computeName
  parent: amlWorkspace
  properties: {
    computeType: 'AmlCompute'
    properties: {
      vmSize: 'Standard_NC6s_v3'
    }
  }
}

output amlWorkspaceId string = amlWorkspace.id
output amlComputeId string = amlCompute.id
