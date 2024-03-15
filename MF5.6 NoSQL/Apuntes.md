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
