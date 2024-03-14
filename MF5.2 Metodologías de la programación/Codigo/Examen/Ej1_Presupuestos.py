def Calculadora(madera,plastico,hospitalario,otros,km):
    ida=km
    vuelta=km*(madera+plastico+hospitalario+otros)
    madera=madera*10
    plastico=plastico*20
    hospitalario=hospitalario*40
    otros=otros*30
    presupuesto=round((ida+vuelta+madera+plastico+hospitalario+otros),2)
    return(presupuesto)

madera=float(input("Introduzca los m3 de madera: "))
plastico=float(input("Introduzca los m3 de plástico: "))
hospitalario=float(input("Introduzca los m3 de material hospitalario: "))
otros=float(input("Introduzca los m3 de otro tipo de residuos: "))
km=float(input("Introduzca los km hasta su emplazamiento: "))

print(f"\nEl presupuesto solicitado para transportar {km} km:\n -{madera} m3 de madera\n -{plastico} m3 de plastico\n -{hospitalario} m3 de residuo hospitalario\n -{otros} m3 de otros residuos\n")
print(f"Son {Calculadora(madera,plastico,hospitalario,otros,km)}€\n")
