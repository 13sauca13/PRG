--- Introducir valores (se ponen los atributos por el orden en el que se declararon)
INSERT INTO camino VALUES ('Francés',25,'13:00:25.00');

--- Para introducir un valor concreto o si los hay NULL hay que poner los campos que se van a introducir y después los valores por orden
INSERT INTO camino (nombre, nº_km_total, tiempo_total)
VALUES ('frances',125,'23:12:12')
  
--- Crear un atributo nuevo en una tabla del tipo int autoincrementable (empieza en 10 y sube de 2 en 2)
ALTER TABLE camino
ADD numero int IDENTITY(10,2);

--- Modificar el tipo de dato de un atributo ya existente de una tabla
ALTER TABLE camino
ALTER COLUMN nº_km_total int NOT NULL;

--- Introducir datos forzando un valor en un campo identidad
SET IDENTITY_INSERT camino ON
INSERT INTO camino (nombre,nº_km_total,tiempo_total,numero) VALUES ('chino',25,'12:12:12',11);

--- Crea una nueva tabla con los datos de los clientes de Madrid
SELECT * INTO clientes_madrid FROM clientes
WHERE población='Madrid'

--- Introduce en una nueva tupla datos de otra tabla, de la empresa de la calle Corrida forzando el CÓDIGOCLIENTE como ct50
INSERT INTO clientes_madrid
SELECT 'ct50', empresa, dirección, población, teléfono, responsable, historial FROM clientes
WHERE dirección like 'corrida%'
