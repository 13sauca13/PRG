# Listar las características que pueden ser instaladas
Get-WindowsFeature *AD*

# Intalar el servicio "AD-Domain-Services"
Add-WindowsFeature -Name AD-Domain-Services

# Instalar los servicios que no se instalaron previamente
Add-WindowsFeature RSAT-ADDS -IncludeAllSubFeature
Add-WindowsFearure GPMC

# Ejecutar el script de configuración de AD
Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "E:\AD\NTDS" `
-DomainMode "WinThreshold" `
-DomainName "CNTS.LOCAL" `
-DomainNetbiosName "CNTS" `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "E:\AD\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "E:\AD\SYSVOL" `
-Force:$true