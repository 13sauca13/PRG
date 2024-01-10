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

## 2. Modelos conceptuales
La base de datos se definirá en forma de descripción de texto, el llamado **Universo de discurso**

### Modelo entidad/relación

***Entidad***: Objeto que existe y puede distinguirse de otros a través de un conjunto de atributos ( :exclamation: **Tiene que tener características**) Se representa con un recángulo :orange_square:

>Existen atributos _descriptivos_ e _identificativos_ o _claves_ (los identificativos/claves son únicos, inequívocos y tienen que rellenarse siempre, los descriptivos si que pueden ser null).
Sólo puede haber un atributo identificativo en cada entidad, si existe algún otro valor que identifica de manera única se tratará de una _clave candidata_ (p.ej: matrícula y número de bastidor).

Tipos de entidades:
+ Entidades débiles: Su existencia depende de otra entidad.
+ Entidades fuertes

Los atributos pueden ser:
+ Simples o compuestos
+ Monovaluados o multivaluados
+ Almacenados o variados
Los dominios del atributo son los valores que puede coger


***Relación***: Asociación entre varias entidades (También pueden tener atributos). Son verbos y se representan con un rombo :large_orange_diamond:
