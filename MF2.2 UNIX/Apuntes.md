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
| /media | Similar a /mnt. Punto de montaje de medios extraibles |
| /opt | Estático y compartible. Almacena programas que no vienen con nuestro SO y no siguen estándares para almacenar en /usr |
| /proc | Sistema de archivos virtual que proporciona info de procesos y aplicaciones por cada proceso existe un subdirectorio. Esta carpeta está en la RAM |
| /root | Variable y no compartible. Es el /home del usuario root |
| /sbin | Estático y compartible. Similar a /bin pero su contenido sólo puede ser usado por root |
| /srv | Almacena datos y directorios que usan los servidores instalados en el equipo (p.ej. ftp, servidor web...|
| /tmp | Aqui se crean y almacenan los archivos temporales. Se vacía con cada reinicio |
| /usr | Compartido y estático. Contiene la mayoría de los programas instalados en el equipo. Accesible solo de lectura para todos los usuarios |
| /var | Archivos de datos variables y temporales como logs, cache, etc. |
| /sys | Similar a /proc. Información sobre el kernel, particiones,sistemas de archivo... |
| /lost+found | Se crea después de ejecutar herramioentas para restaurar y recuperar (p.ej. ```fsch```) |

## 2. Comandos básicos
| Comando | Estructura | Explicación |
| --- | --- | --- |
| ```cal``` | ```cal [opciones][[mes]año]``` | Muesta el calendario (sin opciones, mes actual, ```-y```, año en curso) |
| ```clear``` | ```clear``` | Borra la pantalla del terminal |
| ```hostname``` | ```hostname [nombre]``` | Sin opciones devuelve el nombre de la máquina, con [nombre] cambia el nombre. (```-f``` da el FQDN, ```-d``` da el nombre del dominio) |
| ```id``` | ```id [opciones][username]``` | Muestra info del usuario (UID, GID, grupos...) |
| ```info``` | ```info [nombre]``` | Informacion sobre UNIX |
| ```man``` | ```man [opciones][seccion] nombre``` | Muestra el manual en línea |
| ```pwd``` | ```pwd``` | *Print Working Directory*. Muestra la ruta en la que nos encontramos |
| ```uname``` | ```uname [opciones]``` | Muestra info sobre la máquina y el SO |
| ```who``` | ```who [opciones] [am i]``` | Muestra informacion sobre quien está en el sistema (```am i``` muestra sobre el usuario actual) |
| ```whoami``` | ```whoami``` | Identificador del usuario actual |

## 3. Comandos del sistema de ficheros
Todos los ficheros pertenecen suempre a algún usuario que es quien controla su visibilidad para el resto de usuarios y grupos.

Los ficheros se encuentran en directorios:
+ ```.``` : Directorio actual
+ ```..``` : Directorio superior
+ ```/``` : Directorio raiz
+ ```~``` : Directorio de usuario (/home/%username%)

Existen 3 tipos de acceso a los directorios y ficheros: User, Group y Other (se explica más adelante)

Para cada uno hay 3 tipos de permiso:
+ R (Lectura)
  + Ficheros: Se puede examinar el contenido
  + Directorios: Se puede ver el contenido
+ W (Escritura)
  +  Ficheros: Se pueden modificar contenidos
  +  Directorios: Se pueden modificar contenidos
+  X (Ejecución)
  +  Ficheros: El contenido se puede emplear como comando
  +  Directorios: Se puede emplear como directorio de trabajo

El acceso es dependiente de si se puede entrar a un fichero o directorio. La denegación de escritura no protege contra el borrado.

| Comando | Estructura | Explicación |
| --- | --- | --- |
| ```cd``` | ```cd [directorio]``` | *Change Directory* Cambiar el directorio de trabajo |
| ```pwd``` | ```pwd``` | *Print Working Directory*. Muestra la ruta en la que nos encontramos |
| ```su``` | ```su [usuario]``` | *Switch User* Cambiar de usuario, si no se especifica a cual se cambiará a root |
| ```ls``` | ```ls -[opciones]``` | Lista el contenido del directorio actual (```-l```con detalles, ```-a``` muestra ocultos) |
| ```dir``` | ```dir``` | Igual que ```ls``` sin colores |
| ```vdir``` | ```vdir``` | Igual que ```ls -l``` |
| ```chmod``` | ```chmod XXX [archivo]``` | Las X serán los números que en binario indicarán los permisos :eyes: [CHMOD UNIX](https://ayudalinux.com/comando-chmod-que-es-como-usarlo/#:~:text=Comando%20chmod%3A%20%C2%BFQu%C3%A9%20es%3F%20y%20%C2%BFC%C3%B3mo%20usarlo%3F%201,Cambia%20la%20propiedad%20de%20archivos%20o%20directorios.%20) (*hay más formas de usarlo... a mi me gusta esta*) |
| ```chown``` | ```chown [user[:group]] [filename]``` | Cambia el propietario de un archivo (sólo el propietario original y/o root pueden hacerlo) |
| ```chgrp``` | ```chgrp [group] [filename]``` | Cambia el grupo de un fichero (sólo el propietario original y/o root pueden hacerlo) |
| ```mkdir``` | ```mkdir [opciones] [-m modo] directorio``` | Crea un directorio |
| ```nano``` | ```nano [archivo]``` | Editor de textos por shell |
| ```rmdir``` | ```rmdir [opciones] directorio``` | Elimina directorios vacíos (```-p``` elimina directorios padre si quedan vacíos)|
| ```mv``` | ```mv [opciones] arch_origen arch_destino``` | Cambia el nombre de un archivo |
| ```rm``` | ```rm [opciones] nombre``` | Elimina archivos (```-r``` elimina directorios y contenido) |
| ```ln``` | ```ln [opciones] origen destino``` | Crear enlaces (duros si es sin opciones, blandos si es con ```-s```) (ver más adelante) |

#### ```ln```
Existen dos tipos de enlaces:
+ Enlace duro: crea un nuevo archivo que apunta a la dirección de memoria (borrar el archivo original ya no afectaría al archivo porque hay otro enlace, habría que borrar TODOS los enlaces duros para borrar el archivo :eyes: [Consultar info sobre los Inodos](https://es.wikipedia.org/wiki/Inodo))
+ Enlace blando: Apunta al archivo original, no es un nuevo archivo, si se borra el original se rompe el enlace

**Enlace duro**: ```ln [origen] [destino]```

**Enlace blando**: ```ln -s [origen] [destino]```

El destino es opcional, si no se introduce el enlace se creará en la unicación actual en la que se está.

## 4. Administración de usuarios

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

#### ```passwd```
Se utiliza para moodificar la contraseña de un usuario.

```passwd [username]```

## 5. Editor de textos "VI"
Editor de textos en todas las versiones de UNIX y accesible desde cualquier terminal.

```vi [nombre_archivo]```

El editor VI cuenta con 3 modos:
+ Modo comando: Las teclas ejecutan acciones (es el modo inicial)
+ Modo texto (o modo inserción): Las teclas ingresan el caracter que representan
+ Modo última línea (o modo ex): Las teclas se usan para escribir comandos en la última línea
