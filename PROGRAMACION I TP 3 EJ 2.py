# PRACTICA 3 EJERCICIO 2

#FUNCIONES
def crearMatriz_1357(mat):
    n=len(mat)
    num=1
    for f in range(n):
        for c in range(f,n):
            if c==0 or c==f:
                mat[f][c]=num
        num+=2

def crearMatriz_Diag_1_3_9_27(mat):        
    fin=-1 #nunca llega a -1 por la funcion range. 
    incremento=-1 #por el patron de la matriz, vamos de atrás para adelante.
    inicio=len(mat)-1 #arrancamos en el tamaño -1, porque usamos umeros negativos y pasamos por el 0.
    num=1
    for f in range(inicio,fin,incremento):
        mat[f][inicio-f]=num
        print(f)
        num=num*3
        
def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()  


#PROGRAMA PRINCIPAL
n=4
mat=[[0]*n for i in range(n)]
imprimirmatriz(mat)
print()
#crearMatriz_1357(mat)
crearMatriz_Diag_1_3_9_27(mat)
imprimirmatriz(mat)
