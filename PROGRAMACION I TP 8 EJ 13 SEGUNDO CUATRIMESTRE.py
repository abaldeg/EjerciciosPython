"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario.
Comprobar el comportamiento de la función mediante un programa apropiado."""
import random
def buscarclave(dic, valor):
    """ Busca las claves que contengan el valor pasado como parámetro. """    
    for clave in dic:
        if valor==dic[clave]:
            lista.append(clave)            
    return lista

"""Programa principal"""
lista=[]
dic= {x:random.randint(1,2) for x in range(1,10)}
buscarclave(dic, 2)
print(dic)
print(lista)
