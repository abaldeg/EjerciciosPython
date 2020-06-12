"""Realizar una función recursiva para imprimir una matriz de M x N."""

def print_recursive(matrix, i=0, j=0):
    if i < len(matrix):
        row = matrix[i]
        if i == len(matrix) and j == len(row):
            return
        elif j == len(row):
            print_recursive(matrix, i + 1)
        else:
            print(row[j])
            print_recursive(matrix, i, j + 1)


if __name__ == '__main__':
    matrix = []
    row1 = [1, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    print_recursive(matrix)
    
    
#
"""Escribir una función que sume todos los elementos de una matriz de M x N y de-
vuelva el resultado."""


def summation_recursive(m, i=0, j=0, s=0):
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return s
    elif j == len(m[i]) - 1:
        return summation_recursive(m, i + 1, 0, s)
    else:
        return summation_recursive(m, i, j + 1, s + m[i][j])

#
def determinarminimo(m, i=0, j=0, min=None):
    if min is None:
        min=m[0][0]
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return min
    elif j == len(m[i]) - 1:
        return determinarminimo(m, i + 1, 0, min)
    else:
        if min > m[i][j]:
            min=m[i][j]            
        return determinarminimo(m, i, j + 1, min)


if __name__ == '__main__':
    matriz = []
    row1 = [10, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matriz.append(row1)
    matriz.append(row2)
    matriz.append(row3)
    print(determinarminimo(matriz))