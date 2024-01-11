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

> El comando para consultar el tipo de licencia:
> 
> ```slmgr -dli```

## 1.3 Instalación
El método más habitual es con un fichero ISO.

Proceso de instalación:
1. La BIOS reconoce el dispositivo de arranque y lanza el O.S. que encuentra en él.
2. En la carpeta /Sources:
   + Boot.wim: Contiene el Windows PE y configurará idioma, drivers y discos y las rutas de los drivers no incluidos en este fichero.
   + Install.wim o Install.esd (según el O.S. vendrá un archivo u otro): Contiene el sistema de ficheros del propio O.S.
3. OOBE (Out Of Box Experience): Experiencia rápida que se ejecuta la primera vez que un usuario inicia un equipo.
   + Nombre del PC
   + Nombre del primer usuario y contraseña (este será el Admin)
   + Configuración de red
   + Instalación de actualizaciones
   + Cortana y privacidad
   + ***En un servidor sólo se pedirá la contraseña de Admin***
![Instalación de Windows](Recursos/Instalcion Windows.png)

#### WDS y SYSPREP
+ WDS (Windows Deployement Service): Herramienta software que permite la instalación de sistemas operativos a través de red (Equipos con tarjeta PXE). El problema es que todos los equipos tendrán el mismo nombre y el mismo SID, la solución es ejecutar el SYSPREP.
