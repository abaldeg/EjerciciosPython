def potenciaNumeroNatural(a,b):
    if b==0:
        return(1)
    else:        
        return(a * potenciaNumeroNatural(a,b-1))
        print(a,b)
print(potenciaNumeroNatural(2,2))
        