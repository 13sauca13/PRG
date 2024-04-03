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

Si la variable va a ser una constante (no podrá modificarse)
```java
final tipo_dato nombre_constante;
```

Para introducir datos por parte del usuario existen dos clases:
+ ```scanner```
+ ```JOptionPane```
  
Existen 2 tipos de datos en Java: Primitivos y Referenciados.

#### Tipos primitivos
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

#### Tipos referenciados (tipo object)
Son:
+ Clases
  + ```string``` (la comparación de strings se hace con ```equals```)
+ Interfaces
+ Arreglos (*arrays*)
##### Arrays
```tipo_dato nombre_array [] = new tipo_dato [long_array]```

Para introducir datos se utiliza el índice o se rellena entero:
+ ```nombre_array[indice] = valor```
+ ```tipo_dato nombre_array[] = {valor,valor2...}```

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
