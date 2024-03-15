# HTML

> :book:[**Libro de Javascript EEAE**](https://github.com/13sauca13/PRG/blob/master/Recursos/Javascript.pdf)

<hr>

:mag:[Ejercicios](https://github.com/13sauca13/PRG/tree/master/MF5.4%20HTML/Codigo)

NO pueden verse en formato web desde ahí. Hay otro repositorio con GitHub Pages para visualizar los resultados:

:link:[Ejercicios en vista web](https://13sauca13.github.io/E2T-HTML/)

>[!IMPORTANT]
>[HTML W3 Schools](https://www.w3schools.com/html/)

HTML es un lenguaje de marcado para páginas web. La estructura básica de un fichero HTML es la siguiente:
```html
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

Cada etiqueta se abre y posteriormente se cierra con ```</etiqueta>``` (***Excepto ```<br/>``` y ```<img ... />```** y alguna más)

Para introducir comentarios en el código se utiliza:
```html
<!-- Comentarios -->
```

>[!TIP]
>Todas las etiquetas pueden tener un ```id``` para poder referenciarlas en los estilos o en caso de ser necesario pero los is deben ser únicos:
>```
><etiqueta id="nombre_id"> contenido </etiqueta>
>```

## 1.Formato de contenido
Para dar fomato al texto podemos utilizar:
+ **Encabezados**: ```<hX> Texto </hX>``` siendo x un número del 1 al 6 (tiene jerarquía. 1 es la más alta y 6 la más baja)
+ **Párrafos**: ```<p> Texto del párrafo </p>```
+ **Listas**: Hay dos tipos:
  + Ordenadas: ```<ol> <li>Elemento</li> <li>Elemento2</li>... </ol>``` (cada elemento de la lista va numerado)
  + Desordenadas: ```<ul> <li>Elemento</li> <li>Elemento2</li>... </ul>``` (lista de "puntos")

### Enlaces
```html
<a href="ruta_enlace">Texto mostrado</a>
```
A los enlaces se les puede añadir también ```target="atributo"``` para especificar como se abrirá el enlace:
+ ```_blank```	Abre en una nueva ventana o pestaña (según el navegador)
+ ```_self```	Abre en la misma pestaña en la que se pulsó (esta es la opción por defecto)
+ ```_parent```	Abre en la ventana padre
+ ```_top```	Abre en una ventana completa

### Imágenes
Para introducir imágenes se utiliza la etiqueta:
```html
<img src="ruta_imagen"/>
```

### Tablas
Para crear una tabla se usa la etiqueta ```<table>```:
```html
<table>
  <tr>
    <th>Cabecera_columna1<th>
    <th>Cabecera_columna2<th>
    ...
  </tr>
  <tr>
    <td>Contenido</td>
    <td>Contenido</td>
    ...
  </tr>
  ...
</table>
```
Cada ```<tr>``` tendrá una fila de la tabla (*Table Row*), la primera tendrá dentro ```th```, cabeceras (*Table Header*) y las siguientes ```td``` (*Table Data*).

Para combinar celdas se usa dentro de la etiqueta de la primera celda el atributo ```colspan=x``` siendp x el número de celdas en adelante que se combinarán o ```rowspan``` para combinar filas.
### ```<hr/>```
*Horizontal Rule*, introduce una raya horizontal
### ```<pre>```
Lo que esté dentro de la eqtiqueta ```<pre>``` se considera que viene preformateado y HTML no le hará nada.

Se utiliza para introducir bloques de código.

### ```<div>```

## 2.CSS
El CSS se usa para controlar el estilo de las páginas sin tener que usarlo en el propio HTML. CSS se puede usar de tres formas:
#### En linea
En la propia línea de HTML:
```html
<etiqueta style="propiedad:valor";> contenido </etiqueta>
```

#### Interno
Desde ```<head>``` para aplicar a lo largo de la página:
```html
<head>
  <style>
    .nombre_estilo {
        propiedad:valor;
        propiedad2:valor2;
        ...
    }
  </style>
</head>
```
El nombre del estilo sería ```.nombre_estilo``` para crear una clase de estilo o pueden utilizarse sin ```.``` si se va a utilizar una etiqueta existente de HTML (o varias) o para un id (utilizando ```#nombre_id```) para modificar su estilo por defecto:
```html
<head>
  <style>
    etiqueta, etiqueta2... {
        propiedad:valor;
        propiedad2:valor2;
        ...
    }
  </style>
</head>
```

Para aplicar el estilo (de los que no modifican las propias etiquetas): ```<etiqueta class="nombre_estilo"> contenido </etiqueta>```

#### Externo
Desde un archivo externo con la extensión .css. De esta manera podríamos tener una hoja de estilo común para todas las páginas de una web.
```html
<head>
    <link href="nombre_archivo.css" rel="stylesheet"/>
</head>
```

### Usos
:link:[Regla ```!important```](https://www.w3schools.com/Css/css_important.asp)

:link:[Media Queries](https://www.w3schools.com/css/css3_mediaqueries.asp)

## 3.Frameworks CSS
Un framework es una plantilla para desarrollar software.

Usaremos [**Bootstrap**](https://getbootstrap.com/)
