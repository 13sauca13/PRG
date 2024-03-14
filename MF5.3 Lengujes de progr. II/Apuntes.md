# JAVA
:link:[Java API Clases](https://docs.oracle.com/javase/8/docs/api/)

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

### Variables
Para declarar una variable:
```java
tipo_dato nombre_variable;
```

Si la variable va a ser una constante (no podrá modificarse)
```java
final tipo_dato nombre_constante;
```

Existen 8 tipos de datos primitivos: (cualquier dato diferente a estos es una clase)
+ Enteros
  +  ```byte``` (1 byte): de -128 a 127
  +  ```short``` (2 bytes): -32768 a 32767
  +  ```int``` (4 bytes)
  +  ```long``` (8 bytes): los long necesitan el sufijo ```L```
+ Decimales:
  + ```float``` (4 bytes): máximo 6 o 7 decimales
  + ```double``` (8 bytes): máximo 15 decimales. los double necesitan el sufijo ```f```
+  ```boolean```
+  ```char```: caracteres, ***NO*** es string! (string es una clase en Java) Los ```char``` van entre comillas simples ```' '``` (los strings entre comillas dobles ```" "```)

