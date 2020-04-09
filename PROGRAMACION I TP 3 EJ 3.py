#Desarrollar un programa para rellenar una matriz de N x N con números enteros al
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.

import random

#Funciones
def rellenarMatriz (n,m):
    matriz=[]
    filas=n
    columnas=m
    numerorand=0
    
    #Inicializacion Matriz
    for f in range(filas):        
        matriz.append([0] * columnas)
    
    numerorand=random.randint(0,n*2)
    for f in range (filas):
        for c in range(columnas):
            if buscarRepetido(matriz,numerorand) == 0:
                matriz.append([f],[c])
         
      
def buscarRepetido (matriz,numero):
    filas=len(matriz)
    columnas=len(matriz[0])
    repetido=0
    f=0
    while repetido == 0 and f <==filas:        
        for c in range(columnas):
            if matriz[f,c]==numero:
                repetido==1        
        f=f+1
    return (repetido)


#Programa Principal