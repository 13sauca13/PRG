--- Nos aseguramos de que se va a ejecutar en la base de datos que queremos
use sauca
go

--- Creamos las tablas con los atributos y definimos cual es la clave primaria, las FK...
  
create table camino(
	Nombre nvarchar(15) not null,
	Km numeric(4,2) not null,
	Tiempo int not null,
	primary key (Nombre)
	);

create table etapas(
	Numero int not null,
	Km_parcial numeric(3,2) not null,
	Tiempo_estimado int not null,
	Loc_salida nvarchar(15) not null,
	Loc_llegada nvarchar(15) not null,
	Fk_Camino nvarchar(15) not null,
	primary key (Numero, Fk_Camino),
--- Ahora se dice cual de los atributos es la foreign key, de donde viene y las acciones para delete y update
	foreign key (Fk_Camino) references camino (Nombre) on delete cascade on update cascade
	);
