# Transformación Digital de la Armada

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

## Estrategia Cloud

## Computación en la nube

## Virtualización ligera

## 5G
