# Metodologías de la programación

:link: [JupyterHub](https://bb.eeae.es/hub/login?next=%2Fhub%2F) (Sólo en dominio EEAE. *login e2t_username*)

:mag: [Ejercicios](https://github.com/13sauca13/PRG/tree/master/MF5.2%20Metodolog%C3%ADas%20de%20la%20programaci%C3%B3n/Codigo)

>[!IMPORTANT]
>:book:[El Libro de Python](https://ellibrodepython.com/)

## 1. Lenguajes de programación
El primer lenguaje (más allá de los 0 y 1) fueron abreviaturas para dar órdenes a la máquina, se llamó **ensamblador**, pero dependía de la máquina en la que se ejecutaba. Los lenguajes fueron avanzando a niveles superiores de manera que fuera posible abstraerse del hardware.

Java de todas formas fue el primer lenguaje que fue multiplataforma creando por detrás una máquina virtual que se comunica con la plataforma, nuestro código fuente habla con esta máquina y ella es la que ejecuta las acciones. El códgo fuente se precompila y la máquina virtual lo lee y realiza lo necesario terminando de compilarlo.

Existen varios paradigmas (o maneras) de programación:
+ Programación imperativa: Uso de fórmulas que alteran el estado de un programa
+ Programación funcional: Se basa en el uso de funciones anónimas que reciben datos
+ Programación lógica: Se definen reglas y relaciones de inferencia para luego realizar consultas
+ Programación orientada a objetos (POO): Se basa en el uso de "objetos"

Diferentes lenguajes de programación:
+ Python: Sintaxis clara y legible. Multiparadigma
+ JavaScript: Sicripting de cliente. Utilizado para hacer webs interactivas.
+ Java: Utilizado en desarrollo empresarial, aplicaciones móviles...
+ PHP: Utilizado para desarrollo web del lado del servidor
+ SQL: Lenguaje para bases de datos

## 2. Técnicas fundamentales de programación
Los algoritmos son los pasos necesarios para conseguir el objetivo del programa

![Simbologia algoritmos](https://github.com/13sauca13/PRG/blob/master/Recursos/Simbolos%20diagramas%20de%20flujo.PNG)

Al programar las instrucciones (el "conjunto de instrucciones", que depende del procesador en si. Se tratan de instrucciones de bajo nivel) se ejecutan en un **ciclo de instrucción**, aunque ciertas operaciones necesitan más de un ciclo.

Los algoritmos presentan una serie de caracteristicas comunes:
+ ***Precisos*** Son objetivos, sin ambigüedad
+ ***Ordenador*** La secuencia es clara para llegar a la solución
+ ***Finitos*** Un conjunto determinado de pasos
+ ***Concretos*** Una solución determinada a una situación determinada
+ ***Definido*** El mismo algoritmo debe dar el mismo resultado con la misma entrada

La complejidad es una métrica teórica que nos ayuda a describir el comportamiento de un algoritmo en términos de tiempo de ejecución (tiempo que tarda un algoritmo en resolver un problema) ***complejiad temporal*** y memoria requerida (cantidad de memoria necesaria para procesar las instrucciones que solucionan dicho problema) ***complejidad espacial***.
+ **O(1)** Constante
+ **O(n)** Lineal
+ **O(log n)** logarítmica
+ **O(nlog n)** romper los problemas en varios trozos
+ **O(n<sup>2</sup>)** iteración por todos los elementos
+ **O(2<sup>n</sup>)** funciones que duplican la complejidad con cada elemento añadido
+ **O(n!)** explosión combinatoria

Existen dos formas de guardar bytes en memoria:
+ Big Endian: Los bytes se guardan por orden, el byte más significativo (más peso) se almacena en la dirección de memoria más baja, y los bytes siguientes se colocan en direcciones de memoria ascendentes (normalmente es así como trabajan los equipos)
+ Little Endian: El byte más significativo (más peso) se almacena en la dirección de memoria más baja, y los bytes siguientes se colocan en direcciones de memoria ascendentes.

La conversión de 0 y 1 a símbolos se realiza con codificación como puede ser UTF-8, UNICODE, ANSI, ASCII...

## 3. Estructuras
:interrobang:Revisar magic keywords (```if __name__=='__main__': print(__name__)```)
### 3.1 Estructuras de datos
#### Variables
Las variables son espacios de almacenamiento en la memoria que contienen datos con un nombre asociado y pueden cambiar durante la ejecución del programa.

#### Constantes
Son valores que no cambian durante la ejecución del programa, se utilizan para almacenar datos que se consideran inmutables.

#### Recursivas
Representan estructuras de datos anidadas, comúnmente utilizadas para modelar datos complejos y jerárquicos

#### Valores tipo tabla
Estructuras que permiten almacenar una colección de elementos bajo un solo nombre, existen varios tipos:
##### Listas
Se trata de una colección ordenada, editable, dinámica y no única.
```python
nombre_lista=[elemento1, elemento2...]
```
Funciones útiles:
+ ```list.append(x)```: agrega un elemento al final de la lista.
+ ```list.extend(iterable)```: Extiende una lista agregando todos los items del iterable indicado.
+ ```list.insert(i, x)```: Nos permite insertar un elemento en la posición indicada..
+ ```list.remove(x)```: Elimina el primer elemento de la lista igual a x. Si no consigue el elemento lanza un ValueError.
+ ```list.pop(i)```: Elimina un elemento en la posición indicada. Si no indicamos un elemento, elimina el último elemento de la lista.
+ ```list.clear()```: Elimina los elementos de la lista. Es equivalente a del lista[:]
+ ```list.index(elemento, inicio, fin)```: Nos permite buscar un elemento en la lista. Si no existe el elemento generará un ValueError
  + elemento - lo que buscamos
  + inicio (opcional) - Donde queremos que inicie la búsqueda
  + fin (opcional) - Donde queremos que detenga la búsqueda
+ ```list.count(x)```: Devuelve el número de veces que x aparece en la lista.
+ ```list.sort()```: Ordena los elementos de la lista, si queremos un orden inverso, podemos indicarle reverse=True dentro del paréntesis
+ ```list.reverse()```: Realiza una inversión de la lista.
+ ```list.copy()```: Hace una copia de la lista. recordar este detalle
##### Tuplas
Similar a las listas pero inmutables y más rápidas de procesar.
```python
nombre_tupla=(elemento1, elemento2...)
```
##### Set
Son varios valores almacenados en una misma variable. No están ordenados, no es modificable y no puede tener elementos repetidos (únicos y elementos inmutables). Se declaran con ```{}```
```python
nombre_set={valor1,valor2...}
```
##### Diccionario
Los diccionarios se utilizan para almacenar valores en pares **clave:valor** (es complejo pero los valores de las claves pueden ser también otro diccionario, una lista, una tupla). Es modificable y no permite duplicados (en los nombres de las claves)
***El tipo de dato de la clave (int,str...) va a ser el tipo de dato por defecto del valor también***

Hay dos maneras de crear un diccionario:
```python
nombre_diccionario=dict(clave1:valor1,clave2:valor2...)
```
```python
nombre_diccionario={clave1:valor1,clave2:valor2...}
```
:exclamation: ***Las claves de los diccionarios tienen nombres únicos***

Funciones:
+ ```diccionario.keys()```: Devuelve los valores de las claves del diccionario
+ ```diccionario.values()```:  Devuelve los nombres de las claves del diccionario

### Estructuras de control de selección
Permite ejecutar una o varias acciones basadas en condiciones.

Se trata de ```if```, ```elif``` y ```else```.

### Estructuras de control de iteración
#### ```for```
Ejecuta un bloque de código un número específico de veces.

Se utiliza normalmente con objetos iterables (listas, tuplas, diccionarios...). Esto nos permite que las iteraciones estén acotadas desde el inicio del mismo, al tamaño del objeto iterable. Su sintáxis básica es:
```python
for elemento in iterable:
  código
```
El bucle for, se utiliza normalmente con la función ```range```, que nos devuelve un iterable. Su uso básico es:
+ ```range(max)```: Iterable de numeros enteros consecutivos, empieza en 0 y termina en max-1.
+ ```range(min, max)```: Iterable igual que el anterior, pero que comienza en min y finaliza en max-1
+ ```range(min, max, step)```: Iterable igual que el anterior, pero que se incremente según el valor de step. 
#### ```while``` 
 ejecuta un código que se repite hasta cumplir una condición

## 4.Técnicas fundamentales de programación
### Tipos de datos
+ Enteros: Números enteros sin parte decimal
+ Textos: Strings
+ Decimales
  + 1.1
  + 1/3
  + 1.2E3
+ Booleanos: Sólo admite dos valores (```True``` y ```False```) True también será 1 y False será 0
+ Listas
+ Tuplas
+ Set
+ Diccionario

### Operadores
| Operador | Funcionamiento |
| --- | --- |
| + | Suma |
| - | Resta |
| * | Multiplicación |
| / | División |
| % | Módulo (resto de la división) |
| ** | Exponenciación |
| // | División exacta (Devuelve la división exacta, sin decimales. Sólo la parte entera del resultado) |
| > | Comparador "mayor que" |
| < | Comparador "menor que" |
| == | Comparador de igualdad |
| >= | Mayor o igual a |
| <= | Menor o igual a |
| != | No igual a |
| = | Asignador de valor |
| += | Asigna a la variable su valor más lo que viene a continuación |
| -= |  Asigna a la variable su valor menos lo que viene a continuación  |
| *= |  Asigna a la variable su valor por lo que viene a continuación  |
| /= |  Asigna a la variable su valor entre lo que viene a continuación  |
| %= |  Asigna a la variable el módulo de su valor entre lo que viene a continuación  |
| **= |  Asigna a la variable su valor elevado a lo que viene a continuación  |
| //= |  Asigna a la variable la división exacta de su valor entre lo que viene a continuación  |
| and | Operador lógico "and" |
| or | Operador lógico "or" |
| not | Operador lógico "not" (niega lo que venga después) |
| in | Operador de membresía "en" |
| not in | Operador de membresía "no en" |
| is | Compara si los objetos son iguales(no sólo los valores) |
| is not | Compara si dos objetos no son iguales |

### Asignación múltiple
La asignación múltiple es la acción de asignar de una vez varios valores a varias variables. Puedo asignar varios valores a varias variables a la vez:
```python
x, y, z...= valorX, valorY, valorZ...
```

Y podemos utilizar iterables para asignar esos valores:
```python
lista=[valor1, valor2, valor3...]
x, y, z, ...=lista
```

### Control de errores
```python
try:
  código
except tipo_error:
  código_si_try_falla
except tipo_error:
  código_si_try_falla
...
except:
  código_si_try_falla_generico
```

Los tipos de errores son los siguientes: [https://docs.python.org/3/library/exceptions.html](https://docs.python.org/3/library/exceptions.html)

Además de eso, la palabra ```raise``` me permite levantar un error "personalizado"

### Funciones
Las funciones se declaran con ```def``` y contienen argumentos y código:
```python
def nombre_funcion(argumento1, argumento2...):
  código
```
No se puede crear una función sin código, en caso de querer crear una función "vacía" se utiliza la palabra reservada ```pass```

Los argumentos pueden ser obligatorios y opcionales, pero los obligatorios deben ir al comienzo, por delante de los opcionales. Hay varias formas de introducir los argumentos:
+ Por posición, escribiendolas en el orden en el que aparecen al declarar la función
+ Declarando a que argumento pasamos el valor (p.ej. ```nombre_funcion(argumentoX=valor...)```)

Esto es lo básico para la declaración y uso de una función pero puede "decorarse", aunque esto es informativo, el programa no comprobará que se cumpla:
+ Especificar el tipo de dato que devolverá una función: ```def nombre_funcion(argumento1, argumento2...)->tipo_dato:```
+ Especificar el tipo de dato que espera un argumento: ```def nombre_funcion(argumento1:tipo_dato, argumento2:tipo_dato...)->tipo_dato:```

### Funciones Lambda

### Cadenas formateadas
El formateo de cadenas permite combinar variables y valores en una cadena. Hayo dos formas de hacerlo:
```python
print(f"string {variable}")
```
```python
print("string {}".format(variable))
```

## 5. Módulos
Los módulos son librerías para realizar una serie de funciones. Hay que llamarlos para utilizarlos: ```import nombre_modulo```

### ```os```
El módulo ```os``` sirve para interactuar con el sistema operativo de la máquina.

Tiene muchos [mètodos](https://www.w3schools.com/python/module_os.asp), los más usados:
| Método | Uso |
| --- | --- |
| ```os.makedirs(directorio)``` | Crear directorios |
| ```open(fichero, modo)``` | Abre ficheros para trabajar con ellos (el modo será ```r``` para lectura y ```w``` para escritura) |
| ```fichero.write(contenido)``` | Escribe en ```fichero``` el ```contenido``` |
| ```os.listdir(directorio)``` | Lista el contenido de un directorio |

### ```random```
Sirve para generar numeros aleatorios (o elecciones).

[Métodos de ```random```](https://www.w3schools.com/python/module_random.asp)

## 6.POO
Un ***objeto*** es un conjunto de ***atributos*** (variables o datos) y ***métodos*** o funciones relacionados entre sí.

Una ***clase*** equivale a la generalización de un tipo específico de objetos. Una clase es una plantilla que define las variables y los métodos que son comunes para todos los objetos de un cierto tipo. La clase define los atributos (datos) de un objeto y sus operaciones o métodos (comportamiento)
```
class Nombre_clase:
  código
```
Una vez definida la clase, se pueden crear objetos a partir de ésta, a dicho proceso se le conoce como crear ejemplares de una clase o instanciar una clase. Una ***instancia*** es un elemento de una clase, es decir, un objeto, cada objeto asigna valores a sus atributos y es totalmente independiente de los demás.

>[!WARNING]
>Cuando hay dos variables con el mismo nombre prevalece la de la instancia

### Atributos
Existen dos tipos de atributos:
### Atributos de clase
Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.
### Atributos de instancia
Pertenecen a la instancia de la clase o al objeto. **Son atributos particulares de cada instancia** 

Se utiliza ```self``` para referenciar las variables del propio objeto (lo vemos más adelante en detalle)

### Métodos
#### Metodos de instancia
Son los comportamientos de cada instancia de cada clase. Pueden acceder, editar, modificar los atributos de la instancia.

Reciben como argumento ```self```
```python
def nombre_metodo(self, argumento1, argumento2,...):
  código
```

#### Métodos de clase
Son comportamientos de la clase en si, NO pueden acceder a los atributos de las instancias pero SI pueden modificarlos.

Reciben como argumento ```cls```
```python
@classmethod
def nombre_metodo(cls):
  código
```
### Métodos estáticos
No modifican ni la clase ni la instancia
```pyhon
@staticmethod
def nombre_metodo():
  código
```
## 7.Librerías
Para la instalación de una librería externa se utiliza ```pip```, pero este instala la librería en el intérprete Python del sistema, si hay más de uno se debe poner antes la ruta:
```bash
ruta_python.exe -m pip install nombre_libreria
```
