"""
Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
un programa para ingresar los tres valores, invocar a la función y mostrar el
máximo hallado, o un mensaje informativo si éste no existe.
"""
def obtenerMayor(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            mayor=n1
    elif n2>n1:
        if n2>n3:
            mayor=n2
    elif n3>n1:
        if n3>n2:
            mayor=n3
    else:
        mayor=-1
    return(mayor)

print(obtenerMayor(1,1,1))        
