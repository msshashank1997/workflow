$servicePrincipal = $env:secrets.SERVICE_PRINCIPAL_APPID
$servicePrincipalSecret = $env:secrets.SERVICE_PRINCIPAL_SECRET
$servicePrincipalTenantId = $env:secrets.SERVICE_PRINCIPAL_TENANTID
$azureSubscriptionName = $env:secrets.AZURE_SUBSCRIPTION_NAME
$subid= $env:secrets.AZURE_SUBSCRIPTION_ID
$serverName = "gihtubactions"
$adminLogin = $env:secrets.AZURE_SUBSCRIPTION_NAME
$adminPassword = $env:secrets.ADMIN_PASSWORD
  
$DID = 'DepID'
$rgname = 'host-'+$DID

#region Login
# This logs into Azure with a Service Principal Account

Write-Output "Logging in to Azure with a service principal..."

# Authenticate using the service principal (clientId and clientSecret)
$SecureClientSecret = ConvertTo-SecureString $servicePrincipalSecret -AsPlainText -Force
$psCred = New-Object System.Management.Automation.PSCredential($servicePrincipal, $servicePrincipalSecret)
Connect-AzAccount -ServicePrincipal -Credential $psCred -Tenant $servicePrincipalTenantId

#region Subscription
#This sets the subscription the resources will be created in

Write-Output "Setting default azure subscription..."
Set-AzContext -SubscriptionId $subid
Write-Output "Done"
Write-Output ""
#endregion

#region Create Resource Group
# This creates the resource group used to house the VM

Write-Output "Creating resource group $rgname in region eastus..."
New-AzResourceGroup -Name $rgname -Location "eastus"
Write-Output "Done creating resource group"
Write-Output ""

#region Create VM
# Create a VM in the resource group

try {
    New-AzResourceGroupDeployment -ResourceGroupName $rgname -TemplateFile .\main.bicep -TemplateParameterFile .\parameters.json
}
catch {
    Write-Output "VM already exists"
}
    
Write-Output "Done creating VM"
Write-Output ""
