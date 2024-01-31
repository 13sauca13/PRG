--- Para crear un usuario (con conexión y login):
create login sauca
with password='Minisdef01'must_change,
default_database=master, --- si la base no fuese esta se crearía sólo la conexión, no el usuario
check_expiration=on,
check_policy=on;

--- Si creamos el usuario en una db que no sea master, se crearía sólo la conexion, luego habria que crear el usuario de acceso:
create user sauca for login sauca;
