![Ejercicio corrupcion](https://github.com/13sauca13/PRG/blob/master/Recursos/Ejercicio%20corrupcion.png)

| ENTIDAD | ATRIBUTOS (PK en negrita, * = NULL |
| --- | --- |
| **JUEZ** | (***Nombre***, Dirección*, Fecha_nacimiento*, Fecha_comienzo*) |
| **CASO** | (***Código***, Nombre*, Descripción, Millones*, Dictamen*, FK_Juez, FK_Periódico, Fecha) |
| **CIUDADANO** | (***DNI***, Nombre, Dirección*, Patrimonio*, FK_Partido*) |
| **IMPLICADO** | (***FK_Caso***, ***FK_Ciudadno***, Cargo_ppal) |
| **PERIÓDICO** | (***Nombre***, Dirección*, Tirada*, FK_Partido*) |
| **PARTIDO** | (***Nombre***, Dirección*, Teléfono) |
| **TELÉFONOs** | (***FK_Partido***, ***Teléfono***) |
