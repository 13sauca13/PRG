:link: [1ª Parte - Adrian](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Apuntes.md#big-data)

:link:[2ª Parte - Marcos](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Apuntes.md#fundamentos-de-big-data)

:link:[3ª Parte - Virginia](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Apuntes.md#tipolog%C3%ADa-captura-y-preparaci%C3%B3n-de-los-datos)

# Big Data

+ :monocle_face: [Preguntas tipo test](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Preguntas.md)
  + :link:[Preguntas 1ª Parte](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Preguntas.md#preguntas-adrian) - ```adriancarballal@gmail.com```
  + :link:[Preguntas 2ª Parte](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Preguntas.md#preguntas-marcos) - ```mgestal@udc.es```

:book:[Presentacion Adrian Carballal](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Big%20Data%20E2T.pdf)

## Qué es el big data?
El Big Data son volúmenes de datos masivos que no pueden ser tratados mediante técnicas convencionales:
+ Captura
+ Transferencia
+ Almacenamiento
+ Gestión/mantenimiento/consulta
+ Análisis
+ Visualización

Algo se considera Big Data si cumple las 5 V:
+ Volumen: Se refiere a la gran cantidad de datos que se manejan (del orden de petabytes o exabytes)
+ Variedad: Agregar datos de gran variedad de fuentes (datos desestructuraados y con diferentes formas que no pueden tratarse con DB relacionales normales)
+ Velocidad: Enorme velocidad en la generación, recogida y proceso de la información
+ Veracidad: Se debe analizar inteligentemente un gran volúmen de datos con la finalidad de obtener información verídica y útil
+ Valor: Es la creación de una ventaja competitiva al identificar y procesar datos claves

**Data Warehouse**: Es un almacén de datos creado con el fin de permitir la toma de decisiones en la organización.
En el caso del Big Data, la solución es al mismo tiempo un almacén de datos, una tecnología de proceso, análisis y visualización de datos.

Con la acumulación de datos la minería busca información concreta, sin embargo en el Big Data es necesario saber organizar, refinar y convertir en información relevante. Los datos sólo tienen valor potencial, es su análisis y sistematización el que permite obtener ventajas.

### Los 7 perfiles profesionales del Big Data
+ Chief Data Officer (CDO): Responsable de asegurar que la organización es data driven
+ Data Scientists: Son los miembros clave del equipo de ciencia de datos. Permiten extraer conocimiento e información de los datos.
+ Citizen Data Scientist
+ Data Engineer
+ Data Steward
+ Business Data Analyst
+ Data Artist

>[!TIP]
>Riesgos en el análisis de datos
>Uno de los riesgos que presenta la búsqueda de información en el Big Data es el descubrimiento de patrones no significativos. Estos patrones se conocen como *principios de Bonferroni*.

### Analisis de la información
El Data Mining emplea técnicas interdisciplinares en entornos de procesamiento distribuido:
+ Redes de neuronas artificiales (ANN/DL)
+ Árboles de decisión
+ Regresión (simple/múltiple)
+ Redes Bayesianas
+ Support Vector Machines

Los modelos predictivos evalúan que probabilidad tiene un individuo de mostrar un comportamiento específico en el futuro buscando patrones discriminadores en los datos para responder al comportamiento y realizan cálculos en tiempo real para evaluar un determinado riesgo u oportunidad a fin de orientar una decisión adecuada.

## El dato como activo de valor
COMPLETAR

## Convertir datos en conocimiento
Aprender es:
+ Adquirir conocimiento
+ Desarrollar habilidades a través de instrucción y práctica
+ Organización del conocimiento
+ Descubrimiento de hechos...

De la misma forma el **MACHINE LEARNING** estudia y modela computacionalmente los procesos de aprendizaje en sus diversas manifestaciones

### Aprendizaje computacional
+ **Aprendizaje genético:** Aplica algoritmos inspirados en la teoría de la evolución para encontrar descripciones generales a conjuntos de ejemplos.
+ **Aprendizaje conexionista:**  Busca descripciones generales mediante el uso de la capacidad de adaptación de redes de neuronas artificiales
+ **Aprendizaje por analogía:** : intenta emular la capacidad humana de recordar la solución de problemas previos ante la aparición de problemas parecidos
+ **Aprendizaje multiestrategia:** o combinación de diferentes tipos de estrategias y/o diferentes tipos de aprendizaje.

Otro criterio puede ser basar la clasificación en el objetivo o propósito principal del proceso de aprendizaje:
+ Aprendizaje sintético: el objetivo es adquirir nuevo conocimiento e ir más allá del conocimiento poseído (inducción y analogía)
+ Aprendizaje analítico: en el que poseemos un conocimiento general y lo particularizamos para hacerlo más efectivo (deducción)
+ Aprendizaje supervisado, donde se va dirigiendo al sistema en el proceso de entrenamiento.
+ Aprendizaje no supervisado, donde no se corrige al sistema en su proceso de entrenamiento.
+ Aprendizaje por refuerzo, en el que no se le dice la salida, sólo si ha clasificado bien o no.

#### Aprendizaje inductivo
 El aprendizaje inductivo puede verse como el proceso de aprender una función. 

 ##### Inductivo supervisado
 Los métodos más utilizados en aplicaciones provienen del aprendizaje inductivo supervisado (Inducción: Pasamos de lo específico a lo general, Supervisión: Conocemos el concepto al que pertenece cada ejemplo)

A partir de un conjunto de ejemplos etiquetados obtenemos un modelo:
1. El modelo generaliza los ejemplos, representando los conceptos que definen las etiquetas
2. Obtenemos lo que es común entre los ejemplos de un concepto que les diferencia de los otros

Tipos de métodos de aprendizaje inductivo supervisado:
+ Modelos de caja blanca (podemos inspeccionar el modelo)
  + Árboles de decisión/reglas de inducción
  + Modelos probabilísticos
+ Modelos caja negra
  + Redes de neuronas artificiales
  + Máquinas de soporte vectorial

##### Workflow basico
![Workflow basico](https://github.com/13sauca13/PRG/blob/master/Recursos/Workflow%20basico%20IA.PNG)

##### Workflow cientifico
![Workflow cientifico](https://github.com/13sauca13/PRG/blob/master/Recursos/Workflow%20cientifico%20IA.PNG)

:stop_sign:*Aquí acaba la parte de la asignatura impartida por Adrián y comienza la de Marcos*

---

# Fundamentos de Big Data

:book:[Presentaciones Marcos Gestal](https://github.com/13sauca13/PRG/tree/master/MF7.3%20Big%20Data/PDFs%20Marcos)

## Introducción y conceptos previos
Un **Sistema de Información** es un conjunto de elementos (personas, dispositivos, tecnologías, procesos, aplicaciones, software, etc.) que tiene a su disposición una organización con el objetivo de capturar, almacenar, procesar y dar visibilidad a la información.

A la hora de securizar los datos de un SI, según la norma ISO 27000 tenemos que diferenciar tres conceptos:
+ Vulnerabilidad: Debilidad de un activo que puede ser explotado por una amenaza. Es la posibilidad de que una amenaza se materialice (Es la vía de ataque potencial)
  + Vulnerabilidades físicas
  + Vulnerabilidades naturales
  + Vulnerabilidades hardware
  + Vulnerabilidades software
  + Vulnerabilidad humana
+ Amenaza: Posible causa de un incidente no deseado que puede resultar en daños a un sistema u organización., es decir, es un peligro posible que podría hacer uso de una vulnerabilidad.
  + Disclosure: Revelación (amenaza a la Confidencialidad)
  + Destruction: Destrucción (amenaza a la Integridad)
  + Denial: Denegación (amenaza a la Disponibilidad)
+ Ataques: Cualquier acción que comprometa la seguridad de la información. Se trata de un asalto a la seguridad del sistema derivado de una amenaza (Zero-day Attack: Es un ataque que explota una vulnerabilidad no conocida hasta el momento)
  + Ataques pasivos: intenta conocer o hacer uso sin afectar a los recursos (difíciles de detectar pero fáciles de prevenir)
  + Ataques activos: Intenta alterar los recursos del sistema o afectar a su funcionamiento (fáciles de detectar pero difíciles de prevenir)

Nuestro objetivo es proteger el envío de información. Más en detalle debemos perseguir que el SI sea capaz de proporcionar la mayor parte de los siguientes servicios de seguridad:
+ Confidencialidad
+ Autenticidad
+ Integridad
+ Control de acceso
+ No repudio
+ Disponibilidad

El empleo del cifrado (criptografía) nos ayudará a conseguir la mayor parte de ellos.

## Criptografía
A la hora de hablar de los sistemas de cifrado (criptosistemas), se ha de diferenciar entre:
+ Sistemas INCONDICIONALMENTE seguros: Aquellos para los que se puede demostrar que sin el conocimiento de la clave no se puede obtener el texto claro correspondiente.
+ Sistemas COMPUTACIONALMENTE seguros: Aquellos que cumplen uno de los siguientes criterios:
  + Coste de rotura de cifrado > Coste de la info
  + Tiempo de rotura de cifrado > Vida útil de la info
### Posibles ataques criptográficos
+ Furza bruta: Probar todas las combinaciones de la clave hasta dar con la adecuada (el tiempo necesario suele ser excesivo)
+ Criptoanálisis:
  + A partir de texto cifrado: Simplifica mediante estudios estadísticos, análisis de vulnerabilidades de algoritmos...
  + Texto claro conocido: Aprovecha el conocimiento de parte de los datos cifrados para reducir considerablemente el tiempo de rotura
+ Elección del mensaje: Para cualquier documento se conoce su equivalente cifrado
### Tipos de sistemas de cifrado
#### Simétrico
Emplea la misma clave para cifrar y descifrar. El algoritmo de cifrado suele ser público, por lo que la seguridad del cifrado reside en como de segura sea la clave.

Operaciones de cifado:
+ Transposición: consiste en alterar el orden de las unidades constituyentes del documento original
+ Sustitución: Las unidades constituyentes del documento original son sustituidas con texto cifrado (la sustitución monoalfabética es débil al criptoanálisis de frecuencias, para ello surgen los polialfabéticos)
+ Producto: Aplicación consecutiva de transposición y sustitución. (Incrementa seguridad y permite usar operaciones más sencillas)

En cuanto al cifrado producto se crea la estructura Feistel, propuesta por Horst Feistel en 1970, que facilita la ejecución de n etapas o ciclos de un cifrado producto y es la base de los algoritmos de cifrado en bloque. Esta estructura también permite el cifrado y descifrado con el mismo sistema.

El cifrado producto por excelencia es ***DES (Data Encryption Standard)***, cuya principal característica es el efecto avalancha: pequeños cambios en el mensaje original y/o clave ariginan grandes cambios en el mensaje cifrado. (El cambio de un bit genera el cambio de la mitad del mensaje cifrado)

Los principales problemas del cifrado simétrico son:
+ Generación de claves: En un grupo de N participantes, cada uno necesita N-1 claves diferentes para para poder comunicarse con todos los participantes
+ Distribución de claves

Para solucionar los problemas de cifrado simetrico también existen diferentes soluciones:
+ KDC (Centro de Distribución de Claves): Genera claves compartidas para las comunicaciones entre usuarios
+ Cifrado asimétrico

#### Asimétrico
El cifrado asimétrico se desarrolla para tratar dos problemas:
+ La distribución de claves
+ La firma digital

Implica el uso de dos claves:
+ **KUa**: Clave pública conocida por todo el mundo. Se usará para cifrar los mensajes y verificar la firma de un mensaje
+ **KRa**: Conocida únicamente por el usuario. Se usa para descifrar mensaje y para firmarlos.

Dado esto tenemos 4 posibles escenarios:
##### Cifrado con clave pública de origen (KUorigen)
Sólo podrá descifrarse con la clave privada de origen (KRorigen)

Sólo el propietario de la clave (el origen) podrá acceder al contenido que se haya cifrado previamente

Es una especie de auto-cifrado, o cifrado para uso personal. No suele hacerse de esta manera, pues para esto es más eficiente el cifrado simétrico.
##### Cifrado con clave pública de destino (KUdestino)
Deberá descifrarse con la clave privada del destino (KRdestino)

Proporciona confidencialidad porque sólo el destinatario podrá acceder al contenido cifrado

Proporciona integridad porque si el mensaje es alterado no sé podrá descifrar, con lo que se detectará la modificación.

No proporciona autenticidad de emisor puesto que cualquiera puede enviar el mensaje cifrado, puesto que la clave con la que se cifra es pública (KUdestino). Por esta misma razón, el supuesto emisor puede negar haber enviado el mensaje (no existen pruebas de quien lo envió)
##### Cifrado con clave privada de origen (KRorigen)
Si el emisor usa su propia clave para cifrar, cualquier usuario que conozca su clave pública (KUorigen) podrá leer el mensaje, por lo tanto, ya que cualquiera puede leer el mensaje, no proporciona confidencialidad, sin embargo, sí proporciona integridad, puesto que si el mensaje se modifica no podrá ser descifrado

Autenticidad de emisor, puesto que si el mensaje se puede descifrar correctamente aplicando la clave pública del emisor (KUorigen) es porque obligatoriamente el mensaje se ha tenido que cifrar con la clave privada del emisor (KRorigen) , que sólo él posee.

Por la mismo que lo anterior, el emisor no puede negar ser quién generó el mensaje, proporcionándose así No Repudio de emisor

Es el mecanismo que hace posible la **Firma Digital**

##### Cifrado con clave privada de destino (KRdestino)
No es factible. No podemos cifrar con la clave privada de la persona con la que nos queremos comunicar, pues sólo ella posee esa clave (y la ha de mantener en secreto)

---

# Tipología, captura y preparación de los datos

:book:[PDF Virginia](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Tipologia_Captura_Preparacion_Datos.pdf)

**KDD Knowledge Data Discovery = Ciencia de Datos**

![Que es la ciencia de datos?](https://github.com/13sauca13/PRG/blob/master/Recursos/Que%20es%20la%20ciencia%20de%20datos.PNG)

Para sacar beneficio a la cantidad de información disponible es necesario comprender cuáles son las categorías de datos y las fuentes de origen de los mismos.

En base a la estructura de los datos tenemos:
+ **Datos estructurados**: Son los datos típicos de la mayoría de bases de datos relacionales y tienen un esquema determinado que define las tablas en las que se almacenan, qué tipo de campos tienen y cómo se relacionan entre ellas (Se gestionan mediante lenguaje SQL)
+ **Datos no estructurados**: Datos en bruto y no organizados, sin estructura interna identificable. Se presentan en muchos formatos con diversos grados de complejidad de fuentes heterogéneas y generados por humanos o máquinas.
+ **Datos semiestructurados**: Se encuentran a medio camino entre unos y otros, tienen cierto nivel de estructura aunque carecen de un esquema fijo. Se organizan mediante etiquetas semánticas que permiten agruparlos y crear jerarquías: Metadatos (XML, JSON, HTML...) Se refiere a cualquier información que utilice esquema de *autodescripción*.

>[!NOTE]
>**XML**
>+ Declaración: ```<?xml version="1.0" encoding="UTF-8"?>```
>+ Sintaxis: ```<etiqueta>valor</etiqueta>```
>
>**JSON**
>+ Sintaxis: ```{"etiqueta":valor}```
>+ En realidad son arrays de pares desordenados ```clave:valor```
