'''
Hacer un juego: Un concurso de la tele, hay tres puertas, una con una oveja, otra vacia y otra con un coche.
El jugador elegirá una puerta y el presentador abrirá una de las puertas no elegidas que no contiene el coche
El jugador cambiará o no de manera aleatoria.
Se levantará una estadística del éxito al ganar el coche tanto para cuando el jugador eligió cambiar de puerta como para cuando eligió no cambiar
Todo el proceso se ejecutará en automático, se introducirán únicamente el número de iteraciones.
'''

class Concurso:
    def __init__(self):
        # Se crean las variables necesarias para levantar estadísticas en el método "concursar"
        self.cambia_gana=0
        self.cambia_pierde=0
        self.nocambia_gana=0
        self.nocambia_pierde=0
        self.cambiadas=0
        self.mantenidas=0

    def concursar(self,rondas:str) -> str:
        self.rondas=rondas
        while self.rondas>0:
            self.rondas-=1
        # El estado inicial serán tres puertas vacías:
            puertas={"puerta 1":"","puerta 2":"","puerta 3":""}
        # El presentador desordena aleatoriamente los tres premios y los mete en las puertas
        # El presentador sabe donde se guarda el coche
            premios=["Coche","Oveja","Nada"]
            import random
            random.shuffle(premios)
            j=0         # Contador para usar como índice en premios dentro del "for"
            for i in puertas:
                puertas[i]=premios[j]
                if premios[j]=="Coche":
                    puerta_premiada=i
                j+=1    # Aumento contador para pasar al siguiente índice
        # El jugador elige una puerta al azar
            opciones=["puerta 1","puerta 2","puerta 3"]
            eleccion_inicial=random.choice(opciones)
        # El presentador abre al azar una de las puertas no elegidas que no contiene el premio
            while len(opciones)>2:
                x=random.randint(0,2)
                if opciones[x]!=puerta_premiada and opciones[x]!=eleccion_inicial:
                    opciones.remove(opciones[x])
        # El jugador elige una nueva puerta, cambia o no cambia
            eleccion_2=random.choice(opciones)
            if eleccion_2==eleccion_inicial:
                cambio=False
                self.mantenidas+=1
            else:
                cambio=True
                self.cambiadas+=1
        # Se abren todas las puertas y el concurso termina.
        # Se revisan y anotan resultados
            if eleccion_2==puerta_premiada:
                if cambio==True:
                    self.cambia_gana+=1
                else:
                    self.nocambia_gana+=1
            else:
                if cambio==True:
                    self.cambia_pierde+=1
                else:
                    self.nocambia_pierde+=1
        # Para la presentación de los datos se pasan los resultados acumulados a porcentajes
        self.cambia_gana=round((self.cambia_gana/self.cambiadas)*100,3)
        self.cambia_pierde=round((self.cambia_pierde/self.cambiadas)*100,3)
        self.nocambia_gana=round((self.nocambia_gana/self.mantenidas)*100,3)
        self.nocambia_pierde=round((self.nocambia_pierde/self.mantenidas)*100,3)
        return(f"\nEl jugador ha tenido las siguientes estadísticas:\n    - Cambiando la elección ha ganado el {self.cambia_gana}% y perdido el {self.cambia_pierde}% de las veces.\n    - Manteniendo la elección ha ganado el {self.nocambia_gana}% y perdido el {self.nocambia_pierde}% de las veces.")

# A continuación se pedirá el número de rondas que el jugador jugará para llevarse el premio
concurso=Concurso()
iteraciones=int(input(f"Cuántas rondas del concurso jugará? "))
# Inciamos un temporizador para ver cuanto le lleva al programa ejecutarse
import time
inicio=time.perf_counter()
# Imprimimos resultados del concurso y del tiempo de ejecución
print(concurso.concursar(iteraciones))
fin=time.perf_counter()
print(f"\nLa ejecucuión de las {iteraciones} rondas ha tardado {fin-inicio} segundos")
