# Sin tener en cuenta el signo, cuál es el número más alto que podemos codificar si tenemos 16 bits?
# Opción 1:
x=pow(2,16)
print(x)
# Opción 2:
n=""
for i in range(16):
    n=n+"1"
print(n, len(n), int(n,2))

# Convierta el número 12345 a binario y a hexadecimal
n=12345
print(format(n,'b'))
print(format(n,'x'))

# Cuántos bits ocuparía el número 123456
n=123456
print(len(format(n,'b')))

# Hacer una funcion que adivine el numero que piensa el usuario entre 1 y 100. Utilizar la busqueda binaria
print("Piensa un número entre 1 y 100, yo trataré de adivinarlo")
inicio=0
fin=100
prueba=(fin-inicio)//2
print("Tu número es el",prueba,"?")
respuesta=input("s/n: ")
while respuesta=="n":
    mayor_menor=input("Entonces tu número es mayor o menor? ")
    if mayor_menor=="mayor":
        inicio=prueba
        prueba=(fin+inicio)//2     
    else:
        fin=prueba
        prueba=(fin+inicio)//2
    print("Tu número es el",prueba,"?")
    respuesta=input("s/n: ")
print("Acerté!! Tu número es",prueba)

# Realizar una función que devuelva el número de billetes y monedas que hacen falta para una determinada cantidad de dinero
def cambio(dinero):
    billetes={500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0,0.5:0,0.2:0,0.1:0,0.05:0,0.02:0,0.01:0}
    for x in billetes:
        cambiado=dinero//x
        billetes[x]=cambiado
        dinero=dinero-(cambiado*x)
    return(billetes)

print(cambio(1898.687))

# Crea un código que capture los errores:
try:
    usuario=input("Introduzca un número: ")
    usuario=int(usuario)
    division=usuario/0
except ValueError:
    print("Eso no era un numero, pusiste:",usuario)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except:
    print("Error desconocido")

# Crea el directorio "prueba" con 41 directorios dentro y 4 archivos de texto por directorio
import os
for i in range(1,42):
    os.makedirs("prueba/"+str(i))
    for j in range(1,5):
        with open("prueba/"+str(i)+"/"+str(j)+".txt", "w") as fichero:
            fichero.write(str(" "))

# Crea el directorio "prueba2" con 41 directorios dentro y 4 archivos por directorio con una extensión aleatoria de entre 4 opciones
import os
import random
for i in range(1,42):
    os.makedirs("Python/prueba2/"+str(i))
    for j in range(1,5):
        posibilidades=[".txt",".jpg",".doc",".csv"]
        extension=random.choice(posibilidades)
        with open("Python/prueba2/"+str(i)+"/"+str(j)+extension, "w") as fichero:
            fichero.write(str(" "))
# En el ejercicio anterior añade un contador del número de ficheros que hay de cada tipo:
txt=0
jpg=0
doc=0
csv=0
for l in os.listdir("Python/prueba2"):
    for m in os.listdir("Python/prueba2/"+str(l)):
        ext=m[len(m)-3:]
        if ext=="txt":
            txt+=1
        elif ext=="jpg":
            jpg+=1
        elif ext=="doc":
            doc+=1
        elif ext=="csv":
            csv+=1
print(f"El directorio prueba2 contiene: {txt} documentos de texto, {jpg} imagenes, {doc} archivos de word y {csv} archivos csv.")
