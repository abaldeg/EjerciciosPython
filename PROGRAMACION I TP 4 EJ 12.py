#Desarrollar una función para reemplazar todas las apariciones de una palabra por
#otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
#cantidad de reemplazos realizados. Escribir también un programa para verificar el
#comportamiento de la función
def reemplazarCadena(cadena,palorig,palreemp):
    listaux=cadena.split()    
    cont=listaux.count(palorig)
    for c in cadena:
        if c==palorig:
            c=palreemp
    cadenaaux=cadena.replace(palorig,palreemp)
    return(cadenaaux,cont)

print(reemplazarCadena("Hola Mundo","Mundo","Universo"))

    
    