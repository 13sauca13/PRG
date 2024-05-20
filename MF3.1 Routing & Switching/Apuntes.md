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
