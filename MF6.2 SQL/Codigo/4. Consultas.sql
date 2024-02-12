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

--- Los articulos y la cantidad de cada uno que ha pedido Angel Martinez
SELECT sum([productos- pedidos].unidades) AS cantidad, productos.nombreartículo FROM productos INNER JOIN [productos- pedidos]
ON productos.códigoartículo=[productos- pedidos].[código artículo]
INNER JOIN pedidos
ON [productos- pedidos].[número de pedido]=pedidos.[número de pedido]
INNER JOIN clientes
ON pedidos.[código cliente]=clientes.códigocliente
WHERE responsable='Angel Martínez'
GROUP BY productos.nombreartículo

--- Cuantos meses hace que esta en la base de datos el correpasillos
SELECT datediff(MM, productos.fecha, getdate()) FROM productos
WHERE nombreartículo='correpasillos'

--- Necesito saber el nombre y la seccion de todos los productos superiores a la media
SELECT nombreartículo, sección FROM productos
WHERE precio>(SELECT AVG(precio) FROM productos)

--- Consulta que devuelva los articulos de precio superior a todos los articulos de ceramica
SELECT nombreartículo FROM productos
WHERE precio>ALL(SELECT precio FROM productos WHERE sección='cerámica')

--- Nombre y precio de los productos de los que se hayan pedido mas de 20 unidades
SELECT nombreartículo, precio FROM productos
WHERE códigoartículo in (SELECT [código artículo] FROM [productos- pedidos] WHERE unidades>20)

--- Que clientes no han pagado con tarjeta o no han realizado pedidos
SELECT códigocliente, empresa, responsable FROM clientes
WHERE códigocliente in (SELECT [código cliente] FROM pedidos WHERE [forma de pago]!='tarjeta')
or códigocliente not in (SELECT [código cliente] FROM pedidos)

--- Necesito saber las empresas que hay pedido la consola de video, el numero de pedido que ha hecho cada empresa y las unidades de la consola que han pedido en cada uno
SELECT empresa, pedidos.[número de pedido], [productos- pedidos].unidades  FROM clientes INNER JOIN pedidos
ON clientes.códigocliente=pedidos.[código cliente]
INNER JOIN [productos- pedidos]
ON pedidos.[número de pedido]=[productos- pedidos].[número de pedido]
INNER JOIN productos
ON [productos- pedidos].[código artículo]=productos.códigoartículo
WHERE nombreartículo like 'consola %'

--- Saber los clientes de madrid con pedidos y sin pedidos
SELECT clientes.códigocliente, count([código cliente]) AS pedidos FROM pedidos RIGHT JOIN clientes
ON pedidos.[código cliente]=clientes.códigocliente
WHERE población='madrid'
GROUP BY clientes.códigocliente
