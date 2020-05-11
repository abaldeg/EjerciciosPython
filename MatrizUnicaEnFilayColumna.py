import random

def llenarmatriz(mat):
    """ Rellena la matriz con números al azar entre 0 y 25
        que sean únicos en su fila y columna """
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            # Construimos una lista con los elementos de la columna c
            columna = []
            for fila in range(len(matriz)):
                columna.append(mat[fila][c])
            # Verificamos la presencia del número en la fila y en la columna
            candidato = random.randint(0,25)
            while candidato in matriz[f] or candidato in columna:
                candidato = random.randint(0,25)
            # Ahora que encontramos un número que no esté presente, lo cargamos en la matriz
            mat[f][c] = candidato

def imprimirmatriz(mat):
    """ Imprime la matriz mediante recorrido de secuencias """
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()
    print()

# Programa principal
filas = int(input("Cantidad de filas? "))
columnas = int(input("Cantidad de columnas? "))
# Rellenamos la matriz con -1 porque 0 es parte del intervalo de los números al azar
matriz = [[-1] * columnas for i in range(filas)]
llenarmatriz(matriz)
imprimirmatriz(matriz)
