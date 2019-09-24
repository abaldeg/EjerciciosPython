costobasico = 125
cprustica = 2.20
enctela = 80
encesp = 136

numpag=int(input("Ingrese numero de paginas: "))
costototal=costobasico+numpag*cprustica
if numpag > 300 and numpag < 600:
    costototal=costototal+enctela
elif numpag > 600:
    costototal=costototal+encesp+enctela

print ("Costo total: ",costototal)

