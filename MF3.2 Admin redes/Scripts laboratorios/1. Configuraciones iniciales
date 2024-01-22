# Ver los interfaces de red que posee el servidor
Get-NetIPAddress | where AddressFamily -eq ‘IPv4’ | select InterfaceAlias, IPAddress

# Configurar la dirección de red, máscara y puerta de enlace
New-NetIPAddress -InterfaceAlias Ethernet -AddressFamily IPv4 -IPAddress 172.16.0.254 -PrefixLength 24 -Defaultgateway 172.16.0.1

# Configurar los DNS
Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 172.16.0.254

# Deshabilitar IPv6
reg add "HKLM\System\CurrentControlSet\Services\TCPIP6\Parameters" /v "DisabledComponents" /t REG_DWORD /d 0x000000FF
reg add "HKLM\System\CurrentControlSet\Services\TCPIP6\Parameters" /v " DisableIPSourceRouting" /t REG_DWORD /d 0x0000002

# Habilitar escritorio remoto
Enable-NetFirewallRule -DisplayGroup "Escritorio Remoto"
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\TerminalServer\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1

# Cambiar el nombre del equipo
Rename-Computer SRVCNTSCDW01
