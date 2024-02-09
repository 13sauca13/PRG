# SQL

:mag: [Scripts SQL de clase](https://github.com/13sauca13/PRG/tree/master/MF6.2%20SQL/Codigo)

> Ampliatorio:
> 
> :top: [Select Star SQL](https://selectstarsql.com/) - Libro/guía interactivo
> 
> :video_game: [SQL Murder Mistery](https://mystery.knightlab.com/) - Juego de investigación de un asesinato con SQL

## 1. Componentes del SQL

:eyes: [**SQL Keywords**](https://www.w3schools.com/SQL/sql_ref_keywords.asp)

:eyes: [**SQL Cheat Sheet** - Hoja guia de SQL en pdf](https://learnsql.com/blog/sql-basics-cheat-sheet/sql-basics-cheat-sheet-a4.pdf)

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

Para realizar una copia de seguridad de la base de datos en principio bastaría con copiar los archivos .mdf (en la ruta .../sqlserver/data) y .ldf (en la ruta .../sqlserver/log)


## 3. Data Definition Lenguage (DDL - Creación de tablas)
>[!TIP]
>Para que el código ejecutado sea en una base de datos se comienza la query con:
>```
>use nombre_db
>go
>```

### 3.1 Crear una tabla
```
CREATE TABLE nombre_tabla
(
campo1 TIPO_DATO,
campo2 TIPO_DATO,
 …
);
```

Después del tipo de dato podremos indicar también si es NULL o NOT NULL, y también si es UNIQUE.

Tipos de datos en las tablas (resaltados los principales):
| Dato | Explicación |
| --- | --- |
| bigint | Numero entero (max. 8 bytes) |
| binary(x) | x bytes de datos binarios |
| bit | Un bit que funciona como booleano (true=1 o false=0) |
| char(x) | x bytes caracteres alfanuméricos (ocupa los x bytes de memoria) No Unicode |
| date | Fechas (formato AAAA-MM-DD) |
| datetime | Fechas (formato AAAA-MM-DD hh:mm:ss) |
| datetime2(x) | Fechas (formato AAAA-MM-DD hh:mm:ss.nnnnnnn) |
| datetimeoffset(x) | Fechas (formato AAAA-MM-DD hh:mm:ss.nnnnnnn [+/-] hh:mm) |
| decimal(x,q) | Número decimal con x dígitos TOTALES, de los cuales q serán decimales (sinónimo de ```numeric(x,q)``` )|
| float(x) | Datos numéricos aproximados de coma flotante ( siendo x los bits de la parte decimal) |
| geography | Para almacenar datos espaciales elipsoidales como coordenadas de latitud y longitud GPS |
| geometry | Para almacenar datos espaciales planares en un sistema de coordenadas euclídeo |
| hierarchyid | Para representar la posición en una jerarquía de árbol |
| image | Datos binarios de longitud variable |
| :exclamation: **int** | **Numero entero (max. 4 bytes)** |
| money | Dato para valores monetarios (max. 8 bytes) |
| nchar(x) | x bytes de caracteres Unicode (ocupa los x bytes) |
| ntext | Caracteres alfanuméricos Unicode |
| :exclamation: **numeric(x,q)** | **Número decimal con x dígitos TOTALES, de los cuales q serán decimales** |
| :exclamation: **nvarchar(x)** | **Caracteres Unicode (max. x bytes)** |
| nvarchar(MAX) | Caracteres Unicode de más de 8000 bytes (max. 2^31 bytes) |
| real | Datos numéricos de coma flotante (sinónimo de ```float(24)```|
| smalldatetime | Fechas (formato AAAA-MM-DD hh:mm:ss) |
| smallint | Numero entero (max. 2 bytes) |
| smallmoney | Dato para valores monetarios (max. 4 bytes) |
| sql_variant | Para almacenar valores de varios tipos de datos admitidos en SQL Server |
| text | Caracteres alfanuméricos No Unicode |
| time(x) | Hora (formato hh:mm:ss.nnnnnnn) |
| timestamp | EN DESUSO. Tipo de datos binarios únicos generados automáticamente para las versiones de las filas de una tabla |
| tinyint | Numero entero (max. 1 byte) |
| uniqueidentifier | Para almacenar identificadores únicos globales (GUID) |
| varbinary(x) | Datos binarios (max. x bytes) |
| varbinary(MAX) | Datos binarios de más de 8000 bytes (max. 2^31 bytes) |
| :exclamation: **varchar(x)** | **Caracteres alfanuméricos (max. x bytes) No Unicode** |
| varchar(MAX) | Caracteres alfanuméricos (max. x bytes) No Unicode |
| xml | Para almacenar datos XML |

> [!TIP]
> Podemos utilizar números autoincrementables utilizando el tipo ```int``` y añadiendole "identidad":
>
> ``` atributo int IDENTITY (num_inicio, valor_incremento) ```
>
> El valor de un identidad se rellena automáticamente y es NOT NULL. Para modificarlo o introducirlo manualmente hay que cambiar el ```IDENTITY_INSERT``` a ON y utilizar lista de columnas para declarar el valor (NO vale hacerlo sólo con el orden de los valores, hay que usar primero el listado de campos):
> ```
> SET IDENTITY_INSERT nombre_tabla ON
> INSERT INTO nombre_tabla (campo1, campo2,...) VALUES (valor_campo1, valor_campo2,...);
> ```

### 3.2 Modificar los campos de una tabla
```
ALTER TABLE nombre_tabla
ALTER COLUMN campo TIPO_DATO:
```

## 4. Data Manipulation Language (DML - Consultas y trabajo con las tablas)
>[!CAUTION]
>Las búsquedas NO son "case sensitive" (no diferencian mayúsculas de minúsculas) pero SI afectan los acentos y caracteres especiales

Las consultas se realizarán con ```SELECT```:

```
SELECT campo FROM nombre_tabla
WHERE campo=valor
```

En el valor del campo podemos usar ```*``` para seleccionar todo y también pueden ser usados operadores en los valores (lógicos, de comparación...):
| Operador | Significado |
| --- | --- |
| ```=``` |	Igual a |
| ```>``` | Mayor que |
| ```<``` |	Menor que |
| ```>=``` | Mayor o igual que |
| ```<=``` | Menor o igual que |
| ```<>``` |	No es igual a |
| ```!=``` |	No es igual a |
| ```!<``` |	No es menor que |
| ```!>``` |	No es mayor que |
| ```ALL``` |	TRUE si el conjunto completo de comparaciones es TRUE. |
| ```AND``` |	TRUE si ambas expresiones booleanas son TRUE. |
| ```ANY``` |	TRUE si cualquier miembro del conjunto de comparaciones es TRUE. |
| ```BETWEEN``` |	TRUE si el operando está dentro de un intervalo. |
| ```EXISTS``` |	TRUE si una subconsulta contiene cualquiera de las filas. |
| ```IN``` |	TRUE si el operando es igual a uno de la lista de expresiones. |
| ```LIKE``` |	TRUE si el operando coincide con un patrón. |
| ```NOT``` |	Invierte el valor de cualquier otro operador booleano. |
| ```OR``` |	TRUE si cualquiera de las dos expresiones booleanas es TRUE. |
| ```SOME``` |	TRUE si alguna de las comparaciones de un conjunto es TRUE. |

Después de la consulta podemos hacer un ordenamiento de los datos devueltos, el ordenamiento por defecto será ascendente, pero se puede introducir ```ASC``` ó ```DESC``` tras el campo:

```
SELECT campo FROM nombre_tabla
WHERE campo=valor
ORDER BY campo [ASC/DESC], campo [ASC/DESC],...
```

También se pueden utilizar operadores en las consultas:
+ ```like```: Busca coincidencia con un patrón (el patrón es una cadena que puede incluir uno o más caracteres comodines). Existen dos [wildcards](https://www.w3schools.com/sql/sql_wildcards.asp) para el ```like```
  + ```%```: Respresenta un número indeterminado de caracteres (cero, uno o muchos)
  + ```_```: Representa un único caracter

### 4.1 Funciones
SQL tiene funciones incluídas para conversiones y funciones avanzadas:
+ ```DATEDIFF(intervalo, fecha1, fecha2)```: Calcula la diferencia entre dos fechas (el intervalo es MM para meses, YYYY años,... :eyes:[SQL DATEDIFF](https://www.w3schools.com/sql/func_sqlserver_datediff.asp)
+ ```GETDATE()``` : Devuelve la fecha actual
+ ```CONVERT(tipo_dato(longitud),expresion_a_convertir,estilo)```: Convierte datos de un formato a otro (los estilos tienen un código numérico :eyes:[SQL CONVERT](https://www.w3schools.com/sql/func_sqlserver_convert.asp))
+ ```ROUND(numero,decimales)```: Redondea un número

Al utilizar estas funciones "creo" columnas que no existen ni están metidas en ninguna tabla de manera que no tienen nombre, puede utilizarse un ***alias*** para esta columna recién creada:

```
SELECT funcion AS alias FROM nombre_tabla
WHERE campo=valor...
```

#### Funciones de agregado
Todas las funciones de agregado expuestas desprecian el NULL salvo el ```COUNT```

| Función | Descripción |
| --- | --- |
| ```AVG``` | "Average", media aritmética |
| ```COUNT``` | Cuenta el número de valores |
| ```MAX``` | Valor máximo |
| ```MIN``` | Valor mínimo |
| ```SUM``` | Sumatorio |
| ```STDEV``` | Desviación típica |
| ```VAR``` | Varianza |
| ```COUNT_BIG``` | Se utiliza para conteo con bigint |

Con las funciones ```AVG```, ```COUNT```, ```MAX```, ```MIN``` y ```SUM``` se suele utilizar ```GROUP BY``` para dividir las filas de resultados en grupos en funcion de sus valores en una o varias columnas:

```
SELECT funcion(campo) FROM nombre_tabla
GROUP BY campo
HAVING campo=valor
```

:exclamation: ***Todo lo que esté fuera de la función de agregado tiene que estar en ```GROUP BY```***

## 4.2 Joins
Las clausulas ```JOIN```se utilizan para combinar filas de dos o más tablas basado en una columna relacionada entre ellas (normalmente FK y PK)

Existen diferentes tipos de combinaciones, siendo la más simple ```INNER JOIN```

```
SELECT campos FROM tabla1 INNER JOIN tabla2 
ON tabla1.campo = tabla2.campo
WHERE campo=valor
```

Se pueden encadenar todos los ```JOIN```necesarios:
```
SELECT campos FROM tabla1 INNER JOIN tabla2 
ON tabla1.campo = tabla2.campo
INNER JOIN tabla3
ON tabla2.campo = tabla3.campo
INNER JOIN tabla4
ON tabla3.campo = tabla4.campo
...
WHERE campo=valor
```

Existen también:
+ ```LEFT JOIN```: Devuelve todos los datos de la tabla1 y los coincidentes de la tabla2
+ ```RIGHT JOIN```: Devuelve todos los datos de la tabla2 y los coincidentes de la tabla1
+ Existen también ```FULL JOIN```y ```SELF JOIN```...

![Inner Join](https://github.com/13sauca13/PRG/blob/master/Recursos/inner_join.png) ![Left Join](https://github.com/13sauca13/PRG/blob/master/Recursos/left_join.png) ![Right Join](https://github.com/13sauca13/PRG/blob/master/Recursos/right_join.png)

## 4.3 Unions
Se utiliza para combinar los resultados de dos o más consultas en un único resultado. (Los campos de las consultas deben coincidir en cantidad y tipo)

```
SELECT campo FROM tabla
UNION
SELECT campo FROM tabla2
```

## 4.4 Introducción de datos
### ```INSERT```
Se introducen los datos por el orden en el que se decrararon los atributos en la tabla:

```INSERT INTO nombre_tabla VALUES (valor_campo1, valor_campo2,...);```

O podemos declara los campos que vamos a rellenar si no vamos a introducir datos en todos los campos:

```INSERT INTO nombre_tabla(campo1, campo2,...) VALUES (valor_campo1, valor_campo2,...);```

***Ojo a los tipos de datos y el formato en el que se deben introducir*** (p.ej. strings entre comillas simples ``` 'string' ``` )

### ```UPDATE```
Se utiliza el comando update para modificar filas, grupos de filas o todas las filas de una tabla.

```
update tabla
set campo = valor
where <condiciones>
```
