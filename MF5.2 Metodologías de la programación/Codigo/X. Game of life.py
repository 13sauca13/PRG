import random
from tabulate import tabulate
import os

tablero=[]

y=20
x=10
celulas=10

for i in range(x):
    tablero.append([])
    for j in range(y):
        tablero[i].append(".")

for i in range(celulas):
    eje_x=random.randint(0,x-1)
    eje_y=random.randint(0,y-1)
    tablero[eje_x][eje_y]="*"

print(tabulate(tablero))

while True:
    os.system("cls ")
    print(tabulate(tablero))

    for i in range(x):
        for j in range(y):
            if tablero[i][j]=="."
