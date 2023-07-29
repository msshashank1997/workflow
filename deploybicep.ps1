$servicePrincipal = ${{ secrets.SERVICE_PRINCIPAL_APPID }}
$servicePrincipalSecret = ${{ secrets.SERVICE_PRINCIPAL_SECRET }} 
$servicePrincipalTenantId = ${{ secrets.SERVICE_PRINCIPAL_TENANTID }}
$azureSubscriptionName = ${{ secrets.AZURE_SUBSCRIPTION_NAME }}
$serverName = "gihtubactions"
  
$DID = 'DepID'

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
    New-AzResourceGroupDeployment -ResourceGroupName $rgname -TemplateUri 'bicepcontiner.azurecr.io/bicep/modules/main:v1' -TemplateParameterFile .\parameters.json
}
catch {
    Write-Output "VM already exists"
}
    
Write-Output "Done creating VM"
Write-Output ""
