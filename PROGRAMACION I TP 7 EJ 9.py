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
    row1 = [3, 4, 5, 5]
    row2 = [97, 98, 99, 11]
    row3 = [1959, 196, 19, 198]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    print_recursive(matrix)
