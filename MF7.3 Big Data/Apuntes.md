# Big Data
:monocle_face: ***6 preguntas tipo test*** *adriancarballal@gmail.com*

:book:[PDF apuntes BigData](https://github.com/13sauca13/PRG/blob/master/MF7.3%20Big%20Data/Big%20Data%20E2T.pdf)

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
