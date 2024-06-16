# Configuración desde cero
## 1. Configuración iniciar router
### Cambio de nombre:
´´´
ROUTER> enable
ROUTER# configure terminal
ROUTER (config)# hostname Router-1
Router-1 (config)#
´´´
### Securización:
```
Router-1(config)# enable password <CONTRASEÑA> //esta contraseña está en claro
Router-1(config)# enable secret <CONTRASEÑA> //esta contraseña está cifrada
```
