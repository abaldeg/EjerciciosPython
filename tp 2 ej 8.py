idvendedor=int(input("Numero de Venderdor: "))
montovtas=float(input("Monto de Ventas: "))
cantvtas=int(input("Ingrese cantidad de ventas: "))
salario=800+(50*cantvtas)+(montovtas*0.05)
print()
print("El salario del vendedor",idvendedor,"es de $",salario)