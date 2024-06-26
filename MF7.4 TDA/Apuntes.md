# Transformación Digital de la Armada

:mag:[Codigo de las prácticas](https://github.com/13sauca13/PRG/tree/master/MF7.4%20TDA/Codigo)

## Blockchain
Bitcoin utiliza la tecnología blockchain, que a su vez en un tipo de DLT (Distributed Ledger Technology).

### DLT
La DLT, Tecnología de Registro Distribuido es una combinación de:
+ Redes P2P:
  + Red de ordenadores que se comportan como pares entre si. No hay harware central ni servidor.
  + Están conectados de manera que comparten el registro y la validación de la información del sistema.
+ Almacenamiento de datos distribuido
  + Se comparte el registro entre todos los nodos, no hay un registro centralizado.
  + Es necesario definir el nivel de informacion del registro y los participantes con permiso para leer y escribir.
+ Criptografía
  + La encriptacion permite que solo ciertos participantes tengan acceso a detalles de la transacción y mantener la privacidad.
  + Proceso de verificación o criptografía asimétrica.
    + Mensaje + clave pública = Mensaje cifrado
    + Mensaje encriptado + clave privada = Mensaje descifrado
    + Mensaje + clave privada = Mensaje firmado
    + Mensaje firmado + clave pública = Autenticación

 El funcionamiento de DLT es mediante participantes o nodos y cada nodo posee una copia del registro, al proponer una transaccion se envia a la red y se espera la verificacion, TODOS los nodos de la red reciben los detalles de la transaccion. Todos los nodos de la red verifican la transaccion antes de que se registre  mesiante un protocolo de consenso. Una vez alcanzado el consenso se registra en el libro distribuido (en todos los nodos)

 Una vez registrada una transacción nno se puede alterar, las entradas del registro son inmutables.

 Al registrarse todas las transacciones de manera secuencial e inmutable se pueden rastrear y verificar las transacciones historicas de manera eficiente.

>[!TIP]
>**Blockchain es una DLT con una particularidad:**
>
>Agrupa el registro en bloques y cada bloque se cierra con una firma criptografica llamada hash, este hash será también la apertura del siguiente bloque

### Token
Un token es un activo digital, es decir, “algo” que tiene un valor en un contexto determinado y que sólo es válido en ese universo. Representa cualquier activo negociable y fungible.

Existen diversos tipos de token:
+ Security Token: Estos son similares a cualquier otro token conocido, pero vinculados a los security (valores) tradicionales y sus características.
+ Utility Token: Son «fichas» de aplicación. Permiten el acceso futuro a los productos o servicios ofrecidos por una empresa. Por lo tanto, no se crean para ser una inversión.
+ Equity Token: Representan la propiedad de algún activo o empresa de terceros. Además, su valor está asociado al éxito o fracaso de dicha propiedad.

También hay diversos estándares para los token:
+ ERC-20: se trata del estándar más popular. Son tokens fungibles (es decir que se pueden intercambiar entre ellos) e implementan una API para su desarrollo a través de smart contracts.
+ ERC-721: es el estándar más utilizado para la creación de NFT. Este estándar permite implementar características únicas a cada unidad, haciendo que sean únicos y no se puedan cambiar por otro.
+ ERC-1155: Se trata de un tipo de token que puede mezclar las características de los tokens ERC-20 y de los ERC-721.

## Computación cuántica
La computacion cuantica es un nuevo paradigma de programacion que se basa en los principios de la mecanica cuantica.

Tendrá alto impacto en el sector científico, industrial y militar:
+ Velocidad de proceso
+ Criptoanálisis
+ Criptografía
+ Comunicacion
+ Generacion de numeros aleatorios
+ Simulacion de procesos cuanticos

**Buscar 10 elementos de impacto en la industria militar de la computacion cuantica**

### Antecedentes
+ El átomo de Bohr: Un electrón emite o absorbe energía discreta en forma de cuantos (fotón) COMPLETAR!!!!!*******************************
+ Superposición cuántica: *************************************
+ Entrelazamiento cuántico: Existencia de partículas que están conectadas entre si.
+ Dualidad onda-partícula: Se pensaba que las ondas y las partículas eran cosas distintas, después se descubrió que la luz se comporta como onda en ocasiones y como partículas en otra.

### QuBits
Con toddo esto, en lugar de trabajar con voltajes eléctricos se trabaja a nivel de **cuanto**:
+ cantidad mínima de energía que es susceptible de transmisión a través de una longitud de onda.
+ Un qubit puede representar un 0, un 1 o ambos al mismo tiempo (superposición)

Mientras mayor sea el número de qubits utilizados, el número de Universos posibles para hacer una operación en cada uno también aumenta:  (siendo L es el número de qubits)

$Universos=2L$

Cuando se captura un átomo se aprovecha el spin del lso electrones y según apunte hacia arriba o abajo representará un 0 o 1 (aunque hay valores infinitos entre cada uno). De esta manera si generásemos nuevas dimensiones con cada qubit superpuesto y cada una de estas dimensiones guardara un valor. Un equipo con X qubits tendrá X dimensiones, pero en nuestro mundo de 3 dimensiones lo veremos superpuesto.

#### Entrelazamiento
Se produce entre un grupo de electrones y les permite sincronizar su orientación de Spin (estado). Cuando cambiamos el Spin de una de ellas de forma aleatoria, la otra cambia automáticamente esté donde esté y sin que haya ningún canal de información de por medio.

Esto resulta útil para mediciones precisas y envío seguro de información. 

#### Puertas lógicas cuánticas
Son representadas mediante matrices unitarias y operan en espacios de uno o dos qubits.

Mientras en un ordenador clásico una operación toma un valor binario de entrada y genera un resultado, en un computador cuántico, todas las posibles combinaciones se hacen a la vez, en paralelo.

#### Algoritmos y protocolos
+ Algoritmo de Grover: enrutamiento y búsquedas en bases de datos no indexadas.
+ Algoritmo de Shor: factoriza números enteros. Peligroso para criptografías de clave pública, puede descomponer la clave en 2 números primos(RSA)
+ Protocolo BB84: protocolo de criptografía.
+ Protocolo de teletransporte cuántico: protocolo de transmisión de información cuántica de una posición a otra sucientemente alejada, incluso sin canal

## Estrategia Cloud
La nube son servidores, software y bases de datos diseñados para entregar recursos como procesamiento, almacenamiento, red, escalabilidad y aplicaciones.

Existen diferentes modelos de implementación en la nube:
+ Nube pública o compartida: Entorno de nube que parte de una infraestructura de TI ajena al usuario final. Es compartida por múltiples clientes.
+ Nube privada: La infraestructura se destina a un único cliente con acceso completamente aislado. Existen dos subtipos:
  + Nubes privadas gestionadas: los clientes solo crean y usan la nube
  + Nubes exclusivas: Una nube dentro de otra nube
+  Nube híbrida: Combina nubes públicas y nubes privadas (el cliente suele alojar aplicaciones críticas en sus servidores y secundarias en un proveedor de nube)
+  Multicloud: Compuesto por al menos dos servicios de nube que proporcionan al menos dos proveedores de nube pública o privada

Modelos de servicios en la nube
+  Software-as-a-service: Software por suscripción
+  Platform-as-a-service: Para desplegar y desarrollar aplicaciones
+  Infraestructure-as-a-service: Los proveedores

La conexión a la nube se puede realizar mediante:
+ API: Interfaces de programación de aplicaciones para conectar los datos, las aplicaciones y los dispositivos.
+ Puerta de enlace de API: filtra y distribuye el tráfico entrante entre el cliente y los servicios.
+ VPN

### Opciones de migración a la nube (Las 6R según Gartner)
![Las 6R](https://github.com/13sauca13/PRG/blob/master/Recursos/Las%206R.PNG)
#### Realojar (lift-and-shift)
Migrar sistemas tal y como están a la nube
1. Seleccionar un proveedor IaaS
2. Reproducir la arquitectura en esa infraestructura
#### Refactorizar
Reescribir el código y los marcos de trabajo ya existentes para aprovechar la nube.

Ejecutarán sus aplicaciones en la plataforma de un proveedor de PaaS (Plataforma como servicio).
#### Re-purchase
Pago por uso. Se compran aquellas licencias (SaaS) que se usan en función de la finalidad que se le dará.

Ahorro en infraestructura.
#### Replatform
Rediseñar la plataforma que se está usando.

Requiere un análisis de negocio previo.
#### Retener
Mantener aplicaciones en su estado actual, sin nube.
#### Retirar
Eliminar aplicaciones obsoletas.

### Beneficios y dificultades
Beneficios:
+ Rendimiento: agilidad y eficiencia en la gestión de recursos informáticos.
+ Escalabilidad: ampliación para soportar picos de trabajo.
+ Flexibilidad: Acceso a la nube desde cualquier lugar.
+ Coste: Menos infraestructura física y gastos operativos.
+ Seguridad: recuperación ante desastres y medidas de seguridad avanzadas.

Dificultades:
+ Migrar grandes bases de datos: alto coste de tiempo y complejidad. Integridad de los datos.
+ Operatividad continuada: disponibilidad durante el paso a la nube.
+ Capacitación y formación: la capacitación de los usuarios finales es crucial. Falta de trabajadores sector cloud.
+ Privacidad de los datos y amenazas online

## Computación en la nube

## Virtualización ligera
La virtualización es la tecnología que permite utilizar un programa (software) para imitar las características físicas (hardware) de otra computadora o de un conjunto de computadoras, lo que da lugar a un sistema informático virtual.

Existen diferentes tipos de virtualización:
+ Virtualización del sistema operativo
+ Virtualización del servidor
+ Virtualización de almacenamiento
+ Virtualización de red
+ Virtualización gráfica
+ Virtualización de aplicaciones
+ Virtualización de perfil
+ Virtualización de escritorios

### Virtualización de contenedores
La virtualización a nivel de sistema operativo, también llamada virtualización basada en contenedores.

Sobre el núcleo del sistema operativo de la máquina anfitriona se ejecuta una capa de virtualización que permite que existan múltiples instancias aisladas de espacios de usuario (contenedor)

Un contenedor es un conjunto de procesos aislados, que se ejecutan en un servidor:
+ acceden a un sistema de ficheros propio.
+ tienen una configuración de red propia.
+ accede a los recursos del host (memoria y CPU)

Existen diferentes tipos de contenedores:
+ Contenedores de Aplicaciones: Se suelen utilizar para despliegue de aplicaciones web (Docker, Podman...)
  + Aplicaciones web desplegadas en contenedores: Se usa un esquma multicapa (cada servicio se despliega en un contenedor) Lo que mejor se adapta son los microservicios
+ Contenedor de Sistemas: El uso que se hace de ellos es muy similar al que hacemos sobre una máquina virtual: se accede a ellos (por ssh), se instalan servicios, se actualizan, ejecutan un conjunto de procesos



## 5G
El 5G es la quinta generación de tecnologías móviles de comunicaciones.

