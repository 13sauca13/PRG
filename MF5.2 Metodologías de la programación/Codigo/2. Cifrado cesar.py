"""Construir una clase para hacer cifrado cesar
el cifrado cesar funciona por desplazamiento, es decir

si nuestro cifrado tiene desplazamiento 3, desplaza 3 posiciones la letra

una A se convertiria en D (A->D)

para descifrar con desplazamiento 3, la D se convertiría en A

cuando tenemos un texto, podemos acceder a las letras de cada una de sus posiciones

variable = "HOLA"
variable[0] = "H"
variable[1] = "0"

podemos crear nuestro conversor
conversor = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmñopqrstuvwxyz0123456789-_.,:;*-+"

Si uso conversor.find("B") me devuelve la posicion de esa letra
Si uso conversor[4] me devuelve la letra en esa posición

- Construir con Programación Orientada a Objetos, una clase que realice cifrado cesar
- Para instanciar la clase, le diré el desplazamiento a usar
- Tendré una función para descifrar, otra para descifrar y otra para cambiar el desplazamiento
"""

class Cesar:
    def __init__(self,desplazamiento=3):
        self.desplazamiento=desplazamiento
    def cifrar(self,texto_claro):
        alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmñopqrstuvwxyz0123456789-_.,:;*-+"
        cifrado=""
        for x in texto_claro:
            indice_claro=alfabeto.index(x)
            indice_cifrado=(indice_claro+self.desplazamiento)%len(alfabeto)
            cifrado=cifrado+alfabeto[indice_cifrado]
        print(cifrado)
    def descifrar(self,texto_cifra):
        alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmñopqrstuvwxyz0123456789-_.,:;*-+"
        claro=""
        for x in texto_cifra:
            indice_cifra=alfabeto.index(x)
            indice_claro=(indice_cifra-self.desplazamiento)%len(alfabeto)
            claro=claro+alfabeto[indice_claro]
        print(claro)

ROT13=Cesar(13)

ROT13.cifrar("HoLaCARACOLA8621+-*")

ROT13.descifrar("kjvjh89807089")
