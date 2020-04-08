# Práctica 3, ejercicio 3
# Contiene tres estrategias distintas

import random

def cargarmatriz1(mat):
    """ Estrategia 1:
        Utiliza una lista auxiliar para determinar
        si el número candidato ya fue cargado en
        la matriz, ya que cada número se carga
        simultáneamente en la matriz y en la lista
        auxiliar """
    n = len(mat)
    numeros = [ ]
    cantidad = n**2
    for f in range(n):
        for c in range(n):
            azar = random.randint(0,cantidad-1)
            while azar in numeros:
                azar = random.randint(0,cantidad-1)
            mat[f][c] = azar
            numeros.append(azar)

def estaenmatriz(mat, num):
    """ Verifica si el valor del parámetro n
        ya fue cargado en la matriz mat.
        Esta función se usa en cargarmatriz2 """
    n = len(mat)
    yaesta = False
    for f in range(n):
        if num in mat[f]:   # el operador in busca en toda la fila
            yaesta = True
            break
    return yaesta

def cargarmatriz2(mat):
    """ Estrategia 2:
        Rellena la matriz con números al azar
        verificando si el número candidato ya
        se encuentra cargado en la misma """
    n = len(mat)
    cantidad = n**2
    for f in range(n):
        for c in range(n):
            while True:   # repite hasta que salga con el break
                azar = random.randint(0,cantidad-1)
                if not estaenmatriz(mat, azar):
                    mat[f][c] = azar
                    break

def cargarmatriz3(n):
    """ Estrategia 3:
        Genera una lista con N² números al azar
        in repetir y luego los toma en porciones
        de N elementos usando rebanadas. Cada una
        de estas sublistas se agrega como una fila
        de la matriz """
    lista = [ ]
    # Generamos una lista con N² números al azar sin repetir
    for i in range(n**2):
        azar = random.randint(0,n**2-1)
        while azar in lista:
            azar = random.randint(0,n**2-1)
        lista.append(azar)
    # Ahora vamos tomando los numeros de la lista
    # en porciones de N elementos usando rebanadas
    # y un range con incremento N, y agregamos cada
    # sublista a la matriz
    mat = [ ]
    for i in range(0, n**2, n):
        mat.append(lista[i:i+n])
    return mat

def imprimirmatriz(mat):
    tam = len(mat)
    for f in range(tam):
        for c in range(tam):
            print("%3d" %mat[f][c], end ="")
        print( )

# Programa principal
m = [ ]
n = int(input("Tamaño de la matriz? "))
print( )
# Crear matriz
for i in range(n):
    m.append([0]*n)
cargarmatriz1(m)   # estrategia 1
imprimirmatriz(m)
print( )
print("-"*n*3)   # imprime línea de guiones proporcional al tamaño de la matriz
print( )
del m   # borramos la matriz creada con la estrategia 1
# Volver a crear matriz
m = [ ]
for i in range(n):
    m.append([-1]*n)
    # la matriz se inicializa con -1 porque es un
    # valor fuera del rango de los números al azar
cargarmatriz2(m)   # estrategia 2
imprimirmatriz(m)
print( )
print("-"*n*3)   # imprime línea de guiones proporcional al tamaño de la matriz
print( )
del m  # borramos la matriz creada con la estrategia 2
m = cargarmatriz3(n)   # estrategia 3
imprimirmatriz(m)