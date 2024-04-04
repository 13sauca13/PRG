# Conexion a una base de datos de peliculas de MongoDB con python creando paginas web con Flask de manera automatica

# Importamos flask y render_template
from flask import Flask, render_template
# Importamos MongoClient
from pymongo import MongoClient
# Para poder coger la Id de la pelicula hay que darle formato
from bson.objectid import ObjectId

# La función Conexion conecta con la base da datos, a la db "netflix" y a una tabla concreta
def conexion():
    tabla="movies"
    db=MongoClient('mongodb://root:example@localhost:27017/')["netflix"][tabla]
    return db

# Creamos una instancia de Flask llamada Web_Pelis
Web_Pelis=Flask("web")

# El decorador @Web_Pelis.route recibe un string con la ruta del servidor que queremos enrutar, a continuación la función decorada
@Web_Pelis.route("/")
def index():
    # La variable busqueda contiene una lista de la base de datos de todos los generos (sin repetir)
    busca = conexion().distinct("genres")
    # Servimos la web "index" de la carpeta templates
    return render_template("index.html",busqueda=busca)


@Web_Pelis.route("/pelis/<genero>")
def peliculas(genero):
    filtro={"genres": genero}
    project={"title": 1}
    busca = conexion().find(filter=filtro,projection=project)
    return render_template("pelis.html",chumino=genero,busqueda=busca)

@Web_Pelis.route("/pelicula/<peliculilla>")
def pelicula(peliculilla):
    filtro={"_id": ObjectId(peliculilla)}
    busca = conexion().find(filter=filtro)
    return render_template("pelicula.html",busqueda=busca,peliculilla=peliculilla)


# Llamamos al método "run" de nuestra instancia y le decimos que escuche en el puerto 8080
# Activando el "debug", al guardar un cambio el servidor se reinicia solo
Web_Pelis.run(port=8080, debug=True)
