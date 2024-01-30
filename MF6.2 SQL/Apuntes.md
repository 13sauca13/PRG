# SQL

##### Lenguaje DDL
Se usa para crear y definir nuevas bases de  datos
+ ```create```: crear tablas
+ ```alter```: modificar tablas
+ ```drop```: borrar tablas
+ ```truncate```: borrar tablas

##### Lenguaje DML
Utilizado para generar consultas para ordenar, filtrar y extraer datos de la base de datos.
+ ```select```: consultar datos
+ ```insert```: introducir datos
+ ```update```: modificar datos
+ ```delete```: borrar datos

##### Lenguaje DCL
Seguridad de la base de datos, en todo lo referente al control de accesos y privilegios entre los usuarios.
+ ```revoke```: quitar permisos
+ ```grant```: dar permisos

##### Lenguaje TCL (Lenguaje de Control de Transacciones)
+ ```commit```: guardar cambios
+ ```rollback```: volver a un estado consistente anterior
+ ```savepoint```: crear un punto de recuperación


#### Bases de datos del sistema
![Bases de datos del sistema](https://github.com/13sauca13/PRG/blob/master/Recursos/Bases%20de%20datos%20del%20sistema.PNG)

+ **master**: guarda todos los permisos e inicios de sesión
+ **model**: Cada vez que toco una tabla se crea una copia de esa tabla aqui
+ **msdb**: aqui se guarda la programación de copias de seguridad
+ **tempdb**: aqui se guardan las tablas temporales, cada vez que se hace una transacción se crea tabla. Existen sólo dos tablas:
  + **inserted**
  + **deleted**

Sólo los usuarios con rol sysadmin (normalmente será sólo uno, "sa") pueden crear usuarios

>Crear un usuario:
>```
>create login username
>wiht password='contraseña'[must_changed],
>default_database=[database],
>check_expiration=on,
>check_policy=on;
>```
