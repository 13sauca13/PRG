# Metodologías de la programación

:link: [JupyterHub](https://bb.eeae.es/hub/login?next=%2Fhub%2F) (Sólo en dominio EEAE. *login e2t_username*)

:mag: [Ejercicios hechos en clase](https://github.com/13sauca13/PRG/blob/master/MF5.2%20Metodolog%C3%ADas%20de%20la%20programaci%C3%B3n/Codigo/1.%20Ejercicios%20clase.py)

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
+ Big Endian: Los bytes se guardan por orden (normalmente es así como trabajan los equipos)
+ Little Endian

La conversión de 0 y 1 a símbolos se realiza con codificación como puede ser UTF-8, UNICODE, ANSI, ASCII...

## 3. Estructuras
:interrobang:Revisar magic keywords (```if __name__=='__main__': print(__name__)```)
### 3.1 Estructuras de datos
#### Variables
#### Constantes
#### Listas
Se trata de una colección ordenada heterogénea y mutable.
```
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
#### Tuplas
#### Set
#### Diccionario
La manera de crear un diccionario es: ```nombre=dict()```

#### Estructuras de seleccón de selección

#### Estructuras de control de iteración
+ ```for```
+ ```while``` 
