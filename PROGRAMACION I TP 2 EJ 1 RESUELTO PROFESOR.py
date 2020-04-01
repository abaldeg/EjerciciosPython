# Practica 2, ejercicio 1

import random

def cargarlista():
    cantidad = random.randint(10, 99)   # Número al azar de dos dígitos
    numeros = [ ]
    for i in range(cantidad):
        azar = random.randint(1000, 9999)   # Números al azar de cuatro díigitos
        numeros.append(azar)
    return numeros

def calcularsumatoria(numeros):
    return sum(numeros)

def eliminarvalor(numeros, valor):
    while valor in numeros:
        numeros.remove(valor)

def escapicua(numeros):
    izq = 0
    der = len(numeros) - 1   # El subindice correspondiente a la longitud NO pertenece a la lista
    bandera = True   # Asumimos que es capicúa, ahora vamos a verificarlo
    while izq<der:
        if numeros[izq]!=numeros[der]:
            bandera = False   # Encontramos una diferencia, entonces no es capicua
            break
        izq = izq + 1
        der = der - 1
    return bandera

# Programa principal
lista = cargarlista()
print(lista)
suma = calcularsumatoria(lista)
print("La suma de los elementos de la lista es de", suma)
n = int(input("Qué valor desea eliminar? "))
eliminarvalor(lista, n)
print(lista)
if escapicua(lista):
    print("La lista es capicúa")
else:
    print("La lista no es capicúa")