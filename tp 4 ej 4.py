n=0
impar=False
while n !=-1:        
    if impar==True:
        impar=False
    else:
        ultimopar=n
        impar=True

    n=int(input("Ingrese Numero: "))

print ("Ultimo numero en posicion par: ", ultimopar)
