#Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
#indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
#como valor de retorno. Escribir también un programa para verificar el comportamiento
#de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
#7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
#resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes
#casos:
#a. Utilizando rebanadas
#b. Sin utilizar rebanadas

#Funciones
def extraer_Subcadena_rebanada(cadena, comienzo, cantidad):
    pocisionfinal=len(cadena)
    return(cadena[comienzo:comienzo+cantidad])

def extraer_Subcadena_sin_rebanada(cadena, comienzo, cantidad):
    cadaux=""
    for i in range(0,len(cadena)):
        if i>=comienzo and i <=comienzo+cantidad:
            cadaux+=cadena[i]
    return(cadaux)

#Programa Principal
print(extraer_Subcadena_rebanada("El número de teléfono es 4356-7890",25,9))
print(extraer_Subcadena_sin_rebanada("El número de teléfono es 4356-7890",25,9))