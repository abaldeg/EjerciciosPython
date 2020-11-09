"""
Desarrollar un programa para crear una matriz de NxM y muestre por pantalla representando la matriz obtenida.
El tamaño de la matriz debe establecerse como N x M. Debe rellenar la matriz según el patrón que visualiza
en la imagen adjunta.

Crear una lista con la suma de las filas de la matriz, sólo si la suma es par, caso contrario no incluirlo en la lista.

Resolver utilizando:

Técnica de listas por comprensión.
creando funciones modularizando el programa, teniendo en cuenta:
Al menos una función que utilice parámetros por omisión y una función lambda para resolver el problema.
"""

def crearmatriz(n=4,m=4):
    """Crea una matriz y la devuelve con ceros. Default: matrix 4x4."""    
    matriz = [[0] * m for i in range(n)]
    return matriz

def imprimirmatriz(matriz):
    """Imprime matriz pasada como parámetro."""
    n = len(matriz)
    m = len(matriz[0])
    for f in range(n):
        for c in range(m):
            print("%3d" %matriz[f][c], end="")
        print()

def rellenarmatrix(mat):
    """Rellena matriz según patrón. Ingresa matriz y devuelva la misma matriz rellena por patrón."""
    numimpar=1
    numpar=2
    cantf=len(mat)
    cantc=len(mat[0])
    
    for f in range(cantf):
        if f%2!=0:
            """es impar"""
            for c in range(cantc):
                mat[f][c]=numimpar
                numimpar+=2
        elif f%2==0 or f==0:
            """es par"""
            for c in range(cantc):
                mat[f][c]=numpar
                numpar+=2         
        
    return mat  

def sumarparesporcomprension(mat):
    """Recibe una matriz y devuelve una lista con las sumas que sean pares"""
    cantc=len(mat[0])
    espar=lambda suma: (suma % 2 == 0)    
    suma=[sum(f[0:cantc+1]) for f in mat if espar(sum(f[0:cantc+1]))]    
    return suma

# Programa principal
n=7
m=7
mat = crearmatriz(n,m)
mat=rellenarmatrix(mat)
imprimirmatriz(mat)
lista=sumarparesporcomprension(mat)
print(lista)







