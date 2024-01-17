# Bases de datos

:bulb: ***Dato: mínima unidad de la que vamos a obtener info. (son "atómicos", no pueden ser divididos en menos)***

Los usuarios através de aplicaciones se comunicacn con el SGBD (Sistema Gestor de Base de Datos) y este es el que realiza los consultas o actualizaciones de la propia base de datos.

El SGBD nos proporciona:
+ Acceso controlado a los datos
  + Control de seguridad
  + Control de integridad
  + Control de concurrencia (actualización simultánea de datos)
  + Control de recuperación (mecanismos de recuperación de datos contra fallos lógicos/físicos)
  + Diccionario de datos
+ Lenguajes de gestión (el lenguaje estándar es el SQL):
  + Lenguaje de definición de datos (LDD)
  + Lenguaje de manejo de datos (LMC)
  + Lenguaje de control de datos (LCD)

#### Visión de los datos
| Nivel | Descripción |
| --- | --- |
| Nivel físico | Nivel más bajo de abstracción (como se almacenan los datos) |
| Nivel lógico/conceptual | Descibe que datos serán almacenados y como se relacionan |
| Nivel externo | Nivel de abtracción más alto, es lo que el usuario visualizará |

![SGBD](https://github.com/13sauca13/PRG/blob/master/Recursos/Esquema%20SGBD.PNG)

## 2. Modelo conceptual Entidad/Relación
La base de datos se definirá en forma de descripción de texto, el llamado **Universo de discurso**

#### Entidad
Objeto que existe y puede distinguirse de otros a través de un conjunto de atributos ( :exclamation: **Tiene que tener características**) Se representa con un recángulo :orange_square:

>Existen atributos _descriptivos_ e _identificativos_ o _claves_ (los identificativos/claves son únicos, inequívocos y tienen que rellenarse siempre, los descriptivos si que pueden ser null).
Sólo puede haber un atributo identificativo en cada entidad, si existe algún otro valor que identifica de manera única se tratará de una _clave candidata_ (p.ej: matrícula y número de bastidor).

Tipos de entidades:
+ Entidades débiles: Su existencia depende de otra entidad o no tienen atributo identificativo y tienen que cogerlo de otra. (Se representan con dos rectángulos concéntricos :white_square_button:)
+ Entidades fuertes: Tienen existencia por si mismas y tienen atributo identificativo. 

Los atributos pueden ser:
+ Simples o compuestos
+ Monovaluados o multivaluados
+ Almacenados o variados

Los dominios del atributo son los valores que puede coger

#### Relación
Asociación entre varias entidades (También pueden tener atributos). Son verbos y se representan con un rombo :large_orange_diamond:

Cada entidad desempeña una función en una relación que se denomina ***rol***, y en cada relación pueden participar dos o más entidades, esto es el grado de relación (binaria, ternaria, si hay dos relaciones entre las mismas entidades es doble...)

La asociación entre conjuntos de entidades se denomina ***participación***.

Tipos de relaciones:
+ **Relación de matrimonio**
+ **Relación cursiva o reflexiva**: Cuando una entidad se relaciona consigo misma
+ **Relación de generalización**: Varios conjuntos de entidades se sintetizan en un conjunto de entidades de nivel superior basado en características comunes.
+ **Relación de agregación**: En el modelo Entidad-Relación no se pueden expresar relaciones entre relaciones, la agrupación consiste en agrupar en un rectángulo a la relación y las entidades y atributos involucrados para formar una entidad nueva. (La cardinalidad tiene que ser M:N)

##### Cardinalidad
Es la cantidad de relaciones que pueden establecerse entre entidades o la expresión del número de entidades a las que otra entidad se puede asociar mediante un conjunto de relaciones.
+ Ralaciones uno a uno (1:1) (p.ej. los matrimonios)
+ Relaciones uno a varios (1:N) (p.ej. un tutor y varios alumnos)
+ Relación varios a varios (M:N)

Existen restricciones de participación u obligatoriedades en la cardinalidad:
+ Total: Si todas se relacionan con todas (Obligatoriedad 1)
+ Parcial: No todas se relacionan con todas (Obligatoriedad 0)

Existen diferentes perfiles involucrados en un sistema de base de datos:
+ Administradores
+ Usuarios

Los diseñadores de la base de datos deben interactuar con los expertos y usuarios del dominio para llevar a cabo la tarea. El diseñador escoge un modelo de datos y traduce esos requisitos en un esquema conceptual de la base de datos.

El diseño de la base de datos se denomina ***esquema de la base de datos***.
>**El esquema se modifica rara vez**

La información almacenada en un momento dado en la base de datos es el ***ejemplar de la base de datos***.

## 3. Modelo conceptual relacional
>[!CAUTION]
>En el modelo relacional cambia la nomenclatura:
>
>Las **ENTIDADES** del E/R pasan a llamarse **RELACIONES**
>
>Las **RELACIONES** del E/R son **INTERRELACIONES**

El elemento central del modelo relacional es la relación:
+ **Entidades**: Cada entidad del equema E/R da lugar a una nueva relación (tabla). Esta relación tiene sus características:
  + La tabla es bidimensional, con filas (tuplas) y columnas
  + Es implementable en el SGBD
  + El número de atributos de una relación es el ***grado***
  + El número de tuplas en un momento dado es las ***extensión o cardinalidad***
  + Cada relacuón tiene un nombre distinto
  + El valor de los atributos es atómico (NO hay atributos multivaluados)
  + Pueden existir valores vacíos o nulos
  + Cada atributio de la misma relación tiene distinto nombre
  + No existen dos tuplas exactamente iguales
  + ***No puede haber  atributos que formen parte de la clave primaria que tengan valor nulo***

Los valores del atributo clave de una relación pasarán a la otra como FK(Foreign Key). La restricción de clave ajena, más conocida como ***integridad  referencial***, nos indica que los valores de clave ajena en la relación “hijo” deben corresponderse con los valores de la clave primaria “padre”. 
El nombre de los atributos no tienen por qué llamarse igual.
+ **UNIQUE**: El valor debe ser único.
+ **NO NULL**: Restricción de obligatoriedad
+ **CASCADE**: Borrado en cascada. Si se modifica o borra en la tabla padre se modifican o borran las tuplas de las tablas hijas
+ **CHECK**: Comprueba una condición que deben cumplir los valores de determinados atributos
+ **ASSERTION**: Lo mismo que una restricción “check” pero no solo tienen ámbito en una sola tabla. Afecta a varias tablas

#### Migración del modelo E/R al modelo relacional
Reglas:
+ Cada entidad es una tabla
+ En las entidades bébiles se añade la clave primaria de la entidad de la que dependen
+ Relaciones:
  + 1:1 En una de las entidades se introduce como FK la clave primaria de la otra entidad
  + 1:N En la entidad B (parte N) se introduce como FK la clave primaria de la entidad A (parte 1)
  + M:N: Se crea una nueva entidad (tabla) que tiene las claves de cada una de las otras dos entidades.
+ Atributos:
  + Compuestos: Dan lugar a varios atributos
  + Multivaluados: Dan lugar a varios atributos y una nueva tabla con ralación 1:N o M:N
+ Las entidades agregadas no se traducen en tablas
  + Relación de agregación 1:N, adquiere como parte de su clave la clave primaria de la relación interna de agregación
  + Relación de agregación M:N, Genera una nueva tabla que incluye la clave primaria de la relación interna de la agregación y la clave primaria de la otra entidad.
