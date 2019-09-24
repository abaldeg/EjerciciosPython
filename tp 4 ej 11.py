cant=0
mayor=0
while cant < 10:
    n=int(input("Ingresar numero: "))
    if n > mayor:
        mayor = n
    cant=cant+1
print ("El mayor numero es ", mayor)
