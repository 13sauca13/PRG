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

# Ejercicio
        # Realice una función, que cree una lista a partir de otras dos.
        # El resultado será la combinación de cada elemento de una lista con el de la otra
        # ejemplo: lista1 =['j', 'q'] lista2=[1,2] , resultado =['j1', 'q1', 'j2', 'q2']
lista1 =['j', 'q']
lista2=[1,2]

def combina_listas (lista1,lista2):
    resultado=[]
    for i in range(len(lista1)):
        resultado.append(str(lista1[i]+str(lista2[i])))
    print(resultado)

combina_listas(lista1,lista2)  

# Ejercicio
# Realice una función que inserte un elemento dado ANTES de cada elemento de una lista
# Ejemplo: lista=['j', 'q'] elem=[1] , resultado = ['1j', '1q']
lista=['j','q']
def inserta_elem(elemento):
    for i in range(len(lista)):
        lista[i]=str(elemento)+str(lista[i])
    print(lista)
inserta_elem(1)

