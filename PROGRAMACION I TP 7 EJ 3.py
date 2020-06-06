#Escribir una función que devuelva la suma de los N primeros números naturales.
def sumarNaturales(n,suma=0):
    if n==1:
        suma+=n
        return(suma)
    else:
        suma+=n
        n-=1
        return(sumarNaturales(n,suma))

print(sumarNaturales(3))


