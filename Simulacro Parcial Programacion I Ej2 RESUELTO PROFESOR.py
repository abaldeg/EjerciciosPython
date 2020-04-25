# Simulacro Primer Parcial P1 - Ejercicio 2

def rellenarmatriz(mat):
    n = len(matriz)
    for f in range(1, n):
        for c in range(1, n):
            mat[f][c] = f*c

def imprimirmatriz(mat):
    for fila in mat:
        for elem in fila:
            print("%4d" %elem, end="")
        print()

# Programa principal
n = int(input("Valor máximo de la tabla de multiplicar? "))
print()
matriz = [[0]*(n+1) for i in range(n+1)]
for i in range(n+1):
    matriz[0][i] = i
    matriz[i][0] = i
rellenarmatriz(matriz)
imprimirmatriz(matriz)
