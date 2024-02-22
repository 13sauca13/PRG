# Ejercicio
# Realice una función que devuelva una lista, con la cantidad de números 
# aleatorios que le indiquemos, en el rango indicado.
# Ejemplo: generador(45, 0, 100) nos devolverá una lista de 45 elementos, los
# cuales serán números aleatorios del 0 al 100.
#
# Recordar utilizar la función random.random().
# Recordar que random debemos importarlo [import random] al inicio

import random

def generador(elementos,inicio,fin):
    lista=[]
    for i in range(elementos):
        lista.append(int(random.random()*(fin-inicio))+inicio)
    return(lista)
        
print(generador(18,6,60))

# Ejercicio:
# Realiza una función que sume todos los elementos de una lista.

import random

def generador(elementos,inicio,fin):
    lista=[]
    for i in range(elementos):
        lista.append(int(random.random()*(fin-inicio))+inicio)
    return(lista)

def sumatorio(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return(suma)


print(sumatorio(generador(18,6,60)))

# Ejercicio:
# Realiza una función que elimine todos los elementos duplicados de una lista

def elimina_repes(lista):
    nueva = lista.copy()
    for i in lista:
        if nueva.count(i)!=1:

            # list.remove(i)
            nueva.remove(i)
    print(nueva)

lista=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7]
print(lista)
elimina_repes(lista)
# También se puede resolver con: print(list(set(lista)))

