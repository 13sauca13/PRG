def Sumador(x,y):
    z=0
    if x<y:
        for i in range(x,y+1):
            z+=i
    elif y<x:
        for i in range(y,x+1):
            z+=i
    else:
        print("Sus números son iguales o inválidos")
    print(z)

num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

Sumador(num1,num2)
