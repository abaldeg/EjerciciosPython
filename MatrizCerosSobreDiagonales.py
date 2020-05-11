def colocarceros1(mat):
    # Alternativa 1: Recorremos toda la matriz y en cada elemento verificamos si estamos
    #                por encima o por debajo de ambas diagonales, para colocar allí un 0
    tamaño = len(mat)
    for f in range(tamaño):
        for c in range(tamaño):
            if c>=f and c<tamaño-f:  # Espacio sobre ambas diagonales
                mat[f][c] = 0
            if c<=f and c>=tamaño-f-1:  # Espacio debajo de ambas diagonales
                mat[f][c] = 0

def colocarceros2(mat):
    # Alternativa 2: Recorremos todas las filas y en cada una colocamos los ceros correspondientes
    #                según el número de fila en la que nos encontramos
    tamaño = len(mat)
    for f in range(tamaño):
        for c in range(f, tamaño-f):
            mat[f][c] = 0
            mat[tamaño-f-1][c] = 0

def imprimirmatriz(mat):
    for fila in mat:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()
    print("-"*(len(mat)*3+1))  # Línea separadora proporcional al tamaño de la matriz

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Se muestran dos alternativas equivalentes. Bastaba con una sola.
# Generamos la matriz ya cargada con números de 1 a n en cada fila, usando range()
matriz1 = [list(range(1, n+1)) for i in range(n)]
colocarceros1(matriz1)
imprimirmatriz(matriz1)
matriz2 = [list(range(1, n+1)) for i in range(n)]
colocarceros2(matriz2)
imprimirmatriz(matriz2)