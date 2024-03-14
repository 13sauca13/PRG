import random

frase1="Python es muy entretenido y muy versátil"
frase2='La asignatura es muy divertida y te mantiene "despierto"'
frase3="El profesor tiene muchisimos conocimientos y los imparte de manera clara y atractiva"
frase4="El progreso desde el comienzo de la asignatura hasta el final ha sido muy grande"
frase5="Algunas veces programar me da ganas de tirarme al suelo y llorar!!!"

lista=[frase1,frase2,frase3,frase4,frase5]

print(lista[random.randint(0,len(lista)-1)])