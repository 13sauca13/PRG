# Routing & Switching

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
