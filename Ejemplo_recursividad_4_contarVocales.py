'''
Desarrollar una función para contar cuantas vocales
posee una cadena.
'''
def contarVocales(cadena):
    cont= 0
    for letra in cadena:
        letra= letra.lower()
        if letra in ('a','e','i','o','u'):
            cont+=1
#         else:
#             cont+=0
            
    return cont

def contarVocRec(cadena):
    if len(cadena)==0:
        return 0
    else:
        letra= cadena[0].lower()
        if letra in ('a','e','i','o','u'):
            return contarVocRec(cadena[1:])+1
        else:
            return contarVocRec(cadena[1:])

cadena= "Hl mnd!"
print(contarVocales(cadena))
print(contarVocRec(cadena))
