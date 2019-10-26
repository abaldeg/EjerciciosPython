def fMayor(a,b):    
    
    if a > b :
        maximo = a
    else:
        maximo = b
    
    return maximo

a=int(input("Ingrese número a: "))
b=int(input("Ingrese número b: "))

print ("El numero mayor es",fMayor(a,b))
    