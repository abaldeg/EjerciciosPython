"""Desarrollar una o más funciones para generar una matriz con el patrón indicado, en el que cada columna
contiene alternativamente números impares y pares consecutivos comenzando desde un valor N impar.

El tamaño de la matriz se ingresa desde el teclado y se debe validar positivo.

La función a crear recibe el tamaño por parámetro utilizando valores por omisión se debe crear una
matriz de 4x3 y recibe por parámetro el valor inicial impar, por omisión 1 . Imagen de la matriz a crear adjunta a la tarea.
Escribir también un programa principal que invoque a la/s funcion/es y muestre por pantalla la matriz obtenida.
Luego se solicita crear una lista por comprensión que contenga la suma de cada una de las filas de la matriz.
Imprimir todo por pantalla."""

"""probar cuadrado, mas filas que columnas, y mas col que filas"""

def rellenarMatrix(f=4,c=3,vii=1):    
    """Rellena Matrix"""    
    contimp=vii
    contpar=vii+1
    for columna in range(c):
        if columna%2==0 or columna==0:
            for fila in range(f):
                mat[fila][columna]=contimp
                contimp+=2
        else:
            for fila in range(f):
                mat[fila][columna]=contpar
                contpar+=2
    return        

def imprimirmatriz(mat):
    """Imprime una matriz"""
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()    

mat=[]
f=int(input("Ingrese cantidad de filas de la Matriz: "))
while f <= 0:
    f=int(input("Ingrese cantidad de filas de la Matriz "))

c=int(input("Ingrese cantidad de columnas de la Matriz: "))
while c <= 0:
    c=int(input("Ingrese cantidad de columnas de la Matriz: "))

vii=int(input("Ingrese valor inicial impar: "))
while vii%2==0:
    vii=int(input("Ingrese valor inicial impar: "))    

mat= [[i]*c for i in range(f)]
rellenarMatrix(f,c,vii)
imprimirmatriz(mat)