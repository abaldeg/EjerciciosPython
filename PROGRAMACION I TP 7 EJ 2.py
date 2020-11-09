#Desarrollar una función que reciba un número binario y lo devuelva convertido a
#base decimal.
def convertirBaD(cadena):
    if not cadena:
        return 0
    print(cadena[:-1])
    return convertirBaD(cadena[:-1]) * 2 + (cadena[-1] == '1')
#convertirBaD(cadena[:-1]) va contando el digito donde esta parado.
print(convertirBaD("110"))