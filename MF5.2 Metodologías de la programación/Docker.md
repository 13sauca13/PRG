# Docker
Docker es una plataforma de código abierto para desarrollar aplicaciones, permite el despliegue de entornos independientes y aislados denominados **contenedores**.

Existen dos tipos de virtualización:
+ Nativa (Bare-Metal): se ejecuta directamente sobre el hardware físico del sistema sin necesidad de un sistema operativo anfitrión. El hipervisor (también conocido como VMM - Virtual Machine Monitor) se encarga de administrar los recursos del hardware y crear y administrar las máquinas virtuales
+ Hospedada (Hosted): Se ejecuta en un sistema operativo anfitrión y utiliza una capa de software adicional para crear y administrar las máquinas virtuales.

Las máquinas virtuales (VMs) se ejecutan a través de un hipervisor que crea y administra una capa de abstracción entre el hardware físico y el sistema operativo de la máquina virtual. El hipervisor se encarga de mular el hardware subyacente, incluyendo la CPU, la memoria, el almacenamiento y las interfaces de red, permitiendo que se ejecute un sistema operativo completo y aislado en cada máquina virtual. Cada VM tiene su propio kernel y sistema operativo, lo que significa que es posible ejecutar diferentes sistemas operativos y versiones en cada VM.

Los contenedores son una forma más ligera de virtualización que permite la ejecución de aplicaciones y servicios en un entorno aislado sin necesidad de un sistema operativo completo. En lugar de utilizar un hipervisor, los contenedores se ejecutan en una única instancia de sistema operativo que comparten los recursos de hardware del sistema anfitrión. Los contenedores utilizan la funcionalidad del kernel subyacente para crear un entorno aislado para cada aplicación, incluyendo el espacio de nombres, el control de recursos y la gestión de procesos. **Los contenedores no emulan el hardware**

<hr/>

```docker-compose up --build -d``` (-d lo ejecuta en segundo plano para liberar la linea de comandos)
