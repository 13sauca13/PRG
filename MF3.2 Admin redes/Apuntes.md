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
![Instalación de Windows](https://github.com/13sauca13/PRG/blob/master/Recursos/Instalcion%20Windows.png)

#### WDS y SYSPREP
+ WDS (Windows Deployement Service): Herramienta software que permite la instalación de sistemas operativos a través de red (Equipos con tarjeta PXE). El problema es que todos los equipos tendrán el mismo nombre y el mismo SID, la solución es ejecutar el SYSPREP.

## 1.4 Características de seguridad de Windows
+ **Control de cuentas de usuario (UAC)**
  + Funcion que ayuda a prevenir cambios sin autorización en el equipo.
  + Si se inicia como Administrador pide permiso
  + Si se inicia como usuario solicita la contraseña de Administrador. (los usuarios pueden instalar actualizaciones, controladores de windows update, ver las configuraciones, conectar bluetooth...)
+ **Opciones de red**
  + Detección de redes activa
    + Permite ver otras redes y dispositivos y será visible por los demás
    + Permite compartir archivos, carpetas e impresoras
  + Tipos de red
    + Dominio
    + Trabajo
    + Pública
> Para cambiar el perfil de red:
> 
> ```Get-NetConnectionProfile``` Permite ver el tipo de conexión
> 
> ```Set-NetConnectionProfile``` Modifica el tipo de conexión

  + Firewall de Windows
    + La configuración del Firewall se puede hacer en local (desde Panel de Control o desde MMC), en remoto o mediante GPO
    + Ahora está integrado en la configuracion del Ipsec (Internet Protocol Security)
    + Modos del Firewall
      + Modo Transporte: Sólo se cifra la carga útil (no modifica la cabexera IP, sólo funciona de PC a PC, no atraviesa NAT)
      + Modo túnel: Todo el paquete IP es crifrado y autenticado (se emplea para comunicaciones de Red a Red o PC a PC sobre internet (VPN))
     
## 1.5 Almacenamiento

#### Canal de fibra (FC)
Usa un protocolo de canal de fibra (FCP) que permite comandos SCSI. Su topología de red se denomina ***fabric*** (los dispositivos están conectados entre si por una o más rutas de datos (utilizando conmutadores)). Topologías de conexión:
+ Point to point (P2P-FC): Los dispositivos están conectados uno a otro
+ Arbitrated loop (FC-AL): Todos los dispositivos están conectados a un anillo
+ Switched fabric (FC-SW): Todos los dispositivos están conectados a conmutadres de canal de fibra. Los conmutadores administran el estado de los fabric para optimizar (los medios de comunicación no se comparten, cualquier dispositivo que se comunica con otro lo hace a la velocidad del bus completo

Cada dispositivo incluido en el controlador de hosts de bus se le llama nodo. Al igual que una MAC address 
utilizada en tarjetas de interfaz de red, cada nodo tiene un arreglo de 64 bits de nombre a nivel mundial 
(WWNN: World Wide Node Name) asignado por el fabricante y registrado en la IEEE.

Para hacer más manejable el almacenamiento, el canal de fibra utiliza zonificación y zonificación LUN.
+ Zona: Indica que equipos pueden conectasrse entre si
+ Alias: Nombre asociado a un WWNN o puerto
+ Zoneset: Conjunto de zonas, pueden existir varios definidos, pero sólo uno activo (el zoneset activo es el que está en uso y es el mismo para todos los switches del fabric)

#### iSCSI
Internet Small Computing Interface, es un protocolo de internet para el almacenamiento en red basado en IP. Debe usar un adaptador de red dedicado.

En almacenamiento, una ***Logical Unit Number o LUN*** es una dirección para una unidad de disco duro y por extensión, el disco en sí mismo. Normalmente se refiere a una partición virtual (o volumen) dentro de un conjunto RAID. , iSCSI emula una sesión de un disco duro para que el servidor LUN lo trate como cualquier otro.

iSCSI utiliza la siguiente información para conetarse a la SAN:
+ Nombre del host (o dirección IP)
+ Número de puerto (por defecto 3260)
+ Nombre iSCSI
  + Nombre calificado iSCSI (IQN)
  + Identificador único extendido (EUI)
  + T11 Autoridad de direcciones de red (NAA)
+ Contraseña opcional

Para abrir el Iniciador iSCSI se hará desde "Herramientas" dentro de "Administración del servidor" o en ```services.msc```

El iSCSI también se puede administrar por línea de comandos lanzando el iniciador con: ```iscsicli```
