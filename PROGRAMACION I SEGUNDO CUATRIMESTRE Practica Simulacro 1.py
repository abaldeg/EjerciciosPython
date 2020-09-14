
"""
Desarrollar una o más funciones para generar una matriz con el patrón indicado, en el que cada columna
contiene alternativamente números impares y pares consecutivos comenzando desde un valor N impar.
El tamaño de la matriz se ingresa desde el teclado y se debe validar positivo. La función a crear
recibe el tamaño por parámetro utilizando valores por omisión se debe crear una matriz de 4x3 y recibe
por parámetro el valor inicial impar, por omisión 1 . Imagen de la matriz a crear adjunta a la tarea.

Escribir también un programa principal que invoque a la/s funcion/es y muestre por pantalla la matriz
obtenida.

Luego se solicita crear una lista por comprensión que contenga la suma de cada una de las
filas de la matriz. Imprimir todo por pantalla.
"""

def generamatrix(fila=4,columna=3,vii=1):    
    cont=vii
    for f in range(fila):
        for c in range(columna//2):
            mat[f][c]=cont
            cont+=1
    
    for fil in range(fila):
        for col in range(columna//2,columna):
            mat[fil][col]=cont
            cont+=1    
    return(mat)
                
def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()
    return

def sumarmatrix(mat):
    suma = [sum(elemento) for elemento in mat]
    print(suma)
    return
    

"""
Programa Principal
"""
f=int(input("Ingrese cantidad de filas de la matrix: "))
while f < 0:
    f=int(input("Ingrese cantidad de filas de la matrix: "))

c=int(input("Ingrese cantidad de columnas de la matrix: "))
while c < 0:
    c=int(input("Ingrese cantidad de columnas de la matrix: "))
    
vii=int(input("Ingrese valor inicial impar de la matrix: "))
while c < 0 or vii%2==0:
    vii=int(input("Ingrese valor inicial impar de la matrix: "))

mat = [[0]*(c) for i in range(f)]    
generamatrix(f,c,vii)
imprimirmatriz(mat)
sumarmatrix(mat)

