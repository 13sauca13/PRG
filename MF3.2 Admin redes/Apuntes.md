# Administracion de redes

>[!TIP]
>:computer: [Scripts de los laboratorios](https://github.com/13sauca13/PRG/tree/master/MF3.2%20Admin%20redes/Scripts%20laboratorios)

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


### Particiones de Windows
#### MBR
+ Existe desde DOS
+ Soporta particiones de hasta 2Tb y permite hasta 4 particiones (3 primarias + 1 extendida y la extendida puede tener infinitas unidades lógicas)
+ Cada partición puede contener un sistema operativo booteable

#### GPT (GUID Partition Table)
+ Soporta hasta 18Eb (18 mil millones de Gb)
+ Hasta 128 particiones por disco
+ Almacena un duplicado de las tablas de particiones

### Tipos de discos
+ **Discos básicos**: Contiene las particiones primarias, particiones extendidas y las unidades lógicas (es la configuración al inicializar un disco duro en el ordenador, sea MBR o GPT)
+ **Discos dinámicos**: Tienes una sola partición (LDM), no permite particiones extendidas y hay una a mayores, oculta, al final del disco para la base de datos (Logical Disk Manager, LDM). Se pueden crear hasta 2000 volúmenes y puede compartir datos entre varios discos dinámicos. Permite crear 5 tipos de volúmenes:
  + Simple: Un espacio en un disco
  + Distribuido:  Combinar varios espacios de varios discos en un solo volumen lógico
  + RAID 0 (Volumen seleccionado)
  + RAID 1 (Volumen reflejado)
  + RAID 5: Requiere mínimo 3 discos

## 1.6 Directorio activo
El Active Directory Domain Services (AD DS) es el nombre que .recibe el conjunto de elementos que globalmente constituyen el servicio directorio en dominios Windows.
Utiliza los siguientes protocolos:
+ **SNTP** Simple Network Time Protocol: Permite disponer de un servicio de sincronización de tiempo entre sistemas conectados por red.
+ **LDAP** Lightweight Access Protocol: Protocolo mediante el cual las aplicaciones acceden para leer o modificar la información existente en la base de datos del directorio.
+ **Kerberos**: Protocolo utilizado para la autenticación de usuarios y máquinas.
+ **Certificados X.509**: Estándar que permite distribuir información a través de la red de una forma segura.

### DNS
Cada dominio va a ser un espacio de nombres. DNS es el sistema de nombres para redes basadas en el protocolo TCP/IP y además, es el servicio de nombres que se usa para localizar computadores en Internet.

El Directorio Activo utiliza DNS para tres funciones principales:
+ Resolición de nombres
+ Definición del espacio de nombres
+ Búsqueda de los componentes físicos de AD

### Dominio
El dominio es la unidad principal de la estructura lógica del Directorio Activo, es un conjunto de ordenadores, o equipos, que comparten una base de datos de directorio común. El uso de dominios permite conseguir los siguientes objetivos:
+ Delimitar la seguridad: Un dominio Windows Server define un límite de seguridad. Aunque en una organización pueden existir múltiples dominios interrelacionados, cada uno presenta una configuración de seguridad 
independiente.
+ Replicar informacion: Active Directory utiliza un modelo de replicación multimaestro, lo cual significa que cualquier DC admite cambios en la información de su partición, y es capaz de replicarlos luego al resto de DCs que constituyen su unidad de replicación.
+ Aplicar Politicas (o Directivas) de Grupo: 
+ Delegar permisos administrativos

### Autenticación y autorización
Directorio activo se encarga de proporcionar autenticación y autorización a los clientes (tanto equipos como usuarios y aplicaciones).

El proceso de ***autenticación*** es el proceso de verificar la identidad de un usuario en la red, tanto para el acceso al equipo local como el acceso a los recursos de la red.

El proceso de ***autorización*** es la verificación de que el solicitante tiene permisos de acceso a los recursos que está solicitando.

### Múltiples dominios en la misma organización
Un árbol es un conjunto de uno o más dominios dentro de un bosque que comparten un espacio de nombres contiguo, es decir, comparten un sufijo de DNS común.

Los dominios que forman un árbol se vinculan mediante relaciones de confianza bidireccional y transitiva. La relación padre-hijo entre dominios en un árbol de dominio es simplemente una relación de confianza.

Un bosque se define como un grupo de árboles que no comparten un espacio de nombres contiguo, y que se conectan mediante relaciones de confianza bidireccional y transitiva.

![Multiples dominios](https://github.com/13sauca13/PRG/blob/master/Recursos/Multiples%20dominios.PNG)

Sin embargo, los dominios siguen siendo independientes entre sí: los administradores de un dominio padre no son automáticamente administradores del dominio hijo y el conjunto de políticas de un dominio padre no se aplican automáticamente a los dominios hijo.

##### Relaciones de confianza entre dominios
Una relación de confianza es una relación establecida entre dos dominios de forma que permite a los usuarios de un dominio ser reconocidos por los Controladores de Dominio de otro dominio. Windows Server soporta varios tipos de relaciones de confianza.

***Sitios***: Se trata de una o más subredes IP que están conectadas y típicamente definidas por un área geográfica.

### Controladores de dominio
Un controlador de dominio es un servidor Windows que guarda y replica una cuenta, la información de seguridad del dominio y define los límites de este.

Después de que haya promovido una computadora en el controlador de dominio, debe utilizar varios complementos de las consolas MMC para manejar el Directorio activo. Estas consolas son las siguientes:
+ **Active Directory Users and Computers**
+ **Active Directory Domains and Trusts**
+ **Active Directory Sites and Services**
+ **Active Directory Administrative Center**
+ **Group Policy Management Console (GPMC)**

Aunque estas herramientas son instaladas en controladores de dominio, también pueden instalarse en equipos clientes para que pueda administrar Directorio activo.

********************************** AÑADIR

## 1.7 Resolución de nombres
Se trata del proceso de traducción de nombres a IP, siendo el protocolo más utilizado el Domain Name System (DNS).

En C:\Windows\System32\drivers\etc es la ubicación en la que se encuentran los archivos:
+ hosts: Contiene lista de los nombres e IP ya traducidos
+ lmhosts: igual que hosts pero con equipos de la red local

#### DNS
Es un sistema jerárquico. Los dominios de primer nivel son .com, .es, .org, dominios de países... El segundo nivel de nombres es el que puede ser registrado por distribuidores autorizados.

Las empresas grandes puedes subdividir si espacio DNS en subdominios.

**FQDN** (Fully Qualified Domain Name): Describe la posición exacta de un host en una jerarquía DNS. (p.ej. technet.microsoft.com)

Registro de recursos (RR) dentro de la zona DNS:
+ SOA (Start Of Authority) ************************************ AÑADIR TODOS
+ NS (Name Server)
+ A (Host Address): En IPv4
+ AAAA (Host Address): En IPv6
+ PTR (PoinTeR)
+ CNAME (Canonical Name)
+ MX (Mail Exchanger)
+ SRV (Service)

Existen tres zonas de búsqueda en los DNS: ********************************* AÑADIR
+ Zona de búsqueda directa para traducir nombres a IP
+ Zona inversa para traducir IP a nombres.
+ Sugerencias raiz (Root Hint)

El método para compartir y distribuir cargas dentro de los DNS es Round Robin
