#Escribir una función para eliminar una subcadena de una cadena de caracteres, a
#partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
#Escribir también un programa para verificar el comportamiento de la misma.
#Escribir una función para cada uno de los siguientes casos:
#a. Utilizando rebanadas
#b. Sin utilizar rebanadas

#Funciones
def eliminar_Subcadena_rebanada(cadena, comienzo, cantidad):
    pocisionfinal=len(cadena)
    return(cadena[comienzo:comienzo+cantidad])

def eliinar_Subcadena_sin_rebanada(cadena, comienzo, cantidad):
    cadaux=""
    for i in range(0,len(cadena)):
        if i>=comienzo and i <=comienzo+cantidad:
            cadaux+=cadena[i]
    return(cadaux)

#Programa Principal
print(extraer_Subcadena_rebanada("El número de teléfono es 4356-7890",25,9))
print(extraer_Subcadena_sin_rebanada("El número de teléfono es 4356-7890",25,9))

#Programa Principal
print(extraer_Subcadena_rebanada("El número de teléfono es 4356-7890",25,9))
print(extraer_Subcadena_sin_rebanada("El número de teléfono es 4356-7890",25,9))
