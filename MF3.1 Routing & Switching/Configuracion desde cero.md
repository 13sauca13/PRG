# Configuración desde cero

**Índice:**
1. Routers: config básica y securización
  2.  Lineas VTY
      + Telnet
      + SSH
       

# Routers
El primer paso cuando se configura un dispositivo es asignarle un nombre de host. Estos nombres aparecen el las peticiones de entrada de la CLI y se usan en los diagramas de la topología (también aplica a switches)
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

Para ver SSH en switches mirar más adelante en la seccion de switches.

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

## Configuración DHCP
El protocolo DHCP (Protocolo de configuración dinámica de host) o también conocido como «Dynamic Host Configuration Protocol«, es un protocolo de red que utiliza una arquitectura cliente-servidor. Este protocolo se encarga de asignar de manera dinámica y automática una dirección IP, la puerta de enlace y el servidor DNS.
```
R1(config)# ip dhcp excluded-address <direccion o rango excluidas>
R1(config)# ip dhcp pool <nombre>
R1(dhcp-config)# network <ip> <mascara>
R1(dhcp-config)# default-router <puerta de enlace>
R1(dhcp-config)# dns-server <servidor DNS>
```

## Enrutamiento estático
Un router puede descubrir redes remotas de dos manera:
+ Manuelmente: Se introducen de forma manual por medio de rutas estáticas
+ Automáticamente: La rutas se descubren de forma dinámica mediante protocolos de routing dinámico

Las rutas estáticas no se anuncian en la red aumentando la seguridad, consumen menos ancho de banda que el routing dinámico porque no se calculan ni comunican las rutas.
```
R1(config)# ip route <red_destino> <mascara_destino> <ip_siguiente_salto>
```
En lugar de usar la ```ip_siguiente_salto``` puede utilizarse tambien el interfaz de salida (p.ej Fe0/1...)

Para enrutar TODO hacia algún lugar se puede utilizar la ruta ***Quad Zero*** o ruta sumarizada:
```
R1(config)# ip route 0.0.0.0 0.0.0.0 <ip_siguiente_salto>
```
Esto enviará todo el tráfico vaya a donde vaya (salvo que sea a otra ruta estática ya configurada) hacia donde se indique (ip o interfaz).

## Enrutamiento dinámico
Son protocolos de mensajes y algoritmos que se usan para intercambiar información, compartir y completar las tablas de enrutamiento automáticamente para descibrimiento y elección de los mejores caminos.

Para configurar los enrutamientos dinámicos tenemos que "publicar" las redes desde el router **empezando por la que une a los routers entre ellos para que se hagan "vecinos"**
### RIPv2
En el apartado de ```network``` hay que ir poniendo cada red que el router tiene conectada, es la información que le va a mandar a los demás routers de la red (como una especie de: *Eh! Que yo tengo estas redes conectadas a mi, si necesitais mandarles algo soy vuestro hombre*).

La interfaz pasiva es aquella por la cual no se manda info de las tablas de enrutamiento, para la red de ordenadores p.ej...
```
R1(config)# router rip
R1(config-router)# version 2
R1(config-router)# no auto-sumary //Importante para que no se les asigne clase a las redes
R1(config-router)# network <direccion_red>
R1(config-router)# network ...
R1(config-router)# ...
R1(config-router)# passive-interface <interfaz>
```
Si el router tiene rutas sumarizadas (Quad Zero) hay que añadir un paso a la configuración para que publique esta ruta por defecto a los demás routers:
```
R1(config-router)# default information originate
```
>[!WARNING]
>Ojo al usar el comando anterior!! Le diremos a todos los routers que cuando no sepan a donde mandar algo nos lo manden a este router!!
>
>Asegurarse de que es el router que debe gestionar todo con el exterior (p.ej el router ISP)

### OSPF
El ```<numero>``` de OSPF tiene que ser el mismo en todos los routers, el área también debe ser la misma para todos los routers que queremos que compartan info (podemos poner varias áreas en un router) y de nuevo tenemos que incluir todas las redes que tenemos conectadas:
```
R1(config)# router ospf <numero>
R1(config-router)# network <direccion_red> <wildcard> area <num_area>
R1(config-router)# network ...
```
La interfaz pasiva se haría:
```
R1(config)# router ospf <numero>
R1(config-router)# passive-interface <interfaz>
```
Podemos redistribuir las rutas estáticas que tengamos configuradas:
```
R1(config-router)# redistribute static
```
Y tambien podemos redistribuir las sumarizadas igual que en RIPv2:
```
R1(config-router)# default information originate
```

### EIGRP
El ```<numero>``` de EIGRP tiene que ser el mismo en todos los routers que van a compartir informacion:
```
R1(config)# router eigrp <numero>
R1(config-router)# network <direccion_red> <wildcard>
R1(config-router)# network ...
```
Las interfaces pasivas, el ```no auto-sumary```, la redistribucion de rutas estáticas y de las sumarizadas son igual que en los otros protocolos.

# Switches
También conviene cambiarles el nombre y securizarlos igual que se haría con un router.
## SSH en switches
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
## Securizar interfaces switch
```
S1(config)# interface <interfaz>
S1(config-if)# switchport port-security //Así activamos la seguridad, para quitarla basta con hacerle "no" a esta línea, no a todas
S1(config-if)# switchport port-security mac-address <mac> //también podemos poner "sticky" en lugar de la mac para que la aprenda el switch al enchufarle algo
S1(config-if)# switchport port-security maximum <max_macs_sticky>
S1(config-if)# switchport port-security violation <protect/restrict/shutdown>
```
## Configuración de VLANs
Las redes VLAN permiten que el administrador segmente redes, sin tener en cuenta la ubicación física del usuario o del dispositivo.

***Las redes VLAN se aíslan mutuamente, y sólo a través de un router se pueden comunicar entre ellas.***

Para ver las vlan de un switch se usa el comando:
```
S1# show vlan brief
```

Un enlace troncal de vlan es un enlace punto a punto que transporta datos de más de una red vlan. Generalmente, se establece entre switches para que los dispositivos de una misma red vlan se puedan comunicar, incluso si están conectados físicamente a switches diferentes.

Un enlace troncal de vlan no está asociado a ninguna red vlan.

```
S1(config)# vlan <numero>
S1(config-vlan)# name <nombre>
```
Ya estaría creada y nombrada, hay que añadir los interfaces que la integran:
```
S1(config)# interface <interfaz> //tambien se puede usar: rage <rango_interfaces>
S1(config-if)# switchport mode <access/trunk>
S1(config-if)# switchport access vlan <numero_vlan>
```

### Enrutar entre VLANs
**Esta configuración se realiza en el router!**
Hay que configurar la interfaz del router a la que está conectada el switch y quitarle la ip:
```
R1(config)# interface <interfaz>
R1(config-if)# no ip address <ip_interfaz> <máscara>
```
Ahora hay que crear una subinterfaz para cada vlan (usamos el numero de vlan como numero de subinterfaz):
```
R1(config)# interface <interfaz>.<vlan> //OJO!! hay un punto en medio (ej. f0/1.10)
R1(config-subif)# encapsulation dot1q <num_vlan>
R1(config-subif)# ip address <ip> <mascara>
```
>[!TIP]
>La ip y máscara del subinterfaz tienen que ser del rango de la VLAN (preferiblemente la 1ª IP del rango)


