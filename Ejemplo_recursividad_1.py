def sumarNaturalesIterativa(n): # Ejemplo: n= 6, sumNat(6) = sumaNat(5)+6 = sumaNat(4)+5+6
    if n>0:
        suma= 0
        for i in range(n+1):
            suma= suma+n
    else:
        suma=-1
    
    return suma

# Prog Ppal
# print(sumarNaturalesIterativa(5))

def sumarNaturalesRec(n):
    if n<0:
        return -1
    elif n==0: # Caso Base
        return 0
    else: # Caso Recursivo
        return sumarNaturalesRec(n-1) + n

print(sumarNaturalesRec(5))
