def cortarLista(lista):
    nuevaLista = []
    for n in lista:
        nn = str(n)
        nuevaLista.append(int(nn[0:1]))
    return nuevaLista

lista = []
n = 0
while(n != -1):
    n = int(input("Ingrese un numero para la lista, -1 para terminar:"))
    if(n != -1):
        lista.append(abs(n))

nuevaLista = cortarLista(lista)
print("Lista:", nuevaLista)
print("Sumatoria:", sum(nuevaLista))