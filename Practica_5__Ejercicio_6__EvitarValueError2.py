def cargarlista():
    lista = []
    n = int(input("Ingrese un número o -1 para terminar: "))
    while n!=-1:
        lista.append(n)
        n = int(input("Ingrese un número o -1 para terminar: "))
    return lista

def mostrarelementos(lista):
    errores = 1
    elem = int(input("Qué elemento desea buscar? (-1 para terminar): "))
    while elem!=-1 and errores<3:
        try:
            pos = lista.index(elem)
            print("Elemento", elem,"- Posición:",pos)
        except ValueError:
            print("Elemento inexistente. Vuelva a intentarlo.")
            errores = errores + 1
        elem = int(input("Qué elemento desea buscar? (-1 para terminar): "))
    return errores

# Programa principal
lista = cargarlista()
print("-" * 60)
if mostrarelementos(lista)==3:
    print("Demasiados errores. Abortando.")
        