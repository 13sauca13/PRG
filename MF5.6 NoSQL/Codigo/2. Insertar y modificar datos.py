# Insertar nuevos valores

from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
diccionario={"item": "card", "qty":15}
agregar= client["prueba"]["agregar"].insert_one(diccionario)

from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
diccionario=({"item": "prueba1", "qty":11}, {"item": "prueba2", "qty":22}, {"item": "prueba3", "qty":33})
agregar= client["prueba"]["agregar"].insert_many(diccionario)


# Modificar datos

# Actualizar la cantidad de "card" a 125
from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
buscar={"item":"card"}
actualizar={"$set":{"qty":125}}
agregar=client["prueba"]["agregar"].find_one_and_update(buscar,actualizar)

# Actualizar todas las cantidades a 125 y añade un campo llamado "size" en L
from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
buscar={}
actualizar={"$set":{"qty":125, "size":"L"}}
agregar=client["prueba"]["agregar"].update_many(buscar,actualizar)
