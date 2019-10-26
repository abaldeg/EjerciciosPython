def fVerificaPar(n):    
    
    if n % 2 == 0 :
        par = True
    else:
        par = False
    
    return par

n=int(input("Ingrese número: "))

print (fVerificaPar(n))
    
