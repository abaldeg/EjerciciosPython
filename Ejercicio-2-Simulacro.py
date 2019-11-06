import random

#Formateamos la matriz
def establecerDimensionMatriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(random.randint(1,9))
    return matriz

#Imprimimos la matriz
def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

def calcularFilasYColumnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    diagonalPrincipal = []
    for f in range(filas):
        print("Fila {0} , Su mayor valor es {1} y su menor valor es {2}".format(matriz[f], max(matriz[f]), min(matriz[f])))
        col = []
        for c in range(columnas):
            if c == f:
                diagonalPrincipal.append(matriz[f][c])
            col.append(matriz[c][f])
        print("Columna {0} , Su mayor valor es {1} y su menor valor es {2}".format(col, max(col), min(col)))
        col = []
    print("Diagonal Principal {0}, Su menor valor es {1}".format(diagonalPrincipal, min(diagonalPrincipal)))

matriz = establecerDimensionMatriz(4,4)
imprimirMatriz(matriz)
calcularFilasYColumnas(matriz)