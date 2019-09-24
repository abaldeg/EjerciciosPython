n=0
menor=99999
mayor=-99999

while n !=-1:        
    n=int(input("Ingrese Numero: "))
    
    if n < menor and n != -1:        
        menor=n
    if n > mayor and n != -1:        
        mayor=n
    
print ("Numero ingresado mayor: ", mayor)
print ("Numero ingresado menor: ", menor)
