"""Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
un programa para ingresar los tres valores, invocar a la función y mostrar el
máximo hallado, o un mensaje informativo si éste no existe."""

def encontrarMayor(n1,n2,n3):    
    numMayor=n1    
    if n1>n2:
        if n1>n3:
            numMayor=n1                        
        elif n1<n3:
            numMayor=n3
        else:
            numMayor=-1
    elif n2>n3:
        numMayor=n2
    elif n3>n2:
        numMayor=n3
    else:
        numMayor=-1
    return(numMayor)

print(encontrarMayor(1,2,3))
print(encontrarMayor(7,5,6))
    
    
        
            
            
            
            
        
