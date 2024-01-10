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

***Entidad***: Objeto que existe y puede distinguirse de otros a través de un conjunto de atributos (:bangbang: **Tiene que tener características**)

Existen atributos descriptivos e identificativos (los segundos son únicos, inequívocos y tienen que rellenarse siempre, los descriptivos si que pueden ser null)

***Relación***: Asociación entre varias entidades


