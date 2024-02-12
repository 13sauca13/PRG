USE sauca
GO

DECLARE @manoli INT
SET @manoli=45

IF (@manoli=45)
	BEGIN
		PRINT('Manoli tiene 45 años')
	END
ELSE
	BEGIN
		PRINT('Manoli es joven')
	END

--- Con dos variables máximo imprimir en pantalla 5 veces "Hoy es 12/02/2024"
DECLARE @fecha nvarchar(20)
SET @fecha=getdate()
DECLARE @i int
SET @i=0
WHILE (@i<5)
	BEGIN
		PRINT 'Hoy es ' + @fecha
		SET @i=@i+1
  END

/*
Con if y utilizando 3 variables necesito realizar el siguiente ejercicio:
La primera variable que permite caracteres unicode y de un tamaño de 17, su valor es "Hola, hoy es día "
La segunda variable, su valor es la fecha en la que el serrucho se insertó en la tabla
La tercera variable es el código del cliente de Oviedo
Si la variable de la fecha del serrucho es mayor que la fecha de hoy me tiene que aparecer por pantalla "Hola, hoy es día" y la fecha del serrucho en fomrato DIA/MES/AÑO
pero si no es así me tiene que aparecer "Hola, hoy es día", la fecha de hoy en formato DIA-MES-AÑO y "y el cliente con código" más el código del cliente de Oviedo más "no vende nada"
*/
DECLARE @mensaje1 nvarchar(17)
DECLARE @fecha_s datetime
DECLARE @cliente nvarchar(4)

SET @mensaje1='Hola, hoy es día '
SELECT @fecha_s=fecha FROM productos WHERE nombreartículo='serrucho'
SELECT @cliente=códigocliente FROM clientes WHERE población='oviedo'

IF (@fecha_s>getdate())
	BEGIN
		PRINT @mensaje1 + convert(nvarchar(10),@fecha_s,103)
	END
ELSE
	BEGIN
		PRINT @mensaje1 + convert(nvarchar(10),getdate(),105) + ' ' + @cliente + ' no vende nada'
	END

--- Hacer una funcion que me de la fomra de pago que hace cualquier cliente
CREATE FUNCTION forma_pago(@empresa nvarchar(25)) RETURNS TABLE
AS
RETURN (SELECT [forma de pago] FROM pedidos INNER JOIN clientes
	ON pedidos.[código cliente]=clientes.códigocliente
	WHERE empresa=@empresa);
