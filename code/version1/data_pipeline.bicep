// Bicep template for Data Preparation, Validation, and Augmentation
param location string = resourceGroup().location
param storageAccountName string
param dataFactoryName string

resource storageAccount 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {}
}

// Note: The resource type 'Microsoft.DataFactory/factories@2022-09-01' does not have types available for validation in Bicep.
// Ensure that all properties are correctly defined before deployment.
resource dataFactory 'Microsoft.DataFactory/factories@2022-09-01' = {
  name: dataFactoryName
  location: location
  properties: {}
}

output storageAccountId string = storageAccount.id
output dataFactoryId string = dataFactory.id
