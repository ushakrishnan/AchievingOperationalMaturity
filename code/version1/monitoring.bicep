// Bicep template for Monitoring, Observability, and Cost Management
// Note: The resource types 'Microsoft.OperationalInsights/workspaces@2022-09-01' and 'Microsoft.Insights/components@2022-09-01' do not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
param location string = resourceGroup().location
param logAnalyticsWorkspaceName string
param monitorName string

resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-09-01' = {
  name: logAnalyticsWorkspaceName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
  }
}

resource monitor 'Microsoft.Insights/components@2022-09-01' = {
  name: monitorName
  location: location
  properties: {
    Application_Type: 'web'
  }
}

output logAnalyticsWorkspaceId string = logAnalyticsWorkspace.id
output monitorId string = monitor.id
