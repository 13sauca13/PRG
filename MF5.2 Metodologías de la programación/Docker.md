# Docker
Docker es una plataforma de código abierto para desarrollar aplicaciones, permite el despliegue de entornos independientes y aislados denominados **contenedores**.

Existen dos tipos de virtualización:
+ Nativa (Bare-Metal): se ejecuta directamente sobre el hardware físico del sistema sin necesidad de un sistema operativo anfitrión. El hipervisor (también conocido como VMM - Virtual Machine Monitor) se encarga de administrar los recursos del hardware y crear y administrar las máquinas virtuales
+ Hospedada (Hosted): Se ejecuta en un sistema operativo anfitrión y utiliza una capa de software adicional para crear y administrar las máquinas virtuales.

<hr/>

```docker-compose up --build ld``` (-d lo ejecuta en segundo plano para liberar la linea de comandos)
