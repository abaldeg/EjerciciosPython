n=0
n0=0
cant=0
while n !=-1:        
    n=int(input("Ingrese Numero: "))
    
    if n < n0 and cant > 0:
        print ("Ultimo numero menor a valor anterior:", n, ". Valor anterior", n0)
    
    n0=n
    
    cant=cant+1


    

