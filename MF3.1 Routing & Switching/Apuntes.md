# Routing & Switching

>[!TIP]
>:spiral_notepad:[Archivos de configuración César](https://github.com/13sauca13/PRG/tree/master/MF3.1%20Routing%20%26%20Switching/TXT_Cesar)

## Routers
![Conexiones del router](https://github.com/13sauca13/PRG/blob/master/Recursos/Conexiones%20del%20router.PNG)

Los routers son ordenadores, y como tal necesitan:
+ CPU
+ Memoria
+ Sistema operativo

Con respecto a las memorias, los routers tienen 4 memorias:
+ RAM
+ NVRAM
+ Flash
+ ROM

![Memorias router](https://github.com/13sauca13/PRG/blob/master/Recursos/Memorias%20Router.PNG)

### Proceso de arranque del router
![Arranque router](https://github.com/13sauca13/PRG/blob/master/Recursos/Arranque%20router.PNG)

## Configuración del sistema operativo
Existen 3 formas de acceder a un router:
+ Puerto de consola
+ SSH
+ Telnet

Independientemente del método de acceso es necesario un programa de emulación de terminal.

Los comandos una vez hayamos accedido tienen una estructura jerárquica:
1. Modo exec del usuario:
```
ROUTER>
```
2. Modo exec con privilegios:
```
ROUTER> enable
ROUTER#
```
3. Modo configuración global: Desde este modo se puede acceder a la configuración específica de cada linea o interfaz
```
ROUTER# configure terminal
ROUTER(config)#
```

![Estructura comandos IOS](https://github.com/13sauca13/PRG/blob/master/Recursos/Estructura%20comandos%20IOS.PNG)

## Configuración básica de dispositivos
El primer paso cuando se configura un dispositivo es asignarle un nombre de host. Estos nombres aparecen el las peticiones de entrada de la CLI y se usan en los diagramas de la topología.
```
ROUTER> enable
ROUTER# configure terminal
ROUTER (config)# hostname Router-1
Router-1 (config)#
```

Es necesario limitar el acceso físico a los dispositivos y usar contraseñas seguras.

Para proteger el acceso exec con privilegios se utilizan los siguientes comandos:
```
Router-1(config)# enable password <CONTRASEÑA> //esta contraseña está en claro
Router-1(config)# enable secret <CONTRASEÑA> //esta contraseña está cifrada
```
Para configurar una línea con contraseña se usan los siguientes comandos:
```
Router-1(config)# line <linea> //puede se console, vty (de la 0 a la 15)...
Router-1(config-line)# password <CONTRASEÑA>
Router-1(config-line)# login
```

Los archivos **startup-config** y **running-config** muestran la mayor parte de las contraseñas en texto plano. Esto es un problema de seguridad.

Para cifrar todas las contraseñas usaremos:
```
service password-encryption
```

Para borrar todas las configuraciones de un router:
```
Router-1# erase startup-config
Router-1# reload
```

En el caso de los switches es necesario usar el interfaz virtual del switch (SVI) para poder conectarse de manera remota. Es recomendable crear una VLAN de administracion y no usar la VLAN1.

El SVI debe configurarse con lo siguiente:
+ Direccion IP
+ Mascara de subred
+ Estado habilitada

## Configuración de VLANs
Las redes VLAN permiten que el administrador segmente redes, sin tener en cuenta la ubicación física del usuario o del dispositivo.

***Las redes VLAN se aíslan mutuamente, y sólo a través de un router se pueden comunicar entre ellas.***

Para ver las vlan de un switch se usa el comando:
```
S1# show vlan brief
```

Un enlace troncal de vlan es un enlace punto a punto que transporta datos de más de una red vlan. Generalmente, se establece entre switches para que los dispositivos de una misma red vlan se puedan comunicar, incluso si están conectados físicamente a switches diferentes.

Un enlace troncal de vlan no está asociado a ninguna red vlan.

## Configuracion VTY
Las líneas VTY se tratan de un conjunto de puertos virtuales utilizados para la conexión vía telnet, SSH, http o https al dispositivo para realizar administración en línea.
La mayoría de los dispositivos tienen al menos 5 puertos virtuales identificados como VTY 0 a 4. Sin embargo, en la medida en que resulte necesario, se pueden general más puertos virtuales hasta completar un total de 21 líneas vty.

>[!WARNING]
>Telnet no es seguro porque todo el tráfico viaja en claro (incluída la contraseña al abrir la conexión)
>
>NO USEIS TELNET!! El niño Jesús se pone triste

### Telnet
Para configurar telnet basta con "habilitar" las líneas VTY y darles suario y contraseña. En este caso creamos usuario y contraseña para el router en si y luego le decimos a las líneas VTY que utilicen el login del router:
```
R1(config)# username <nombre_usuario> privilege <privilegios_del_1_al_15> password <contraseña>
!OJO: Esta contraseña está en claro... (secret... service password encryption...)
R1(config)# line vty 0 4
R1(config-line)# login local
R1(config)#
```
Para hacerlo con una contraseña específica para la conexión en lugar de usuario y contraseña:
```
R1(config)# line vty 0 4
R1(config-line)# password <contraseña>
R1(config-line)# login
R1(config)#
```

### SSH
La conexión por SSH cifra los datos. Es como telnet pero seguro.

Podemos igual que con telnet utilizar usuario y contraseña del router o crear una contraseña específica para esa conexión. (El ```hostname``` no puede ser el por defecto!!)

```
R1(config)# ip domain-name <lo_que_sea> !Es necesario definir un nombre de dominio
R1(config)# line vty 0 4
R1(config-line)# transport input ssh
R1(config-line)# login
!Si vamos a usar user y pass será login local, si creamos password para vty será sólo login (ver la parte de telnet)
```
Una vez configurada la línea hay que crear las claves que van a cifrar la conexión:
```
R1(config)# crypto key generate rsa
!Sale el siguiente aviso para introducir la longitud de las claves
!(si pulsamos enter aplica el valor entre corchetes, si no introducimos la longitud deseada)
How many bits in the modulus [512]:
```

Para deshabilitar el ssh hay que borrar las claves y quitar el ```transport input ssh``` de las vty:
```
R1(config)# crypto key zeroize rsa
```

>[!TIP]
>Conviene usar la versión 2 de ssh por ser más segura, pero necesitamos que la clave RSA que generamos sea de al menos 768
>Se haría al terminar de configurar SSH y añadiendo:
>```
>R1(config)# ip ssh version 2
>```

#### SSH en switches
En el caso de un switch también podemos usar SSH pero será necesario crear un SVI (Switch Virtual Interface), que es una interfaz virtual (Porque los switches trabajan en capa 2) para conectar y enrutar tráfico en una VLAN. En este caso el SVI tambié nos vale para poder hacer la conexión.

Configuraríamos todo igual que en el router y además:
```
S1(config)# interface vlan <nº_vlan>
S1(config)# ip address <ip> <mascara>
```
Así podríamos hacer SSH desde cualquier PC de la VLAN X usando la IP que acabamos de configurar.

Si a mayortes queremos hacer la conexión desde otra VLAN haría falta un router (como para cualquier tipo de tráfico entre VLANs) tendríamos que darle al switch una puerta de enlace para responder a la subinterfaz del router correspondiente a la VLAN del SVI (si no el tráfico llega a la SVI pero el switch no sabe a quien responderle):
```
S1(config)# ip default-gateway <ip_subinterfaz_router> <mascara>
```

## Configuración DHCP
El protocolo DHCP (Protocolo de configuración dinámica de host) o también conocido como «Dynamic Host Configuration Protocol«, es un protocolo de red que utiliza una arquitectura cliente-servidor. Este protocolo se encarga de asignar de manera dinámica y automática una dirección IP, la puerta de enlace y el servidor DNS.
```
R1(config)# ip dhcp excluded-address <direccion o rango excluidas>
R1(config)# ip dhcp pool <nombre>
R1(dhcp-config)# network <ip> <mascara>
R1(dhcp-config)# default-router <puerta de enlace>
R1(dhcp-config)# dns-server <servidor DNS>
```
