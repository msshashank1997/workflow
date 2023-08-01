# This IaC script provisions a VM within Azure
#
[CmdletBinding()]
param(
    [Parameter(Mandatory = $True)]
    [string]
    $servicePrincipal,

    [Parameter(Mandatory = $True)]
    [string]
    $servicePrincipalSecret,

    [Parameter(Mandatory = $True)]
    [string]
    $servicePrincipalTenantId,

    [Parameter(Mandatory = $True)]
    [string]
    $azureSubscriptionName,

    [Parameter(Mandatory = $True)]
    [string]
    $resourceGroupName,

    [Parameter(Mandatory = $True)]
    [string]
    $resourceGroupNameRegion,

    [Parameter(Mandatory = $True)]  
    [string]
    $serverName,

    [Parameter(Mandatory = $True)]  
    [string]
    $adminLogin,

    [Parameter(Mandatory = $True)]  
    [String]
    $adminPassword
)
  
$DID = '55679'
$rgname = 'host-'+$DID

#region Login
# This logs into Azure with a Service Principal Account

Write-Output "Logging in to Azure with a service principal..."
az login `
    --service-principal `
    --username $servicePrincipal `
    --password $servicePrincipalSecret `
    --tenant $servicePrincipalTenantId
Write-Output "Done"
Write-Output ""

#region Subscription
#This sets the subscription the resources will be created in

Write-Output "Setting default azure subscription..."
az account set `
    --subscription $azureSubscriptionName
Write-Output "Done"
Write-Output ""
#endregion

#region Create Resource Group
# This creates the resource group used to house the VM

Write-Output "Creating resource group $rgname in region eastus..."
az group create `
    --name $rgname `
    --location "eastus"
    Write-Output "Done creating resource group"
    Write-Output ""

#region Create VM
# Create a VM in the resource group

try {
    az deployment group create --resource-group MyResourceGroup --template-file main.bicep --parameters parameters.json
}
catch {
    Write-Output "VM already exists"
}
    
Write-Output "Done creating VM"
Write-Output ""
