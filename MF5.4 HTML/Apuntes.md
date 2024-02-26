# HTML
Los enlaces de los ejercicios de esta asignatura NO están en GitHub para que puedan ser visializados en el navegador y no sólo sean código:

:mag:[Ejercicios](https://spaces.w3schools.com/space/e2t-sauca)

>[!IMPORTANT]
>[HTML W3 Schools](https://www.w3schools.com/html/)

HTML es un lenguaje de marcado para páginas web. La estructura básica de un fichero HTML es la siguiente:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Titulo de la página</title>
  </head>
  <body>
    Cuerpo de la página
  </body>
</html>
```

+ ```<!DOCTYPE html>``` Indica que es un archivo HTML5
+ ```<html>``` Es el elemento raiz de la página
  + ```<head>``` Contiene informacion sobre la página
    + ```<title>``` Especifica el título de la página (se verá en la pestaña del navegador)
  + ```<body>``` Define el cuerpo del documento, contiene todos los elementos visibles como cabeceras, párrafos, imágenes, enlaces, tablas, listas...

Cada etiqueta se abre y posteriormente se cierra con ```</etiqueta>``` (***Excepto ```<br/>``` y ```<img ... />***)

Para introducir comentarios en el código se utiliza:
```
<!-- Comentarios -->
```

## 1.Formato de contenido
Para dar fomato al texto podemos utilizar:
+ **Encabezados**: ```<hX> Texto </hX>``` siendo x un número del 1 al 6 (tiene jerarquía. 1 es la más alta y 6 la más baja)
+ **Párrafos**: ```<p> Texto del párrafo </p>```
+ **Listas**: Hay dos tipos:
  + Ordenadas: ```<ol> <li>Elemento</li> <li>Elemento2</li>... </ol>``` (cada elemento de la lista va numerado)
  + Desordenadas: ```<ul> <li>Elemento</li> <li>Elemento2</li>... </ul>``` (lista de "puntos")

### Enlaces
```
<a href="ruta_enlace">Texto mostrado</a>
```
A los enlaces se les puede añadir también ```target="atributo"``` para especificar como se abrirá el enlace:
+ ```_blank```	Abre en una nueva ventana o pestaña (según el navegador)
+ ```_self```	Abre en la misma pestaña en la que se pulsó (esta es la opción por defecto)
+ ```_parent```	Abre en la ventana padre
+ ```_top```	Abre en una ventana completa

### Imágenes
Para introducir imágenes se utiliza la etiqueta:
```
<img src="ruta_imagen"/>
```
