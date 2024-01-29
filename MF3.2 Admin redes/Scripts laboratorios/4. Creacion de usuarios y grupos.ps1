# Crear un usuario cuyo nombre sea: Alumno, los apellidos Microsoff PowerShell, el logon sea AMicroPower y la contraseña UsrP@55w0rd
New-ADUser -DisplayName "Alumno Microsoft PowerShell" `
-GivenName "Alumno" `
-Surname "Microsoft PowerShell" `
-Name "Alumno Microsoft PowerShell" `
-SamAccountName "AMicroPower" `
-UserPrincipalName:"AMicroPower@CNTS.LOCAL" `
-ChangePasswordAtLogon $false `
-PasswordNeverExpires $true `
-AccountPassword (ConvertTo-SecureString `
-AsPlainText -String "UsrP@55w0rd" -Force) `
-Enabled $true

# Para crear múltiples usuarios:
# Primero hay que modificar la política de ejecucion pare permitir scripts no firmados
Set-ExecutionPolicy RemoteSigned

# Script que recibe los datos del .csv
Param ([Parameter(Mandatory=$true)] [string]$Nombre,
[Parameter(Mandatory=$true)] [string]$Apellido1,
[Parameter(Mandatory=$true)] [string]$Apellido2,
[Parameter(Mandatory=$true)] [string]$Logon)
$Dominio=(Get-ADDomain).DNSRoot
New-ADUser -DisplayName "$Nombre $Apellido1 $Apellido2" `
-GivenName "$Nombre" `
-Surname "$Apellidos" `
-Name "$Nombre $Apellido1 $Apellido2" `
-SamAccountName "$Logon" `
-UserPrincipalName:"$Logon@$Dominio" `
-ChangePasswordAtLogon $false `
-PasswordNeverExpires $true `
-AccountPassword (ConvertTo-SecureString `
-AsPlainText -String "UsrP@55w0rd" -Force) `
-Enabled $true

# Importar el .csv y tunelarlo al script anterior
Import-Csv .\UsuariosDominio.csv | ForEach-Object {.\CreacionUsuario.ps1 -Nombre $_.Nombre -Apellido1 $_.Apellido1 -Apellido2 $_.Apellido2 -Logon $_.Login}

# Creacion de grupos locales y globales
Ipmo ActiveDirectory

New-ADGroup -Name "_GAR-CNTS-POWERSHELL" `
-SamAccountName "_GAR-CNTS-POWERSHELL" `
-GroupCategory Security `
-GroupScope Global `
-DisplayName "_GAR-CNTS-POWERSHELL"

New-ADGroup -Name "_LAR-CNTS-POWERSHELL" `
-SamAccountName "_LAR-CNTS-POWERSHELL" `
-GroupCategory Security `
-GroupScope DomainLocal `
-DisplayName "_LAR-CNTS-POWERSHELL"

# Anidamiento de grupos
Add-ADGroupMember -Identity _LAR-CNTS-POWERSHELL -Members _GAR-CNTS-POWERSHELL
