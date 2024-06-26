# Docker
Docker es una plataforma de código abierto para desarrollar aplicaciones, permite el despliegue de entornos independientes y aislados denominados **contenedores**.

Existen dos tipos de virtualización:
+ Nativa (Bare-Metal): se ejecuta directamente sobre el hardware físico del sistema sin necesidad de un sistema operativo anfitrión. El hipervisor (también conocido como VMM - Virtual Machine Monitor) se encarga de administrar los recursos del hardware y crear y administrar las máquinas virtuales
+ Hospedada (Hosted): Se ejecuta en un sistema operativo anfitrión y utiliza una capa de software adicional para crear y administrar las máquinas virtuales.

Las máquinas virtuales (VMs) se ejecutan a través de un hipervisor que crea y administra una capa de abstracción entre el hardware físico y el sistema operativo de la máquina virtual. El hipervisor se encarga de mular el hardware subyacente, incluyendo la CPU, la memoria, el almacenamiento y las interfaces de red, permitiendo que se ejecute un sistema operativo completo y aislado en cada máquina virtual. Cada VM tiene su propio kernel y sistema operativo, lo que significa que es posible ejecutar diferentes sistemas operativos y versiones en cada VM.

Los contenedores son una forma más ligera de virtualización que permite la ejecución de aplicaciones y servicios en un entorno aislado sin necesidad de un sistema operativo completo. En lugar de utilizar un hipervisor, los contenedores se ejecutan en una única instancia de sistema operativo que comparten los recursos de hardware del sistema anfitrión. Los contenedores utilizan la funcionalidad del kernel subyacente para crear un entorno aislado para cada aplicación, incluyendo el espacio de nombres, el control de recursos y la gestión de procesos. **Los contenedores no emulan el hardware**

## Servidor, contenedor y orquestador
Un **servidor** es una computadora o dispositivo que proporciona servicios y recursos a otros dispositivos o usuarios en una red.

Un **contenedor** es una unidad de software que encapsula una aplicación y todas sus dependencias en un paquete autónomo. El contenedor utiliza recursos del sistema operativo del host y se ejecuta aislado de otros contenedores, lo que permite que varias aplicaciones se ejecuten en el mismo host sin interferencias entre sí.

Un **orquestador** de contenedores es un software que se utiliza para gestionar y coordinar la implementación y ejecución de aplicaciones en contenedores en un conjunto de servidores.

## Docker
En Docker, hay tres componentes clave que se utilizan para crear, ejecutar y gestionar contenedores: el cliente Docker, el host Docker y el registro (registry) de Docker. El cliente Docker es la interfaz de línea de comandos (CLI) que se utiliza para interactuar con el demonio de Docker en el host. Este envía solicitudes al host Docker para crear, ejecutar, detener y eliminar contenedores, entre otras cosas. El cliente Docker se puede ejecutar en cualquier sistema operativo que sea compatible con Docker y se comunica con el host Docker a través de una API REST.

El host Docker es el motor de Docker que ejecuta los contenedores. Es responsable de crear, ejecutar y detener los contenedores, y proporciona aislamiento a nivel de sistema operativo para los contenedores. El host Docker utiliza el kernel del sistema operativo anfitrión para ejecutar los contenedores.

El registro de Docker (Docker Hub) es un repositorio centralizado de imágenes que permite a los usuarios compartir y distribuir imágenes de contenedores. Se pueden buscar y descargar imágenes desde el registro de Docker, lo que hace que sea más fácil y rápido trabajar con ellas. También es posible crear y subir imágenes personalizadas para su uso en proyectos individuales o compartidos.

