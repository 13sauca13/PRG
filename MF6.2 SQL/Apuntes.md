# SQL

##### Lenguaje DDL
+ ```create```: crear tablas
+ ```alter```: modificar tablas
+ ```drop```: borrar tablas
+ ```truncate```: borrar tablas

##### Lenguaje DML
+ ```select```: seleccionar datos
+ ```insert```: introducir datos
+ ```update```: modificar datos
+ ```delete```: borrar datos

##### Lenguaje DCL
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
