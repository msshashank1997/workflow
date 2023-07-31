metadata description = 'Creates a Basic VM'

targetScope = 'resourceGroup'

//parameter declartion
param adminUsername string
@description('Password for the Virtual Machine.')
@minLength(12)
@secure()
param adminPassword string
param DeploymentID string
param location string = resourceGroup().location

//Variable declartion
var vmName = 'labvm-${DeploymentID}'
var addressPrefix = '10.0.0.0/16'
var networkInterfaceName = '${vmName}-nic'
var networkSecurityGroupName = '${vmName}-nsg'
var publicIpAddressDNSName = '${vmName}-dns-${DeploymentID}' //prefer-interpolation
var publicIpAddressName = '${vmName}-pip'
var subnetName = 'Subnet'
var subnetPrefix = '10.0.0.0/24'
var virtualMachineSize = 'Standard_D4s_v3'
var virtualNetworkName = 'labvNet'

module publicIP 'br:bicepcontiner.azurecr.io/bicep/modules/publicip:v1' = {
  name: 'publicIP'
  params: {
    publicIpAddressDNSName: publicIpAddressDNSName
    location: location
    publicIpAddressName: publicIpAddressName
  }
}

module nsg 'br:bicepcontiner.azurecr.io/bicep/modules/nsg:v1' = {
  name: 'nsg'
  params: {
    networkSecurityGroupName: networkSecurityGroupName
    location: location
  }
}

module virtualnetwork 'br:bicepcontiner.azurecr.io/bicep/modules/virtualnetwork:v1' = {
  name: 'VN'
  params: {
    virtualNetworkName: virtualNetworkName
    location: location
    addressPrefix: addressPrefix
    subnetName: subnetName
    subnetPrefix: subnetPrefix
    nsgid: nsg.outputs.nsfid
  }
}

module networkinterface 'br:bicepcontiner.azurecr.io/bicep/modules/networkinterfaces:v1' = {
  name: 'networkinterface'
  params: {
    networkInterfaceName: networkInterfaceName
    location: location
    publicipID: publicIP.outputs.publicaddressid
    virtualNetworkName: virtualNetworkName
    subnetName: subnetName
    networkSecurityGroupName: networkSecurityGroupName
  }
  dependsOn: [
    virtualnetwork
  ]
}

module virtualMachine 'br:bicepcontiner.azurecr.io/bicep/modules/windowsvm:v1' = {
  name: 'vmName'
  params: {
    vmName: vmName
    location: location
    adminUsername: adminUsername
    adminPassword: adminPassword
    virtualMachineSize: virtualMachineSize
    networkInterfaceid: networkinterface.outputs.networkInterfaceid
  }
}

output deploymetid string = DeploymentID
output username string = adminUsername
output password string = adminPassword
output dns string = publicIP.outputs.dns
