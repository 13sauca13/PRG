# Importamos flask y render_template
from flask import Flask, render_template

# Creamos una instancia de Flask llamada Sauca
programa=Flask("Sauca")

# El decorador @app.route recibe un string con la ruta del servidor que queremos enrutar, a continuación la función decorada
@programa.route("/")
def hola_mundo():
    return "<h1>Hola Mundo</h1><br/><a href=/hola2>Enlace pagina 2</a>"
@programa.route("/hola2")
def hola_mundo2():
    return "<h1>Hola Mundo2</h1><br/><a href=/>Enlace pagina 1</a>"
# Cramos una página con una ruta que es una variable
@programa.route("/hola2/<nombre>")
def hola_usuario(nombre):
    return "<p>Hola "+nombre+" !!!</p>"

# Vamos a incluir plantillas renderizadas en nuestro proyecto. Esto son archivos html, que pueden contener programación en su interior. (usando render_template)
@programa.route("/codigo")
def renderizada():
    return render_template("otro.html")
# Podemos pasar variables en la ruta que irán a las plantillas renderizadas
@programa.route("/codigo/<variable>")
def renderizada2(variable):
    return render_template("otro.html", veces=int(variable))


# Llamamos al método "run" de nuestra instancia y le decimos que escuche en el puerto 8080
# Activando el "debug", al guardar un cambio el servidor se reinicia solo
programa.run(port=8080, debug=True)
