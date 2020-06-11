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