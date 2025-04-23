// Bicep template for Managed Data Preparation and Validation
param location string = resourceGroup().location
param dataFactoryName string

// Note: The resource type 'Microsoft.DataFactory/factories@2022-09-01' does not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
resource dataFactory 'Microsoft.DataFactory/factories@2022-09-01' = {
  name: dataFactoryName
  location: location
  properties: {}
}

output dataFactoryId string = dataFactory.id
