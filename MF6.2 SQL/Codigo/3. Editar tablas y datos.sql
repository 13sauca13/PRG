--- Introducir valores (se ponen los atributos por el orden en el que se declararon)
INSERT INTO camino VALUES ('Francés',25,'13:00:25.00');

--- Crear un atributo nuevo en una tabla del tipo int autoincrementable (empieza en 10 y sube de 2 en 2)
ALTER TABLE camino
ADD numero int IDENTITY(10,2);

--- Modificar el tipo de dato de un atributo ya existente de una tabla
ALTER TABLE camino
ALTER COLUMN nº_km_total int NOT NULL;
