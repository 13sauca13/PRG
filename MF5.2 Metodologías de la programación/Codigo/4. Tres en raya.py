from tabulate import tabulate
import random

# Creacion del tablero
tablero=[[" ","A"," ","B"," ","C"],
         ["1","_","|","_","|","_"],
         ["2","_","|","_","|","_"],
         ["3"," ","|"," ","|"," "]
         ]
print(tabulate(tablero))

# La variable acabado se mantiene en False mientras no se cumpla el tres en raya
acabado=False

# Funcion de comprobacion del 3 en raya
def comprobacion(tablero):
    for i in range(1,6):
        if tablero[1][i]!="_" and tablero[1][i]!=" "  and tablero[1][i]!="|" and tablero[1][i]==tablero[2][i] and tablero[1][i]==tablero[3][i]:
            return True

    # Comprobacion de verticales
    for i in range(1,4):
        if tablero[i][1]!="_" and tablero[i][1]!=" " and tablero[i][1]!="|" and tablero[i][1]==tablero[i][3] and tablero[i][1]==tablero[i][5]:
            return True
    
    # Comprobacion de diagonales
    if tablero[1][5]==tablero[2][3]==tablero[3][1]:
        return True
    
    elif tablero[1][1]==tablero[2][3]==tablero[3][5]:
        return True

# El jugador elije ficha y el pc juega con la restante
jugador=str(input("Con que fichas desea jugar? (elija X ó O) ")).capitalize()
pc=["X","O"]
pc.remove(jugador)

# Empieza el juego
while not acabado:
    eleccion=(input("Introduce la coordenada de la ficha a colocar (columna fila): ")).capitalize()
    if eleccion[0]=="A":
        eleccion=f"1{eleccion[1]}"
    elif eleccion[0]=="B":
        eleccion=f"3{eleccion[1]}"
    elif eleccion[0]=="C":
        eleccion=f"5{eleccion[1]}"
    else:
        print("La coordenada seleccionada no esta en el tablero.\nRevise la jugada.")
        continue
    if tablero[int(eleccion[1])][int(eleccion[0])]!=jugador and tablero[int(eleccion[1])][int(eleccion[0])]!=str(pc[0]):
        tablero[int(eleccion[1])][int(eleccion[0])]=jugador
    else:
        print("La casilla está ocupada")
        continue
    print(tabulate(tablero))

    # Comprobamos si hay 3 en raya:
    acabado=comprobacion(tablero)
    if acabado:
        ganador=jugador
        continue

    # Juega el ordenador
    contrincante=[random.randint(1,5),random.randint(1,3)]
    pc_listo=False
    while pc_listo==False:
        if tablero[int(contrincante[1])][int(contrincante[0])]!=jugador and tablero[int(contrincante[1])][int(contrincante[0])]!="|" and tablero[int(contrincante[1])][int(contrincante[0])]!=str(pc[0]):
            tablero[int(contrincante[1])][int(contrincante[0])]=str(pc[0])
            pc_listo=True
        else:
            contrincante=[random.randint(1,5),random.randint(1,3)]
    print(tabulate(tablero))
    
    # Comprobamos si hay 3 en raya:
    acabado=comprobacion(tablero)
    if acabado:
        ganador=str(pc[0])
        continue

print("Juego terminado")
print(f"El ganador es {ganador}!")
