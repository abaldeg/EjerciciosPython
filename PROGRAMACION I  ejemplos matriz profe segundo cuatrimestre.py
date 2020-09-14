import random

filas= 4
col= 4
# Creo la matriz cuadrada con 0
matriz= [[0]*col for i in range(filas)]

# Pongo en su diagonal valores aleatorios
for i in range(len(matriz)):
    matriz[i][i]= random.randint(0,9)

# Muestro la matriz generada
for fila in matriz:
    print(f"Muestro la matriz generada {fila}")
print()

# Genero una lista con los valores de las diagonales de la matriz
listaDiagonales= []
for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        if f==c:
            listaDiagonales.append(matriz[f][c])

print(listaDiagonales)

# Genero una lista con los valores de las diagonales de la matriz (por Comprensión)
listaDiagonalesPorComprension= [matriz[f][c] for f in range(len(matriz)) for c in range(len(matriz[0])) if f==c]
print(listaDiagonalesPorComprension)

listaDiagonalesPorComprension= [matriz[f][c] for f in range(len(matriz)) for c in range(len(matriz[0])) if f==0]
print(listaDiagonalesPorComprension)

listaDiagonalesPorComprension= [matriz[f][c] for f in range(len(matriz)) for c in range(len(matriz[0])) if c==0]
print(listaDiagonalesPorComprension)


"""
listaDiagonalesPorComprension= [ print(f"Matriz {matriz[f][c]}, F:{f}, C:{c}") for f in range(len(matriz)) for c in range(len(matriz[0])) ]
print(listaDiagonalesPorComprension)
"""

"""
n= [ max(matriz[f][c]) for f in range(len(matriz)) for c in range(len(matriz[0])) ]
print(listaDiagonalesPorComprension)
"""



