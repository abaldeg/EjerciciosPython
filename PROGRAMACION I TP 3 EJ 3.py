#Desarrollar un programa para rellenar una matriz de N x N con números enteros al
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.

import random

#Funciones
def rellenarMatrizv1(matriz):
    largo=len(matriz)
    listanumeros=[ ] #Lista auxiliar para chequear que el numero no esté ya cargado
    for f in range(largo):
        for c in range(largo):
            numerorand=random.randint(0,(largo**2)-1)
            while numerorand in listanumeros:
                #Se sigue generando un numero al azar mientras la lista que registra los numeros
                #que se van generando YA LO TENGA. HAY QUE SEGUIR GENERANDO HASTA QUE ENCUENTRE OTRO.
                numerorand=random.randint(0,(largo**2)-1)
            matriz[f][c]=numerorand
            listanumeros.append(numerorand)

def imprimirMatriz(matriz):
    largo=len(matriz)
    for f in range(largo):
        for c in range(largo):
            print("%3d" %matriz[f][c] %largo, end = "")
        print()
            
#Programa Principal
matriz=[ ]
n=int(input("Ingrese tamaño de la Matriz: "))
print()
#Crear Matriz
for i in range (n):
    matriz.append([0]*n) 
rellenarMatrizv1(matriz)
imprimirMatriz(matriz)
    