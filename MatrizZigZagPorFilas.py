def rellenarmatriz1(mat):
    # Alternativa 1: Rellenando la matriz elemento por elemento.5
    n = len(mat)
    contador = 1
    for f in range(n):
        # Determinamos si la fila es par o impar para definir si se
        # rellena de izquierda a derecha o de derecha a izquierda
        if f%2==0:
            inicio = 0
            fin = n
            incremento = 1
        else:
            inicio = n-1
            fin = -1
            incremento = -1
        for c in range(inicio, fin, incremento):
            mat[f][c] = contador
            contador = contador + 1

def rellenarmatriz2(mat):
    # Alternativa 2: Rellenamos la matriz sin zig-zag y luego usamos
    #                reverse() para invertir las filas impares.
    n = len(mat)
    contador = 1
    for f in range(n):
        for c in range(n):
            mat[f][c] = contador  # f*n+c+1 daría lo mismo y evitamos el contador
            contador = contador + 1
        if f%2==1:            # Si la fila es impar...
            mat[f].reverse()  # ...la invertimos

def rellenarmatriz3():
    # Alternativa 3: Creamos la matriz desde la nada usando range() para generar cada fila,
    #                e invertimos las filas impares usando reverse().
    mat = []
    for i in range(n):
        mat.append(list(range(i*n+1, i*n+n+1)))
        if i%2!=0:  # Fila impar descendente
            mat[i].reverse()
    return mat

def rellenarmatriz4():
    # Alternativa 4: Creamos la matriz desde la nada usando listas por comprensión
    #                y range() para generar cada fila, e invertimos las filas impares
    #                usando rebanadas. La variable mat podría eliminarse.
    mat = [list(range(i*n+1,i*n+n+1)) if i%2==0 else list(range(i*n+1,i*n+n+1))[::-1] for i in range(n)]
    return mat

def rellenarmatriz5():
    # Alternativa 5: Creamos la matriz desde la nada usando listas por comprensión
    #                y rangos crecientes o decrecientes para generar cada fila.
    #                La variable mat podría eliminarse.
    mat = [list(range(i*n+1,i*n+n+1)) if i%2==0 else list(range(i*n+n, i*n, -1)) for i in range(n)]
    return mat

def imprimirmatriz(mat):
    for fila in mat:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()
    print("-"*(len(mat)*3+1))  # Línea separadora proporcional al tamaño de la matriz

# Programa principal
n = int(input("Ingrese el tamaño de la matriz: "))
print()
# Se muestran cinco alternativas equivalentes. Bastaba con una sola.
matriz1 = [[0] * n for i in range(n)]
rellenarmatriz1(matriz1)
imprimirmatriz(matriz1)
matriz2 = [[0] * n for i in range(n)]
rellenarmatriz2(matriz2)
imprimirmatriz(matriz2)
matriz3 = rellenarmatriz3()
imprimirmatriz(matriz3)
matriz4 = rellenarmatriz4()
imprimirmatriz(matriz4)
matriz5 = rellenarmatriz5()
imprimirmatriz(matriz5)
