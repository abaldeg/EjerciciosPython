cant=1
norden=0
menor=99999
while cant <= 10:
    n=int(input("Ingresar numero: "))
    if n <= menor:
        menor=n
        norden=cant
    cant=cant+1

print ("Numero menor: ", menor)
print ("Numero de orden: ", norden)


