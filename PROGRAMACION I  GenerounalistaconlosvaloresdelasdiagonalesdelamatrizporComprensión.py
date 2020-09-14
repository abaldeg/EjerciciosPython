filas= 4
col= 4
# Creo la matriz cuadrada con 0
matriz= [[0]*col for i in range(filas)]

# Genero una lista con los valores de las diagonales de la matriz (por Comprensión)
listaDiagonalesPorComprension= [matriz[f][c] for f in range(len(matriz)) for c in range(len(matriz[0])) if f==c]
print(listaDiagonalesPorComprension)