# Diseño Web

Spring Boot es un framework de Java de código abierto que se utiliza para crear microservicios.

Sin Spring habría que crear el proyecto con Maven o Gradle y descargar las dependencias necesarias y posteriormente configurarlas en ficheros XML. Spring Boot lo realiza de manera automática para simplificarlo mediante el [Spring Initializr](https://start.spring.io).

En esta asignatura usaremos 4 dependencias:
+ ***SPRING DEV TOOL***: Nos permite reiniciar más facilmente aplicaciones en tomcat
+ ***LOMBOK***: Nos permite reducir código como pueden ser los métodos get y set.
+ ***SPRING WEB***: Permitiendo crear aplicaciones de tipod rest y aplicaciones web utilizando spring mvc.
+ ***THYMELEAF***: Para agregar paginas web de manera más simple, asi no tendremos que usar jsp’s.

## Spring y NetBeans
Es necesario descargar el plugin de NetBeans para Spring ([NB Springboot](https://plugins.netbeans.apache.org/catalogue/?id=4)). Una vez instalado ya es posible crear proyectos de Java con Spring Initializr.

Una vez creado el proyecto de "Java with Maven/Spring Boot Initializr project" es necesario hacer un "Clean and Build"  para descargar los modulos y refrescar las dependencias.

El proyecto creado tendra una clase NombreProyectoApplication.java, esta clase también se crea de forma automática y contiene un método MAIN y el metodo run. Contiene la anotacion de @SpringBootApplication y nos permitirá ejecutar nuestras aplicaciones de spring.

Si ejecutamos nuestra aplicación veremos:

![Output Spring](https://github.com/13sauca13/PRG/blob/master/Recursos/Output%20Spring.png)

Podemos ver en ese log:
+ El puerto en el que está nuestra aplicación (```Tomcat initialized with port 8080 (http)```)
+ La ruta de la aplicación (```Tomcat started on port 8080 (http) with context path```)
+ Confirmar que la aplicación está corriendo (```Started HolaSpringApplication in 2.086 seconds (process running for 2.469)```)


### Estructura de los paquetes
La estructura de paquetes del programa será la siguiente:
+ com.eeae.HolaSpring
+ com.eeae.HolaSpring.dao
+ com.eeae.HolaSpring.domain
+ com.eeae.HolaSpring.servicio
+ com.eeae.HolaSpring.web
