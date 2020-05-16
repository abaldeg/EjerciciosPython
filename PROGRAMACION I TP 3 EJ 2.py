# PRACTICA 3 EJERCICIO 2

#FUNCIONES
def crearMatriz_1357(mat):
    n=len(mat)
    num=1
    for f in range(n):
        for c in range(f,n):
            if c==f:
                mat[f][c]=num
        num+=2

def crearMatriz_Diag_1_3_9_27(mat):        
    fin=-1 #nunca llega a -1 por la funcion range. 
    incremento=-1 #por el patron de la matriz, vamos de atrás para adelante.
    inicio=len(mat)-1 #arrancamos en el tamaño -1, porque usamos umeros negativos y pasamos por el 0.
    num=1
    for f in range(inicio,fin,incremento):
        mat[f][inicio-f]=num #Que columnas imprimo en cada fila
        print(f)
        num=num*3
        
def crearMatriz_4_33_222_1111(mat):        
    fin=-1 #nunca llega a -1 por la funcion range. 
    incremento=-1 #por el patron de la matriz, vamos de atrás para adelante.
    inicio=len(mat)-1 #arrancamos en el tamaño -1, porque usamos numeros negativos y pasamos por el 0.
    num=1
    acum=0
    # Ese deben imprimir todas las columnas, luego de a una menos.
    for f in range(inicio,fin,incremento):
        for c in range(inicio-acum,fin,incremento): #
            mat[f][c]=num            
        num+=1 #El numero se incrementa en cada fila
        acum+=1
        

def crearMatriz_Diag_4_3_2_1(mat):        
    fin=-1 
    incremento=-1 
    inicio=len(mat)-1 
    num=1
    c=inicio 
    for f in range(inicio,fin,incremento):
        mat[f][c]=num                
        c-=1
        num+=1

def crearMatriz_Diag_Con_Ceros(mat):
    # Alternativa 2: Recorremos todas
    # las filas y en cada una colocamos
    # los ceros correspondientes
    # según el número de fila en la que
    # nos encontramos
    tamaño = len(mat)
    for f in range(tamaño):
        for c in range(f, tamaño-f):
            mat[f][c] = 1
            mat[tamaño-f-1][c] = 2


def crearMatriz_8_4_2_1(mat):        
    fin=-1 
    incremento=-1 
    inicio=len(mat)-1 
    num=1
    c=inicio 
    for f in range(inicio,fin,incremento):
        for c in range(inicio,fin,incremento):
            mat[f][c]=num
        num*=2

def crearMatriz_0_1_0_2_0_3_0_4_0_5_0_6(mat):        
    fin=len(mat)
    incremento=1
    inicio=0
    num=1   
    for f in range(inicio,fin,incremento):
        for c in range(inicio,fin,incremento):
            if f%2==0 and c%2!=0:
                mat[f][c]=num
                num+=1
            elif f%2!=0 and c%2==0:
                mat[f][c]=num
                num+=1          


def crearMatriz_ZIGZAG_v2(mat):        
    fin=len(mat)
    incremento=1 
    inicio=0
    inicioCol=len(mat)-1
    finCol=len(mat)-2
    incCol=-1
    num=1    
    for f in range(inicio,fin,incremento):
        for c in range(inicioCol,finCol,incCol):
            mat[f][c]=num                        
            num+=1
        finCol-=1
        
        
def crearMatriz_ESPIRAL_v1(mat):
    tamaño=len(mat)
    inicio=0
    fin=0
    numero=1
    while numero <= tamaño*tamaño: #Mat 4x4: Ultimo numero 16
        fin += 1
        for j in range(inicio, tamaño-fin):
            i = inicio
            mat[i][j] = numero
            numero += 1
            imprimirmatriz(mat)
        for i in range(inicio, tamaño-fin):
            j = tamaño-fin
            mat[i][j] = numero
            numero += 1
            imprimirmatriz(mat)
        for j in range(tamaño-fin, inicio, -1):
            i = tamaño-fin
            mat[i][j] = numero
            numero += 1
            imprimirmatriz(mat)
        for i in range(tamaño-fin, inicio, -1):
            j = inicio
            mat[i][j] = numero
            numero += 1
            imprimirmatriz(mat)
        inicio += 1  

            
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
crearMatriz_ESPIRAL_v1(mat)
imprimirmatriz(mat)
