'''
Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
también será un número al azar de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''
import random
def cargarLista(lista):
    """
    Ingresa lista vacia
    Devuelve lista aleatorios
    """    
    for i in range(0,random.randint(0,9)):
        num=random.randint(0,9)
        lista.append(num)

def sumatoriaLista(lista):
    return(sum(lista))

def eliminarValor(lista,valor):
    while valor in lista:
        lista.remove(valor)

def verificaCapicua(lista):
    capicua=False
    if len(lista)%2!=0:
        for i in range(0,len(lista)):
            if lista[i]==lista[i-1]:
                capicua=True        
    return(capicua)
    

"""
Programa principal
"""
"""
lista=[]
cargarLista(lista)
print(lista)
print(sumatoriaLista(lista))
valor=int(input("Ingrese un valor a eliminar: "))
eliminarValor(lista,valor)
print(lista)
"""
lista=[50, 17, 91, 17, 50]
print(verificaCapicua(lista))
