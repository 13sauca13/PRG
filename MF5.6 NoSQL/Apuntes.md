# NoSQL
**Not Only SQL**

Las bases de datos no relacionales ofrecen una arquitectura distribuida que permite almacenar información en casos en los que las bases de datos relacionales no son capaces de ofrecer el rendimiento y la escalabilidad necesarios.

 ACID:
 + Atomicidad
 + Consistencia
 + Isolation
 + Durabilidad

Las bases NoSQL no requieren in esquema fijo (son más fáciles de escalar), no soportan operaciones JOIN.

Hay distintos tipos:

| Tipo | DB | |
| --- | --- | --- |
| Documental | Mongo DB | Almacena clave/valor y el valor puede ser otra clave/valor. Los datos suelen estar almacenados como objetos binarios BSON o de texto JSON |
| Grafos | Neo4J | Usa estructuras de grafos para consultas semánticas y representa los datos como nodos, bordes y propiedades |
| Clave valor | Scalaris DB | Almacena clave:valor pero el valor es único (no como las documentales).Los datos suelen estar almacenados como objetos binarios |
| Multivalor | ADABAS | Pares clave/valor, solo que permiten almacenar múltiples valores asociados a una clave |
| Columnar | Cassandra | Cada columna se trata por separado. Los valores de bases de datos de una sola columna se almacenan de forma contigua. |
| Orientada a objetos | ZODB | DB optimizada para almacenar objetos en memoria |
| Tabular | Hbase | |
| Arrays | Rasdaman DB | Trabajan con datos multidimensionares en diferentes ejes |

## MongoDB
Las bases de datos de MongoDB son diccionarios clave:valor, de manera que las búsquedas y consultas se harán de esa manera: **clave:valor**

| Query | Uso |
| --- | --- |
| ```db.collection.find ( <query>, <projection>, <options> )``` | Selección o búsqueda de datos |
| ```db.collection.findOne ( <query>, <projection>, <options> )``` | Devuelve un único resultado |
| ```db.collection.find ( <query>, <projection>, <options> ).limit( <valor> )``` | Devuelve un número determinado de registros |
| ```db.collection.deleteOne ( <filter> )``` | Borra el primer valor que aparezca |
| ```db.collection.deleteMany ( <filter> )``` | Borra todos los valores |
| ```db.collection.insertOne ( <valores> )``` | Inserta un valor |
| ```db.collection,insertMany ( {<valores>}, {<valores>}, ...)``` | Inserta varios valores |
