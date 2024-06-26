# JAVA

:mag:[Ejercicios](https://github.com/13sauca13/PRG/tree/master/MF5.3%20Lengujes%20de%20progr.%20II/Codigo)

>[!IMPORTANT]
>:link:[Java W3 Schools](https://www.w3schools.com/java/java_ref_keywords.asp)
>
>:link:[Java API](https://docs.oracle.com/en/java/javase/22/docs/api/index.html)
>
>:book:[Libro "Java para novatos"](https://github.com/13sauca13/PRG/blob/master/MF5.3%20Lengujes%20de%20progr.%20II/Java%20para%20novatos.pdf)



Existen dos paquetes de software: JDK y JRE.

JDK es el paquete de software que utilizamos para crear nuestras aplicaciones.

El JRE (Java Runtime Enviroment) permite usar aplicaciones y es también la máquina virtual de Java que ejecuta el código. JDK contiene también el JRE.

El Java al ser multiplataforma tiene que ser compilado (del código fuente se compila el "bytecodes") y posteriormente interpretado por el JRE.

## "Escribir" en Java
Lo primero es crear una clase (para Java TODO son objetos). Por ejemplo:

```java
public class Nombre_clase:{
  public static void main(String args []){
    System.out.println("hola mundo");
  }
}
```
```public``` es el modificador de acceso, existen tres en Java:
+ ```public```
+ ```private```
+ ```protected```

Los nombres de las clases siempre tienen que empezar por mayúscula.

Para ejecutar el programa primero hay que compilarlo con ***javac***: ```javac nombrearchivo.java```. Esto creará un archivo .class (el bytecode) que se podrá ejecutar.

A continuación se ejecuta: ```java Nombre_clase```

Sólo se va a llamar a la clase principal (aunque haya muchas más). El archivo .java tiene que llamarse igual que esa clase main.
>[!TIP]
>Cuando trabajamos con Java, por defecto usamos el paquete java.lang, por lo que podemos acceder a sus clases sin más.
>
>Si vamos a usar clases de otro paquete habría que especificarlo.

### Variables
Para declarar una variable:
```java
tipo_dato nombre_variable;
```

El alcance de una variable hace referencia a las áreas del programa donde funcionan ciertos datos
+ **Variables de clase**: Pueden usarse en cualquier método de la clase y se inicializan con valores por default
+ **Variables locales**: Sóplo pueden usarse en el método en el que se definen y deben inicializarse
+ **Variables estáticas**: Se crean con la clase y son estáticas (se definen con ```static```) pero pueden modificarse

Si la variable va a ser una constante (no podrá modificarse)
```java
final tipo_dato nombre_constante;
```
#### Modificar valores de las variables
Para introducir datos por parte del usuario existen dos clases:
+ ```scanner```
+ ```JOptionPane```

Existen dos formas de pasar los valores:
+ Paso por valor: Se asigna directamente el valor de la variable
+ Paso por referencia: Se asigna el valor del espacio de memoria de otra variable u objeto

Si existen dos variables refereciadas, para poder borrar una sin eliminar los datos del espacio de memoria y perdiendo también los datos en la segunda habría que asignar a la variable que queremos borrar el valor ```null``` de manera que dejamos de referenciar ese espacio de memoria y ya podría ser borrada sin eliminar los datos de la segunda,
  
#### Tipos de variables
Existen 2 tipos de datos en Java: Primitivos y Referenciados.

##### Tipos primitivos
Existen 8 tipos de datos primitivos: (cualquier dato diferente a estos es una clase)
+ Enteros
  +  ```byte``` (1 byte): de -128 a 127
  +  ```short``` (2 bytes): -32768 a 32767
  +  ```int``` (4 bytes)
  +  ```long``` (8 bytes): los long necesitan el sufijo ```L```
  +  ```char``` (2 bytes): caracteres, ***NO*** es string! Es un único caracter (string es una clase en Java) Los ```char``` van entre comillas simples ```' '``` (los strings entre comillas dobles ```" "```). Son tipo entero porque aun siendo caracteres no se trata de letras si no de números de posición en la tabla UNICODE
+ Flotantes:
  + ```float``` (4 bytes): máximo 6 o 7 decimales
  + ```double``` (8 bytes): máximo 15 decimales. los double necesitan el sufijo ```f```
+  ```boolean```

##### Tipos referenciados (tipo object)
Son:
+ Clases
  + ```String``` (la comparación de strings se hace con ```equals```)
+ Interfaces
+ Arreglos (*arrays*)
###### Arreglos
Para crear un arreglo se hace de la siguiente manera (los nombres se recomiendan en plural): ```tipo_dato nombre_arreglo []``` o ```tipo_dato [] nombre_arreglo```

Una vez creado hay que instanciarlo: ```nombre_arreglo = new tipo_dato [longitud_arreglo]```

Para inicializar los datos: nombre_arreglo[indice] = valor```

También pueden declararse de manera rápida dando directamente los datos:
```java
tipo_dato [] nombre_arreglo = {valor1, valor2 ...}
```

Se pueden crear arreglos con datos primitivos y con objetos.

Para crear una matriz hacemos un arreglo con dos longitudes (numero de filas y de columnas): ```nombre_arreglo = new tipo_dato [filas] [columnas]```

>[!TIP]
>Para introducir datos se utiliza el índice o se rellena entero:
>+ ```nombre_array[indice] = valor```
>+ ```tipo_dato nombre_array[] = {valor,valor2...}```



### Expresiones
#### Condicionales (```if``` y ```else```)
```java
if ( condicion ) {
  //Sentencia a ejecutar si es verdadero ;
}
else if ( condicion ) {
  //Sentencia...
}
...
else {
  //Sentencia a ejecitar si es falso ;
}
```
Los corchetes se pueden omitir si hay una única sentencia a ejecutar
#### ```switch```
En lugar de escribir varios if-else, se puede utilizar ```switch```
```java
switch (expresion) {
  case condicion:
    codigo
  case condicion:
    codigo
  ...
  default:
    codigo
}
```
#### Bucle ```while```
```java
while ( condicion ) {
  //Sentencia
}
```
Los corchetes se pueden omitir si hay una única sentencia a ejecutar
#### Bucle ```for```
```java
for (inicio;fin;salto){
  codigo
}
```
#### ```do while```
```java
do {
  codigo
} while (condicion)
```

## Clases y objetos en Java
Las ***clases*** son una plantilla que posee atributos y métodos.

Los ***objetos*** possen un nombre y sin una instancia de una clase

**Forma general de una clase en Java:**
```java
class NombreDeLaClase {
  tipoDato variableDeInstancia1;
  tipoDato vablaDeInstancia2;
  ...

  tipoDato nombreMetodo1 (argumentos){
    //Cuerpo del metodo
  }
  ...
}
```
El ```tipoDato``` será el tipo de dato que devuelve el método pero si no devolviese ningún dato se pondría ```void```.

El operador ```this``` es una palabra reservada que hace referencia al propio objeto que se está ejecutando en el código. Se puede utilizar para acceder a los atributos y a los métodos del propio objeto.

## Encapsulamiento
El estado de un obketo está generalmente oculto y se conoce como encapsulamiento.

Java utiliza modificadores de acceso para definir estas características.
```java
modificador_acceso otros modificadores nombreMetodo( listaArgumentos )
```
Modificadores de acceso (son 4 pero hablaremos de 2):
+ ```public```: permite acceder sólo desde la misma clase al método o atributo marcado con este modificador
+ ```private```: permite acceder desde cualquier clase a cualquier método o atributo definido con este modificador

## Herencia en Java
La herencia permite representar comportamientos comunes de varias clases, evita la dubplicación de código.

La sintaxis para crear subclases es con la palabra ```extends```.

Todas las clases que no especifican de manera explícita un ```extends``` heredan de la clase Object.

La manera de llamar a los atributos y métodos de la clase de la cual heredamos es con ```super```

## JDBC
La API JDBC (Java Database Conectivity) es una API que permite la ejecución de de operaciones sobre bases de datos desde el lenguaje de programación Java.

Para utilizar JDBC es necesario:
1. Descargar el driver de la base de datos que utilizaremos
2. Agregar el driver a la classpath de la aplicación
3. Crear una clase Java:
  1. Registrar el driver JDBC
  2. Crear una conexion a la DB
  3. Crear un objeto ```statement``` (la sentencia)
  4. Ejecutar la secuencia SQL y procesarla
  5. Cerrar los objetos creados (```statement``` y la conexion)

Para poder conectarse al MySQL es necesario descargar dependencias. El proyecto de Java debe ser Maven y en "Project Files", el archivo "pom.xml" debe incluir:
```xml
    <dependencies>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.33</version>
        </dependency>
    </dependencies>
```
