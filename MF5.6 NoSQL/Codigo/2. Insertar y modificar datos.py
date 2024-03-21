# Insertar nuevos valores

from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
diccionario={"item": "card", "qty":15}
agregar= client["prueba"]["agregar"].insert_one(diccionario)

from pymongo import MongoClient
client = MongoClient('mongodb://root:example@localhost:27017/')
diccionario=({"item": "prueba1", "qty":11}, {"item": "prueba2", "qty":22}, {"item": "prueba3", "qty":33})
agregar= client["prueba"]["agregar"].insert_many(diccionario)
