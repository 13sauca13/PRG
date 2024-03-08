import turtle

tablero=turtle.Screen()
tablero.title("Mi tablero")
tablero.bgcolor("black")
tablero.setup(width=800,height=600)

cuadrado=turtle.Turtle()
cuadrado.shape(("square"))
cuadrado.color("red")
cuadrado.speed(0)

cuadrado2=turtle.Turtle()
cuadrado2.shape(("circle"))
cuadrado2.color("blue")
cuadrado2.speed(2)

for i in range(360):
    tablero.update()
    cuadrado.left(1)
    cuadrado.forward(1)
    if i<=90:
      cuadrado.color("red")  
    elif 180>=i>90:
       cuadrado.color("blue")
    elif 270>=i>180:
       cuadrado.color("green")
    else:
       cuadrado.color("yellow")
