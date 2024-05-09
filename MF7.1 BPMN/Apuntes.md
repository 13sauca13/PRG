# BPMN
## Introduccion
A partir de la década de los 80, a raíz del modelo japonés (Sistema de producción Toyota), se impulsó la implantación de un sistema estructural basado en la gestión por procesos.

Se trata de una metodología empresarial cuyo objetivo es mejorar el desempeño (eficiencia y eficacia) y la optimización de los procesos de una organización.

El objetivo principal del BPMN es proveer una notación gráfica para el modelado de procesos que sea fácilmente entendible por todos los usuarios de negocio (NO el usuario del producto o el cliente).

Un diagrama BPMN es un tipo de diagrama de flujo que utiliza iconos estandarizados para representar los diferentes elementos y el flujo de un proceso de negocio. 

### Proceso de negocio
Los procesos de negocio son fluijos de trabajo concretos de material, información y conocimientos: conjuntos de actividades que permiten elaborar un producto o servicio valioso.

En resumen son una colección de actividades que tomando una o más entradas crean una salida que tiene valor para el cliente.

### Modelado de procesos
Es la subdivisión del proceso de negocio en sus elementos básicos con el propósito de poderlos estudiar y mejorarlos.

Nos ayuda a identificar el problema que el sistema de información deberá resolver y la manera en como deberá resolverlo.

Existen diferentes puntos de vista para el modelado:
+ Datos
+ Funciones
+ Organización
+ Procesos
+ Productos/Servicios

![Vistas modelado](https://github.com/13sauca13/PRG/blob/master/Recursos/Vistas%20modelado%20procesos.PNG)

### Modelo en las organizaciones
El modelo de una organización es un conjunto de conceptos que permiten construir una representación organizacional de la empresa. Existen dos enfoques:
+ Funcional (tradicional): Una función seidentifica con un verbo y es algo continuo (comprar, vender...)
+ Proceso: Se identifica con verbo+sustantivo y tiene inicio y fin, no es continuo (ensamblar pieza, solicitar material...)

![Vision funcional vs procesos](https://github.com/13sauca13/PRG/blob/master/Recursos/Vision%20funcional%20vs%20procesos.PNG)

En resumen, la visión por procesos se enfoca en la identificación y mejora de los procesos clave que son críticos para la entrega de productos o servicios a los clientes.
Mientras que la visión funcional se enfoca en la organización de la empresa en departamentos funcionales y en la eficiencia de estos departamentos.

### BPMN vs UML
La principal diferencia entre BPMN y UML es su finalidad: UML se utiliza para modelar software mientras que BPMN describe procesos empresariales

## Notacion basica de BPMN 2.0
### Modelado de procesos
El objetivo es lograr un nivel de desagregación que permita llegar al nivel de procesos operativos de bajo nivel. (SACAR LOS PROCESOS MÁS PEQUEÑOS)
1. Identificar las entidades que participan
2. Entradas y salidas del proceso
3. Secuencia temporal de las actividades y entidades que las realizan
4. Los puntos de medición, indicadores y metas
5. Nombre del proceso, breve descripción y quien es el responseble
6. Cuando se inicia, que incluye y cuando finaliza
7. Las relaciones con otros porcesos y otros clientes

Loa símbolos de BPMN se dividen en 4 categorías básicas
+ Objetos de flujo: Definen el comportamiento de los procesos
  + Eventos: Algo que sucede
  + Actividades: Acciones que se llevan a cabo
  + Decisores: Puntos de divergencia o convergencia
+ Objetos de conexión: Simbolizan como se conectan los objetos entre si
  + Líneas de secuencia: Control de flujo y secuencia de actividades
  + Líneas de mensaje: Mensajes entre procesos (sólo se utiliza entre swimlanes)
  + Líneas de asociación: Información adicional y datos de E/S
+ Artefactos: Información adicional
  + Objetos de datos: Documentos u otros objetos que son usados o actualizados
  + Anotación de texto: Información adicional sobre el proceso
  + Grupos: Agrupa conjuntos de actividades
+ Swimlanes: Organizadores (organizar las actividades del flujo en diferentes categorías visuales que representan áreas funcionales, roles o responsabilidades)
  + Pool: Representan organizaciones o procesos. Solo contiene un proceso. Los flujos de secuencia no pueden cruzar los límites de un pool.
  + Lanes: Representan roles o departamentos en una organización (nunca personas concretas)
![Swimlanes](https://github.com/13sauca13/PRG/blob/master/Recursos/Swimlane%20BPMN.PNG)

### Eventos básicos
Un evento representa algo que ocurre (o puede ocurrir) durante un proceso, se nombra con ```NOMBRE+PARTICIPO```, existen tres tipos:
+ Eventos de inicio: Desencadena el flujo de secuencia del proceso
+ Eventos intermedio: Interrumpe temporalmente el flujo del proceso
+ Eventos final: Finaliza el flujo

Dentro de estos tres tipos de eventos hay muchas variantes:
+ Temporizador
+ Condicional: tiene asociada una restricción.
+ Señal: recibe una señal “catch”, lanza una señal “throw”
+ Escalada: inicia subproceso al recibir mensaje de escalada, envía un mensaje escalable.
+ Compensación: deshacer acciones, finaliza e inicia el rebobinado de las acciones del proceso.
+ Múltiple: varias formas/reglas de inicio con una ya se inicia, el evento se dispara con que se cumpla una regla.
+ Paralelo: varias reglas se tienen que cumplir todas, el evento se dispara si se cumplen todas.
+ Enlace: flujo de secuencia virtual. Van en pares como un throw-catch.
+ Cancelación: Finaliza el proceso cerrando todos los «tokens» activos. Este elemento es importante si existen caminos paralelos en su proceso.

![Eventos BPMN](https://github.com/13sauca13/PRG/blob/master/Recursos/Eventos%20BPMN.PNG)

## Conceptos basicos de BPMN 2.0
## Aplicaciones para la automatizacion de procesos
