def rellenarporcolumnas(mat):
    n = len(mat)
    contador = 1
    for c in range(n):
        # Determinamos si la columna es par o impar para definir si se
        # rellena de arriba a abajo o de abajo a arriba
        if c%2==0:
            inicio = 0
            fin = n
            incremento = 1
        else:
            inicio = n-1
            fin = -1
            incremento = -1
        for f in range(inicio, fin, incremento):
            mat[f][c] = contador
            contador = contador + 1

def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()

# Programa principal
n = int(input("Tamaño de la matriz? "))
print()
matriz = [[0] * n for i in range(n)]
rellenarporcolumnas(matriz)
imprimirmatriz(matriz)