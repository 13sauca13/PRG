/*
###########             El diagrama de este ejercicio se encuentra en la suguiente dirección:             ###########
########### https://github.com/13sauca13/PRG/blob/master/Recursos/Relacional%20Camino%20de%20Santiago.PNG ###########
/*

--- Nos aseguramos de que se va a ejecutar en la base de datos que queremos
USE sauca
GO

--- Creamos las tablas con los atributos y definimos cual es la clave primaria y la FK
CREATE TABLE camino(
	nombre nvarchar(15) NOT NULL,
	nº_km_total numeric(4,2) NOT NULL,
	tiempo_total time NOT NULL,
	PRIMARY KEY (nombre)
	);

CREATE TABLE etapas(
	numero int NOT NULL,
	nº_km_parcial numeric(3,2) NOT NULL,
	t_estimado int NOT NULL,
	ciudad_salida nvarchar(15) NOT NULL,
	ciudad_llegada nvarchar(15) NOT NULL,
	fk_camino nvarchar(15) NOT NULL,
	PRIMARY KEY (numero, fk_Camino),
--- Ahora se dice cual de los atributos es la foreign key, de donde viene y las acciones para delete y update
	FOREIGN KEY (fk_camino) REFERENCES camino (nombre) ON DELETE CASCADE ON UPDATE CASCADE
	);

CREATE TABLE ciudad(
	nombre nvarchar(25) NOT NULL,
	comunidad nvarchar(15) NOT NULL,
	[codigo postal] int NOT NULL, --- Este campo va entre corchetes por el caracter especial (espacio) que contiene
	PRIMARY KEY (nombre)
	);

CREATE TABLE recorrido(
	fk_etapas_numero int NOT NULL,
	fk_etapas_camino nvarchar(15) NOT NULL,
	fk_ciudad nvarchar(25) NOT NULL,
	PRIMARY KEY (fk_etapas_numero,fk_etapas_camino,fk_ciudad),
	FOREIGN KEY (fk_ciudad) REFERENCES ciudad(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (fk_etapas_numero,fk_etapas_camino) REFERENCES etapas(numero,fk_camino) ON DELETE CASCADE ON UPDATE CASCADE
	);

CREATE TABLE albergue(
	nombre nvarchar(10) NOT NULL,
	capacidad int NOT NULL,
	precio money NULL,
	fk_ciudad nvarchar(25) NOT NULL,
	PRIMARY KEY (nombre),
	FOREIGN KEY (fk_ciudad) REFERENCES ciudad(nombre) ON DELETE CASCADE ON UPDATE CASCADE
	);

CREATE TABLE peregrino(
	[nº identificacion] int NOT NULL,
	nombre nvarchar(50) NOT NULL,
	calle nvarchar(20) NULL,
	numero int NULL,
	piso varchar(4) NULL,
	PRIMARY KEY ([nº identificacion])
	);

CREATE TABLE [camino realizado](
	fk_ciudad nvarchar(25) NOT NULL,
	fk_peregrino int NOT NULL,
	fecha date NOT NULL
	PRIMARY KEY (fk_ciudad,fk_peregrino,fecha),
	FOREIGN KEY (fk_ciudad) REFERENCES ciudad(nombre) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (fk_peregrino) REFERENCES peregrino([nº identificacion]) ON DELETE CASCADE ON UPDATE CASCADE
	);
