base = float(input("Ingrese BASE:"))
altura = float(input("Ingrese ALTURA:"))

if (base >= 0) and (altura >= 0):
    superficie=base*altura/2
    print("La superficie del triangulo es ",superficie)
else:
    print("Ingreso al menos un numero negativo")
