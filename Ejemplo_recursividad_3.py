'''
Desarrollar una función para sumar los elementos de
una lista
'''
def sumar(lista):
    suma= 0
    for i in range(len(lista)):
        suma+= lista[i]
    return suma

# Rebanadas
def sumarRec(lista): # lista= [1,2,3,4]
    # Caso Base
    if len(lista)==0:
        return 0
    else:
        return sumarRec(lista[1:]) + lista[0]

# Índice
def sumarRecInd(lista, i=0):
    if i == len(lista):
        return 0
    else:
        return lista[i] + sumarRecInd(lista, i+1)

lista= [1,2,3]
# print(sumar(lista))
# print(sumarRec(lista))
print(sumarRecInd(lista))
