# UNIX
## 1. Estructura de directorios en Linux
El estándar de jerarquía del sistema de archivos, también conocido como FHS (File Hierarchy System), es la norma que define los directorios y sus contenidos en los sistemas Unix.
Proporciona una serie de ventajas:
+ El software sae en todo momento las carpetas y permisos del ordenador
+ Los usuarios conocen en todo momento el contenido de las carpetas
+ Ayuda a la hora de realizar mantenimiento en el ordenador
+ Ayuda a otorgar permisos a las diferentes carpetas

El FHS es flexible y existe cierta libertad para aplicar sus normas.
Existen varios tipos de tipos de directorios:
+ Compartibles: pueden ser compartidos dentre distintos equipos
+ No compartibles: No se pueden compartir y sus uso y modificación están limitados al administrador del sistema
+ Variables: Contienen archivos que pueden ser modificados
+ No variables: Contienen archivos que solo pueden ser modificados con ayuda del administrador del sistema

Partiendo del directorio raíz ```/``` están todas las carpetas y estructura del sistema operativo:

| Carpeta | Descripción |
| --- | --- |
| /bin | Estático y compartido, contiene archivos binarios ejecutables necesarios para el funcionamiento del SO. Estos archivos los pueden usar todos los usuarios. NO PUEDE CONTENER SUBDIRECTORIOS |
| /boot | Estático y no compartible, contiene todos los archivos necesarios para el arranque del ordenador excepto los archivos de configuración |
| /dev | Aqui estarán los dispositivos, a los que unix trata como un archivo |
| /etc | Directorio estatico con archivos de configuración del sistema operativo y diversos programas |
| /home | Variable y compartible donde se encuentran los ficheros de todos los usuarios salvo root. Cada usuario tendrá su carpeta en /home |
| /lib | Estático y compartible. Contiene bibliotecas necesarias para ejecutar los ejecutables de /bin y /sbin. Tambien contiene módulos kernel y controladores necesarios durante el arranque y funcionamiento del SO |
| /mnt | Alberga los puntos de montaje de los diferentes dispositivos |
| /opt |  |
| /proc | |
| /root | |
| /sbin | |
| /tmp | |
| /usr | |
| /var | |

## Administración de usuarios y grupos
| Comando | Uso |
| --- | --- |
| ```useradd -g [grupo] -m [username]``` | Creación de usuarios *(el -m crea el directorio del usuario en la carpeta /home)*|
| ```usermod``` | Modificación de usuarios *(el parámetro ```-r``` elimina también la carpeta de /home del usuario)* |
| ```userdel``` | Eliminación de usuarios |
| ```groupadd``` | Creación de grupos |
| ```groupmod -n [new_name] [old_name]``` | Modificación de grupos |
| ```groupdel``` | Eliminación de grupos |
| ```adduser [username] [groupname]``` | Añadir usuarios a un grupo (también sirve para crear usuarios) |
| ```deluser [username] [groupname]``` | Eliminar usuarios de un grupo |

## ```passwd```
Se utiliza para moodificar la contraseña de un usuario.

```passwd [username]```

## ```ln```
Existen dos tipos de enlaces:
+ Enlace duro: crea un nuevo archivo que apunta a la dirección de memoria (borrar el archivo original ya no afectaría al archivo porque hay otro enlace, habría que borrar TODOS los enlaces duros para borrar el archivo :eyes: [Consultar info sobre los Inodos](https://es.wikipedia.org/wiki/Inodo))
+ Enlace blando: Apunta al archivo original, no es un nuevo archivo, si se borra el original se rompe el enlace

**Enlace duro**: ```ln [origen] [destino]```

**Enlace blando**: ```ln -s [origen] [destino]```

El destino es opcional, si no se introduce el enlace se creará en la unicación actual en la que se está.

## ```chmod```
Modifica los permisos de un archivo o directorio.

Los permisos se representan con 9 letras. Son 3 grupos de tres:
+ 3 primeras: Permisos para propietario
+ 3 centrales: Permisos para el grupo
+ 3 últimas: Permisos para el resto

Las letras indican el permiso concedido (r=read, w=write, x=execute) y están en ese orden: ```rwxrwxtwx```

Uno de los modos de modificar los permisos es usando un número (de 0 a 7) por cada trío de letras, que al pasar a binario se convertiría en 3 ceros y/o unos, indicando el 1 que ese permiso se concede y el 0 que no.
```
chmod XXX [archivo]
```
