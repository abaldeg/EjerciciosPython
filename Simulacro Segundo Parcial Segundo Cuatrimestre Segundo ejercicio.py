"""2) Desarrollar una función recursiva que reciba un número binario y lo devuelva convertido
a base decimal. Creando una excepción o generando ValueError en caso de recibir un número que no es
binario o un número negativo con el mensaje aclaratorio correspondiente a cada error. Resolver utilizando
raise o assert."""
def convertirBaD(cadena):
    if not cadena:
        return 0
    print(cadena[:-1])
    return convertirBaD(cadena[:-1]) * 2 + (cadena[-1] == '1')
