def fMultiplica(a,b):
    cont=1
    resultado=0
    while cont <= b:
        resultado=resultado+a
        cont=cont+1
    return resultado

def fExponente(a,b):
    cont=1
    resultado=1
    while cont <= b:
        resultado=fMultiplica(a,resultado)        
        cont=cont+1
    return resultado


# print (fMultiplica(2,2))
print (fExponente(10,10))

