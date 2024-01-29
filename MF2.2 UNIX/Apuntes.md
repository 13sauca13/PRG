# UNIX

#### Administración de usuarios y grupos
| Comando | Uso |
| --- | --- |
| ```useradd -g [grupo] -m [username]``` | Creación de usuarios *(el -m crea el directorio del usuario en la carpeta /home)*|
| ```usermod``` | Modificación de usuarios *(el parámetro ```-r``` elimina también la carpeta de /home del usuario)* |
| ```userdel``` | Eliminación de usuarios |
| ```groupadd``` | Creación de grupos |
| ```groupmod -n [new_name] [old_name]``` | Modificación de grupos |
| ```groupdel``` | Eliminación de grupos |
| ```adduser [username] [groupname]``` | Añadir usuarios a un grupo |
| ```deluser [username] [groupname]``` | Eliminar usuarios de un grupo |

#### ```passwd```
Se utiliza para moodificar la contraseña de un usuario.

```passwd [username]```

#### ```ln```
Existen dos tipos de enlaces:
+ Enlace duro: crea un nuevo archivo que apunta a la dirección de memoria (borrar el archivo original ya no afectaría al archivo porque hay otro enlace, habría que borrar TODOS los enlaces duros para borrar el archivo :eyes: [Consultar info sobre los Inodos](https://es.wikipedia.org/wiki/Inodo))
+ Enlace blando: Apunta al archivo original, no es un nuevo archivo, si se borra el original se rompe el enlace

**Enlace duro**: ```ln [origen] [destino]```

**Enlace blando**: ```ln -s [origen] [destino]```

El destino es opcional, si no se introduce el enlace se creará en la unicación actual en la que se está.
