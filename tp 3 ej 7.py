cant=int(input("Ingrese cantidad: "))
pciobase=float(input("Ingrese precio base: "))

cant_10_porc = 100 - 12
cant_25_porc = cant - 100

total_12 = pciobase * 12
total_10 = cant_10_porc * pciobase * 0.90
total_25 = cant_25_porc * pciobase * 0.75

total = total_12 + total_10 + total_25
promedio = total / cant
