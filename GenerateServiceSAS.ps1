#This script is used to create Service SAS for a specific container which give external access
# Login to Azure
# Documentation : https://docs.microsoft.com/en-us/rest/api/storageservices/create-service-sas

Connect-AzAccount
$ResourceGroup = 'AZUODSOPSPROD'
$storageAccountName = 'ngmreportingprd'
$now=get-date
# Read, Create, List
$permission = "rclw"

$accountKeys = Get-AzStorageAccountKey -ResourceGroupName $ResourceGroup -Name $storageAccountName
$storageContext = New-AzStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $accountKeys[0].Value 
$token = New-AzStorageContainerSASToken -Name swenergy -Context $storageContext -Permission $permission -StartTime $now.AddHours(-1) -ExpiryTime $now.AddYears(1)




