--- Buscar el valor del campo "responsable" en la tupla de la empresa "EL ESPAÑOLITO"
SELECT responsable FROM clientes
WHERE empresa='EL ESPAÑOLITO';

--- Más búsquedas y consultas...
SELECT códigocliente FROM clientes
WHERE población='Gijón';

SELECT nombreartículo, precio FROM productos
WHERE sección='cerámica';

SELECT nombreartículo, precio, sección FROM productos
WHERE sección='cerámica' or sección='deportes';

SELECT nombreartículo, precio, sección FROM productos
WHERE sección='deportes' and paísdeorigen='usa';

--- Operaciones con funciones
--- Seleccionar el nombre del articulo, el precio y el precio con 21% de IVA redondeado a 2 decimales y debe llamarse precio con iva, de los productos de Taiwan
SELECT nombreartículo, precio,convert(decimal(6,2),round(precio*1.21,2)) AS precio_con_IVA FROM productos
WHERE paísdeorigen='taiwán'