![Docker](https://github.com/13sauca13/PRG/blob/master/Recursos/Docker_estructura.PNG)

### Dockerfile
Las imágenes de Docker se crean mediante un archivo Dockerfile. Se pueden usar una variedad de comandos dentro de estos archivos para definir la imagen de Docker que se creará.
| Comando | Uso |
| --- | --- |
| ```FROM``` | |
| ```RUN``` | |
| ```COPY``` o ```ADD``` | |
| ```WORKDIR``` | |
| ```CMD``` | |
| ```ENTRYPOINT``` | |
| ```ENV``` | |
| ```EXPOSE``` | |
| ```VOLUME``` | |

***************Completar

Cada capa es un conjunto de cambios que se aplican a la imagen base, y estas capas se apilan unas sobre otras para formar la imagen completa.
+ **Bootfs**
+ **Rootfs**
+ **Capas adicionales**

<hr/>

## Comandos Docker
| Comando | Explicación |
| --- | --- |
| ```docker --help``` | Muestra  una lista de comandos de Docker y sus opciones. |
| ```docker <comando> --help``` | Muestra información detallada sobre cómo usar un comando específico de Docker y sus opciones.|
| ```docker info``` |  Información detallada del sistema Docker que se está ejecutando en tu máquina. |
| ```docker run <options> <image> <command>``` | utiliza para crear y ejecutar un contenedor Docker a partir de una imagen de Docker existente. |
| ```docker ps``` | Muestra una lista de los contenedores en ejecución (con la opción ```-a``` muestra también los detenidos, con ```-l``` muestra info detallada) |
| ```docker images``` | Para mostrar una lista de imágenes de Docker en tu sistema y para gestionar y eliminar imágenes |
| ```docker rm``` | Para eliminar contenedores de Docker (```-f``` es para forzar) |
| ```docker stop``` | Detener contenedores de Docker de manera ordenada y puede ayudar a evitar la pérdida de datos y a garantizar la integridad del sistema. (se puede especificar un tiempo con ```-t```) |
| ```docker volume``` | |
| ```docker inspect``` | |
| ```docker cp``` | |
| ```docker stats``` | |
| ```docker logs``` | |
| ```docker history``` | |

### ```docker run```
```docker run <options> <image> <command>```

+ OPTIONS son las opciones que se pueden utilizar para configurar el contenedor Docker, como el puerto de exposición, las variables de entorno y la asignación de volúmenes.
  + ```-p local:contenedor```: Expone el puerto "contenedor" del contenedor en el puerto "local" del host
  + ```-it```: Interactivo, abre la consola con la máquina en cuanto el contenedor esté montado
  + ```--rm```: Borra el contenedor en cuanto se detenga
  + ```--name <nombre>```: Asigna al contenedor el nombre indicado
  + ```-d```: Ejecuta el contenedor en modo daemon, lo envía a segundo plano para liberar la shell
+ IMAGE es el nombre de la imagen de Docker a partir de la cual se creará el contenedor.
+ COMMAND y ARG... son los comandos y argumentos que se ejecutarán dentro del contenedor en cuanto se haya montado.

### ```docker exec```
Para ejecutar un comando en un contenedor se usa ```docker exec```

Abrir una consola de comandos con el contenedor se haría de la siguiente manera:
```sh
sudo docker exec -it ID_contenedor /bin/sh
```

### achivo docker-compose.yml
:link:[Awesome-compose GitHub](https://github.com/docker/awesome-compose)

Docker Compose es una herramienta que permite simplificar el uso de Docker. ***A partir de archivos YAML*** es mas sencillo crear contendores, conectarlos, habilitar puertos, volumenes, etc.
```yaml
services:
  frontend:
    image: nombre_imagen
    ports:
      - puerto_host:puerto_contenedor
    volumes:
      - ruta_host:ruta_contenedor
    configs:
      - httpd-config

  backend:
    image: nombre_imagen
    volumes:
      - ruta_origen:ruta_contenedor

volumes:
  db-data:
```

Teniendo el archivo "docker-compose.yml":
```
docker-compose up --build
```

## Ej. docker-compose para wordpress
```yaml
services:
  db:
    image: mysql:8.0.27
    command: '--default-authentication-plugin=mysql_native_password'
    volumes:
      - db_data:/var/lib/mysql #Al final del archivo se crea "db_data"
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=xx
      - MYSQL_DATABASE=xx
      - MYSQL_USER=xx
      - MYSQL_PASSWORD=xx
    expose:
      - 3306  #El puerto no está mapeado a ninguno de la máquina física por lo que no será accesible desde fuera.

  wordpress:
    depends_on:
     - db
    image: wordpress:latest
    ports:
      - 8080:80
    restart: always
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=xx
      - WORDPRESS_DB_PASSWORD=xx
      - WORDPRESS_DB_NAME=xx
    volumes:
      - wp-content:/var/www/html/wp-content

  phpmyadmin:
    image: phpmyadmin
    restart: always
    ports:
      - 6969:80
    environment:
      - PMA_HOST=db


volumes:
  db_data:
  wp-content:
```
## Ej. docker-compose para MongoDB
```yaml
services:
  mongo1:
    container_name: "mongo1"
    restart: always
    image: mongo:4.4.18
    ports:
      - 27017:27017
    environment:
      - "MONGO_INITDB_ROOT_USERNAME=root"
      - "MONGO_INITDB_ROOT_PASSWORD=example"
```

La herramienta ```mongorestore``` sirve para restaurar bases de datos:
```
mongorestore --host localhost --port 27017 --db netflix -u root -p example --dir /data/samples/mflix --authenticationDatabase=admin
```
El ```-u``` es el usuario, y el ```-p``` es la contraseña.
## Ej. docker-compose para neo4j
```yaml
services:
    neo4j:
      container_name: neo4j
      image: neo4j:latest
      ports:
        - 7474:7474
        - 7687:7687
      volumes:
        - ./conf:/conf
        - ./data:/data
        - ./import:/import
        - ../tmp/neo4j/logs:/logs
        - ./plugins:/plugins
      environment:
        - NEO4J_AUTH=none
```
