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

--- Media de los artículos de deporte y cerámica
SELECT AVG(precio) AS media_precio, sección FROM productos
GROUP BY sección
HAVING sección='deportes' or sección='cerámica'

--- Cuantos clientes hay en cada población
SELECT count(códigocliente) AS número_clientes, población FROM clientes
GROUP BY población

--- Precio maximo de la seccion de confeccion
SELECT max(precio) AS [precio maximo], sección FROM productos
GROUP BY sección
HAVING sección='confección'

--- Todos los datos de los clientes de Madrid que hayan hecho pedidos
SELECT códigocliente,empresa,dirección,población,teléfono,responsable,historial FROM clientes INNER JOIN pedidos
ON clientes.códigocliente=pedidos.[código cliente]

--- Que persona ha pedido la muñeca andadora y en que fecha
SELECT responsable, convert(date, pedidos.[fecha de pedido]) FROM clientes INNER JOIN pedidos
ON clientes.códigocliente=pedidos.[código cliente]
INNER JOIN [productos- pedidos]
ON pedidos.[número de pedido]=[productos- pedidos].[número de pedido]
INNER JOIN productos
ON productos.códigoartículo=[productos- pedidos].[código artículo]
WHERE nombreartículo='muñeca andadora'

--- Como ha pagado Elvira Gomez y cuantas unidades ha comprado en el pedido del 1 de mayo de 2001
SELECT pedidos.[forma de pago], unidades, pedidos.[fecha de pedido] FROM [productos- pedidos] INNER JOIN pedidos
ON [productos- pedidos].[número de pedido]=pedidos.[número de pedido]
INNER JOIN clientes
ON pedidos.[código cliente]=clientes.códigocliente
WHERE responsable='Elvira Gómez' and pedidos.[fecha de pedido]='2001-05-01'
