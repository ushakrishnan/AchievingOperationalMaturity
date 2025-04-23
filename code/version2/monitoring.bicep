// Bicep template for Managed Monitoring and Observability
param location string = resourceGroup().location
param logAnalyticsWorkspaceName string

// Note: The resource type 'Microsoft.OperationalInsights/workspaces@2022-09-01' does not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-09-01' = {
  name: logAnalyticsWorkspaceName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
  }
}

output logAnalyticsWorkspaceId string = logAnalyticsWorkspace.id
