#Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
#utilizar cadenas de caracteres.
def contarCantDigitos(n,cantdigitos=None):
    if cantdigitos is None:
        cantdigitos=1
    n=n//10
    if  n>0:
        cantdigitos+=1
        return (contarCantDigitos(n,cantdigitos))
    else:
        return(cantdigitos) 
print(contarCantDigitos(12))

        
        
    