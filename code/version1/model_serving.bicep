// Bicep template for Model Serving and Inference
param location string = resourceGroup().location
param aksClusterName string
param inferenceServerName string

resource aksCluster 'Microsoft.ContainerService/managedClusters@2022-09-01' = {
  name: aksClusterName
  location: location
  properties: {
    kubernetesVersion: '1.25.6'
    agentPoolProfiles: [
      {
        name: 'nodepool1'
        count: 3
        vmSize: 'Standard_NC6s_v3'
        osType: 'Linux'
      }
    ]
  }
}

resource inferenceServer 'Microsoft.ContainerService/managedClusters/agentPools@2022-09-01' = {
  name: inferenceServerName
  parent: aksCluster
  properties: {
    count: 1
    vmSize: 'Standard_NC6s_v3'
  }
}

output aksClusterId string = aksCluster.id
output inferenceServerId string = inferenceServer.id
