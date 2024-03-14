'''
La aplicación se trata de un simple juego del escondite.
El programa se "esconderá" en alguna casilla del tablero y el jugador tendrá una serie de disparos para darle.
El enemigo ocupa 2x2 y un único disparo lo mata
'''

from tabulate import tabulate
import random

# El tablero tiene un indicador de munición y una cuadrícula
tablero=[["Munición"," ","A","B","C","D","E","F","G","H","I"],
         ["*","1"],
         ["*","2"],
         ["*","3"],
         ["*","4"],
         ["*","5"],
         ["*","6"],
         ["*","7"],
         ["*","8"],
         ["*","9"]
         ]
# Generamos el tablero
for i in range(1,10):
    for j in range(2,11):
        tablero[i].append(".")
 
# La variable munición indica el número de intentos del jugador y la flag final es False hasta que el juego acabe
municion=9
final=False

# Esta variable se utilizará en la impresión del resultado del juego
gana="perdido"

# Cada vez que el jugador dispare se restará munición y se actualizará el tablero
# Se disparará con: municion=disparo(municion)
def disparo(ammo):
    tablero[ammo][0]=" "
    return(ammo-1)

# Se genera una posición aleatoria para la esquina superior izquierda del "enemigo" de manera que no pueda quedar fuera del tablero
coord_colu=random.randint(2,9)
coord_fila=random.randint(1,8)

# El juego comienza:
while not final:

    print(tabulate(tablero))

    # Un diccionario transforma la letra de la columna en un número para utilizar luego como coordenada de la tabla
    columnas={"A":2,"B":3,"C":4,"D":5,"E":6,"F":7,"G":8,"H":9,"I":10}

    # El usuario introduce las coordenadas
    tiro=input("Introduzca la coordenada para disparar (letra y número): ")
    
    #Se transforman actualiza tablero y comprueba si coinciden con la posición del enemigo
    columna=columnas[tiro[0].capitalize()]
    fila=int(tiro[1])

    if (columna==coord_colu or columna==coord_colu+1) and (fila==coord_fila or fila==coord_fila+1):
        gana="ganado"
        final=True
        tablero[coord_fila][coord_colu]="0"
        tablero[coord_fila+1][coord_colu]="0"
        tablero[coord_fila][coord_colu+1]="0"
        tablero[coord_fila+1][coord_colu+1]="0"

    elif tablero[fila][columna]==".":
        tablero[fila][columna]="*"

    # No es posible "disparar" contra casillas ya disparadas o fuera del tablero, reinicia el bucle para pedir nuevo disparo sin restar munición
    else:
        print("\nCoordenada incorrecta, introdúzcala de nuevo\n")
        continue
    
    # Se contabiliza el disparo y se comprueba que quede munición disponible, de no ser así el juego acaba
    municion=disparo(municion)

    if municion==0:
        final=True

print(tabulate(tablero))
print(f"Has {gana}!!\n")
