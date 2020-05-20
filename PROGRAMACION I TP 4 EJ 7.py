#Escribir una función para eliminar una subcadena de una cadena de caracteres, a
#partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
#Escribir también un programa para verificar el comportamiento de la misma.
#Escribir una función para cada uno de los siguientes casos:
#a. Utilizando rebanadas
#b. Sin utilizar rebanadas

#Funciones
def eliminar_Subcadena_rebanada(cadena, comienzo, cantidad):    
    cadenaaux=cadena[comienzo:comienzo+cantidad]
    cadenaret=""
    for c in cadena:
        if c not in cadenaaux:
            cadenaret=cadenaret+c
    return(cadenaret)

def eliminar_Subcadena_sin_rebanada(cadena, comienzo, cantidad):        
    cadenaret=""
    for i in range(len(cadena)):
        if i<comienzo and i >comienzo+cantidad:
            cadenaret=cadenaret+cadena[i]                
    return(cadenaret)



#Programa Principal
print(eliminar_Subcadena_rebanada("El número de teléfono es 4356-7890",3,9))
print(eliminar_Subcadena_sin_rebanada("El número de teléfono es 4356-7890",3,9))

