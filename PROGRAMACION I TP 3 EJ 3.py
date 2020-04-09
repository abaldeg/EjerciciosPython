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
            if buscarNoRepetido(matriz,numerorand)
         
      
def buscarNoRepetido (matriz,numero):
    filas=len(matriz)
    columnas=len(matriz[0])
    sinrepetido=True
    f=0
    while sinrepetido and f <==filas:        
        for c in range(columnas):
            if matriz[f,c]==numero:
                sinrepetido==False        
        f=f+1
    return (sinrepetido)


#Programa Principal