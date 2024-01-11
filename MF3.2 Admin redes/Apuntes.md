# Administracion de redes

## 1. Windows Server
### 1.1 Versiones
Se emplea como O.S. para servidores. Para cada versión de estación de trabajo sale una versión de Windows Server, las versiones comparten el mismo núcleo.

| Servidor | Estación de trabajo |
| --- | --- |
| Windows Server 2008 | Windows 7 |
| Windows Server 2012 | Windows 8 y 8.1 |
| Windows Server 2016 y 2019 | Windows 10 |

#### Versiones:
+ **Datacenter**: Para entornos virtualizados.
+ **Standard**: Para entornos pequeños donde la virtualización es mínima.
+ **Essentials**: Pequeñas empresas con hasta 25 usuarios y 50 dispositivos
+ **Hyper-V**: Contiene el núcleo del sistema operativo y el Hypervisor de Windows para la virtualización de máquinas

Datacenter y Standard ofrecen varias posibilidades:
+ Desktop experience: Con entorno gráficod e escritorio.
+ Server Core: Se ejecuta en línea de comandos sin gráfica. Es necesario cmd o powershell para interactuar con el servidor en local.
+ Nano Server: Está optimizado para trabajar en la nube, cargando en local sólo el núcleo del sistema. (No tiene sesiones locales no GPOs)

## 1.2 Licencias
Tipos de licencias:
+ Licencia OEM: Sólo se pueden adquirir al fabricante con un ordenador nuevo. Se asocian con una máquina.
+ Licencia minorista: Adquirida en tiendas o en internet, se puede mover de un equipo a otro.
+ Licencia por volumen: Esán destinadas a organizaciones para una gran cantidad de dispositivos.
  + MAK (Multiple Activation Key): Clave de Activación Múltiple. Para activar un número específico de dispositivos.
  + KMS (Key Management System): Sistema de Administración de Claves. Es necesario un Servidor KMS que da la clave a los equipos, periódicamente los equipos tienen que renovarla, si no se puede coonceder esa clave a otro equipo.

> Para saber el tipo de licencia:
> SLMGR -DLI
