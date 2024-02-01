# SQL

:mag: [Scripts SQL](https://github.com/13sauca13/PRG/tree/master/MF6.2%20SQL/Codigo)

## 1. Componentes del SQL

:eyes: [**SQL Keywords**](https://www.w3schools.com/SQL/sql_ref_keywords.asp)

##### Lenguaje DDL
Se usa para crear y definir nuevas bases de  datos
+ ```create```: crear tablas
+ ```alter```: modificar tablas
+ ```drop```: borrar tablas enteras
+ ```truncate```: borrar el contenido de tablas (no la tabla en si misma)

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


## 2.Bases de datos del sistema
![Bases de datos del sistema](https://github.com/13sauca13/PRG/blob/master/Recursos/Bases%20de%20datos%20del%20sistema.PNG)

+ **master**: En esta BD se encuentra la información sobre las cuentas de los usuarios y la configuración del sistema. Asimismo, tiene información sobre dónde localizar las BD que creamos.
+ **model**: Siempre que se crea una base de datos, SQL SERVER inicia una copia de MODEL. Plantilla para las base de datos nuevas
+ **msdb**: Aqui se guarda la programación de copias de seguridad e información que se necesita para procesar trabajos y alertas.
+ **tempdb**: En ella se almacenan todas las tablas temporales que se generan durante la ejecución de los procesos. Cada vez que se hace una transacción se crea tabla. Existen sólo dos tablas:
  + **inserted**
  + **deleted**

:exclamation: ***Sólo los usuarios con rol sysadmin (normalmente será sólo uno, "sa") pueden crear usuarios***

>Crear un usuario:
>```
>create login username
>wiht password='contraseña',
>default_database=master,
>check_expiration=off,
>check_policy=off;
>```
>La default_database tiene que ser ```master``` porque es donde tienen que estar las cuentas de usuario. Al crear un usuario en realidad se crea el login y la conexión ambos con el mismo nombre. Si creasemos el login en una base que no es la master se crearía sólo la conexión para esa base, pero no el login.
>
>```check_expiration``` es para la expiración de la cuenta
>
>```check_policy``` es la política de complejidad de contraseñas (min. 8 caracteres y max. 12)
>
>Borrar usuario:
>```
>drop login username;
>```

## 2. Manejo de SQL
>[!TIP]
>Para que el código ejecutado sea en una base de datos se comienza la query con:
>```
>use nombre_db
>go
>```

#### Crear una tabla
```
CREATE TABLE nombre_tabla
(
campo1 tipo_dato,
campo2 tipo_dato,
 …
);
```

Tipos de datos en las tablas (resaltados los principales):
| Dato | Esplicación |
| --- | --- |
| bigint | |
| binary(x) | |
| bit | es un booleano (true o false) |
| char(x) | x caracteres, que aunque no se usen todos, los huecos se rellenan igualmente en memoria |
| date | fechas |
| datetime | |
| datetime2(x) | |
| datetimeoffset(x) | |
| decimal(x,q) | número decimal con x a la izquierda de la coma y q a la derecha |
| float | |
| geography | |
| geometry | |
| hierarchyid | |
| image | |
| **int** | **numero entero** |
| money | dinero |
| nchar(x) | texto con caracteres especiales |
| ntext | |
| **numeric(x,q)** | **número decimal con x dígitos TOTALES, de los cuales q serán decimales** |
| **nvarchar(x)** | **************************************REVISAR |
| nvarchar(MAX) | |
| real | |
| smalldatetime | |
| smallint | |
| smallmoney | |
| sql_variant | |
| text | |
| time(x) | |
| timestamp | |
| tinyint | |
| uniqueidentifier | |
| varbinary(x) | |
| varbinary(MAX) | |
| varchar(x) | |
| varchar(MAX) | |
| xml | |
