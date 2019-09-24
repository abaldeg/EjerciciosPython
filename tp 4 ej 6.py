n=0
cantimpar=0
cantpar=0

while n !=-1:        
    n=int(input("Ingrese Numero: "))
    
    if n%2==0:        
        cantpar=cantpar+1
    else:        
        cantimpar=cantimpar+1

    
print ("Cantidad de numeros impares: ", cantimpar)
print ("Cantidad de numeros pares: ", cantpar)
