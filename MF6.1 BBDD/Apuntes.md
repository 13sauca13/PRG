# Bases de datos

>[!TIP]
>:man_teacher: [Ejercicios de clase](https://github.com/13sauca13/PRG/blob/master/MF6.1%20BBDD/Ejercicios/0.%20Ejercicios%20clase.md)

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
  + Lenguaje de definición de datos (DDL)
  + Lenguaje de manejo de datos (DML)
  + Lenguaje de control de datos (DCL)

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
Objeto que existe y puede distinguirse de otros a través de un conjunto de atributos ( :exclamation: **Tiene que tener características**) Se representa con un rectángulo :orange_square:

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
+ **Relación de generalización**: Varios conjuntos de entidades se sintetizan en un conjunto de entidades de nivel superior basado en características comunes (la entidad superior es el ***supertipo*** y las inferiores ***subtipo***).
  + Si todas las entidades tienen todos los atributos del supertipo se llama ***total*** (si no es ***parcial***)
  + Si una misma entrada del supertipo puede ser más de un subtipo se llama ***solapamiento***, si sólo puede ser uno se llama ***exclusividad***
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
  + 1:N La clave primaria de la entidad A (parte 1) migra como FK a la entidad B (parte N)
  + M:N: Se crea una nueva entidad (tabla) en donde la clave primaria estará formada por las claves primarias que participan en la relación
+ Atributos:
  + Compuestos: Dan lugar a varios atributos
  + Multivaluados: Dan lugar a varios atributos y una nueva tabla con ralación 1:N o M:N (la clave serán el valor del atributo y la clave primaria de la entidad original)
+ Las entidades agregadas no se traducen en tablas
  + Relación de agregación 1:N, adquiere como parte de su clave la clave primaria de la relación interna de agregación
  + Relación de agregación M:N, Genera una nueva tabla que incluye la clave primaria de la relación interna de la agregación y la clave primaria de la otra entidad.
+ Conversión con valores opcionales:
  + 1:1 obligatoria-opcional: La entidad con participación opcional migrará como FK a la otra tabla  como NO NULL y UNIQUE
  + 1:1 opcional-opcional: Se crea una tabla nueva que recibe las claves de las dos entidades para evitar valores nulos (la clave de esta tabla serán las dos claves)
  + 1:N obligatoria-opcional: La clave de la parte 1 migra al lado N como NO UNIQUE y NULL
  + 1:N opcional-obligatoria: La clave de la parte 1 migra al lado N como NO UNIQUE y NO NULL
  + 1:N opcional-opcional: La clave de la parte 1 migra a la parte N como NO UNIQUE y NULL
  + M:N independientemente de la obligatoriedad da lugar a una nueva tabla con las claves de ambas partes
+ Los atributos de las interrelaciones por norma general hay que llevar ell atributo a donde migre la FK (hay excepciones, habria que estudiar bien el universo de discurso, podría crearse una nueva tabla)
+ Las relaciones de generalización tiene tres opciones a elegir (preferimos la 2)
  1. Crear una nueva tabla con los atributos del supertipo y todos los subtipos
  2. Creamos una tabla por cada entidad y la clave del supertipo migra a cada subtipo
  3. Crear una tabla por cada subtipo incluyendo los atributos comunes en cada una
+ Las interrelaciones reflexivas se convierten en dos tablas, una para la entidad y otra para la interrelación excepto en dos casos:
  + Reflexiva 1:1 se crea un nuevo atributo que es la clave de la otra parte de esa interrelación (igual que se migran las FK pero migra a la misma tabla)
  + Reflexiva 1:N hay que tener en cuenta la cardinalidad del lado N
    + Si no es obligatoria se crea una nueva tabla cuya clave será la del lado muchos y se propaga la clave a la nueva tabla como FK
    + Si es obligatoria no se crea una nueva tabla
  + Reflexiva M:N crea una nueva tabla a la que migran dos veces las claves (por cada emparejamiento) y la clave será la unión de ambas claves
+ Las relaciones ternarias crean una nueva tabla con el nombre de la interrelación con las claves de las partes "muchos"

Para poder enlazar una clave con otra tiene que cumplir unas condiciones (Estos 7 conceptos se implementan en el SGBD):
1. ***Integridad referencial*** (restricción de clave ajena): El valor de la FK en la relación hijo debe corresponder con los valores de la clave primaria padre
2. Las claves candidatas deben tratarse como UNIQUE
3. Restricción de obligatoriedad (NOT NULL)
4. Opcion de borrado en cascada (CASCADE): Si borro en una tabla padre deben borrarse las tuplas de la tabla hijo
5. Modificación en cascada (como borrado en cascada pero modificando, no borrando)
6. Restricción de verificación (CHECK): cuando es necesario cumplir una condición en los valores
7. ASSERTION: Es restricción de verificación que afecta a varias tablas

>[!IMPORTANT]
>Cuando dos tablas están relacionadas existen 4 opciones y cada una de ellas se aplica por separado a la modificación (***UPDATE***), al borrado (***DELETE***) o a las dos cosas:
>+ **CASCADE**: Actualiza y/o borra las tuplas de la otra tabla
>+ **SET NULL**: Deja en null el valor de la otra tabla
>+ **SET DEFAULT**: Pone un valor por defecto en la otra tabla
>+ **NOT ACTION** o **RESTRICT**: No hace nada

##### Normas formales
Las normas formales (NF) proporcionan criterios para determinar el grado de vulnerabilidad de una tabla a inconsistencias y anomalías lógicas. Son aplicables a tablas individuales.
1. Todos los valores asociados a un atributo deben ser un valor único y atómico
2. Tiene que estar en 1ªNF. Todos los atributos que no formen parte de la clave tienen que depender completamente de la clave
3. Tiene que estar en 1ªNF y 2ªNF. El valor de los atributos que NO son clave primaria no puede depender de atributos que no sean clave primaria.
