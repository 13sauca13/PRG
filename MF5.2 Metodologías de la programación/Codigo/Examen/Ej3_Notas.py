def Notas(t_escrito,t_clase,ex_progresion,ex_papel,ex_plataforma,ej_ex,recompensa):
    nota=t_escrito*0.2+t_clase*0.1+ex_progresion*0.05+ex_papel*0.2+ex_plataforma*0.2+ej_ex*0.25
    if not recompensa:
        return(nota)
    else:
        return(nota*0.2+8)

data_ok=False

while not data_ok:
    t_escrito=int(input("Introduzca la nota del trabajo escrito: "))
    t_clase=int(input("Introduzca la nota del trabajo en clase: "))
    ex_progre=int(input("Introduzca la nota del examen de progresión: "))
    ex_papel=int(input("Introduzca la nota del examen escrito: "))
    ex_plataf=int(input("Introduzca la nota del examen de la plataforma: "))
    ex_final=int(input("Introduzca la nota de los ejercicios del examen final: "))
    recomp=bool(input("Tiene recompensa el alumno? (introduzca 1 si la tiene y 0 si no): "))

    if 0<=t_escrito<=10 and 0<=t_clase<=10 and 0<=ex_progre<=10 and 0<=ex_papel<=10 and 0<=ex_plataf<=10 and 0<=ex_final<=10:
        data_ok=True
    else:
        print("\nLas notas introducidas no son válidas, revise y recuerde que deben estar entre 0 y 10\n")
        continue

print(f"\nLa nota final es {Notas(t_escrito,t_clase,ex_progre,ex_papel,ex_plataf,ex_final,recomp)}\n")
