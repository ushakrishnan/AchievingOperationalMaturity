// Bicep template for Managed GPU-Optimized Services
param location string = resourceGroup().location
param aksClusterName string
param nodePoolName string

resource aksCluster 'Microsoft.ContainerService/managedClusters@2022-09-01' = {
  name: aksClusterName
  location: location
  properties: {
    kubernetesVersion: '1.25.6'
    agentPoolProfiles: [
      {
        name: nodePoolName
        count: 3
        vmSize: 'Standard_NC6s_v3'
        osType: 'Linux'
      }
    ]
  }
}

output aksClusterId string = aksCluster.id
