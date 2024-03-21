# Buscar peliculas que hayan ganado algún premio e imprimir sólo el título
from pymongo import MongoClient
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://root:example@localhost:27017/')
filter={
    'awards.wins': 1
}
project={
    'title': 1
}
result = client['netflix']['movies'].find(
  filter=filter,
  projection=project
)

for i in result:
    print(i['title'])

#
