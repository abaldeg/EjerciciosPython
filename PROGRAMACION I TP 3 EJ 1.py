# Desarrollar cada una de las siguientes funciones y escribir un programa que permita
# verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
# teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
# f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
# g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
# parámetro.
# h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número
# se recibe como parámetro.
# i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
# j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
# una lista con los números de las mismas.
# NOTA: El valor de N debe establecerlo el programador o ingresarse por teclado,
# pero las funciones deben servir aunque este valor se modifique.


#Funciones
def cargarMatriz(matriz):
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
# teclado.
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            numero=int(input("Ingrese numero para matriz: "))
            matriz[f][c]=numero
    return

def ordenarFilas (matriz):
    # b. Ordenar en forma ascendente cada una de las filas de la matriz.
    matriz.sort()

def intercambiaFilas (matriz,numero1,numero2):
    # c. Intercambiar dos filas, cuyos números se reciben como parámetro.    
    listaaux=matriz[numero1][:]    
    matriz[numero1][:]=matriz[numero2][:]
    matriz[numero2][:]=listaaux

def intercambiaColumnas (matriz,numero1,numero2):
    # d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
    

#Programa Principal
n=int(input("Ingrese tamaño de la matriz: "))
matriz=[]
for i in range(n):
    matriz.append([0]*n)
print("La matriz está así:")
for f in range(n):
    for c in range (n):
        print ("%d" %(matriz[f][c]), end="")
    print()

cargarMatriz(matriz)
print("La matriz cargada a mano está así:")
for f in range(len(matriz)):
    for c in range (len(matriz)):
        print ("%d" %(matriz[f][c]), end="")
    print()

ordenarFilas(matriz)
print("La matriz ordenada está así:")
for f in range(len(matriz)):
    for c in range (len(matriz)):
        print ("%d" %(matriz[f][c]), end="")
    print()
    
intercambiaFilas(matriz,0,1)
print(matriz[numero1][:])
print(matriz[numero2][:])
