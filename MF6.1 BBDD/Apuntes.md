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
| Nivel lógico/conceptual | |
| Nivel externo | |

## 2. Modelos conceptuales

### Modelo entidad/relación

***Entidad***: Objeto que existe y puede distinguirse de otros a través de un conjunto de atributos ( :exclamation: **Tiene que tener características**) Se representa con un recángulo :orange_square:

Existen atributos _descriptivos_ e _identificativos_ (los segundos son únicos, inequívocos y tienen que rellenarse siempre, los descriptivos si que pueden ser null).
Sólo puede haber un atributo identificativo en cada entidad, si existe algún otro valor que identifica de manera única se tratará de una _clave candidata_ (p.ej: matrícula y número de bastidor).

***Relación***: Asociación entre varias entidades. Son verbos y se representan con un rombo :large_orange_diamond:


