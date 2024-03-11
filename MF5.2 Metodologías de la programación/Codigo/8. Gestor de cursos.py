'''
Crea un programa que sirva para gestionar estudiantes y cursos.
'''

class Estudiante:
    altas=[]
    def __init__(self,nombre,apellido,DNI,edad) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.dni=DNI
        self.edad=edad
        Estudiante.altas.append(self)
    def __str__(self) -> str:
        return(self.nombre+" "+self.apellido)
    @staticmethod
    def estudiantes():
        for i in Estudiante.altas:
            print(i)

class Curso:
    creados=[]
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        self.estudiantes=[]
        Curso.creados.append(self)
    def agregar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    def __str__(self) -> str:
        return(self.nombre)
    @staticmethod
    def estudian(consulta):
        for i in consulta.estudiantes:
            print(i)
    @staticmethod
    def cursos_creados():
        for i in Curso.creados:
            print(i)

terminado=False

while not terminado:
    print("\nElige una opción:\n1. Consultar cursos\n2. Consultar alumnos\n3. Crear nuevo curso\n4. Matricular alumno\n5. Dar nuevo alumno de alta\n6. Salir del programa")
    seleccion=input("\n")

    if seleccion=="1":
        Curso.cursos_creados()
    elif seleccion=="2":
        seleccion2=input("\nElige una opción:\n1. Consultar estudiantes matriculados en un curso\n2. Consultar todos los estudiantes dados de alta\nPulse cualquier otra tecla para volver atrás...\n")
        if seleccion2=="1":
            seleccion3=input("\nIntroduzca el nombre del curso: ")
            try:
                Curso.estudian(seleccion3)
            except:
                print("El curso seleccionado no existe")
        elif seleccion2=="2":
            Estudiante.estudiantes()
        else:
            continue
    elif seleccion=="3":
        curso=input("Introduzca el nombre del curso a crear: ")
        # COMO CAMBIO EL NOMBRE DE LA INSTANCIA
        pass
    elif seleccion=="4":
        nombre=input("Introduzca el nombre del alumno: ")
        curs=input("Introduzca el curso: ")
        curs.agregar_estudiantes(nombre)
    elif seleccion=="5":
        nombre=input("Introduzca el nombre del alumno: ")
        apellido=input("Introduzca los apellidos del alumno: ")
        dni=input("Introduzca el DNI del alumno: ")
        edad=input("Introduzca la edad del alumno: ")
        # COMO CAMBIO EL NOMBRE DE LA INSTANCIA
    elif seleccion=="6":
        terminado=True
    else:
        print("\Selección inválida. Revise su respuesta\n")
