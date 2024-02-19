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
