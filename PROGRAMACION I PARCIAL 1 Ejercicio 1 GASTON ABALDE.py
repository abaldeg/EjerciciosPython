#Escribir un programa para generar e imprimir una matriz de N x N con números enteros
#correlati-vos a partir de 1 siguiendo un patrón en zig-zag por columnas.
#Imprimir la matriz por pantalla respetando el formato de la misma.
#El programa debe funcionar para cualquier valor de N, el que se ingresa por teclado.
#Ejemplo para N=5


#Funciones
def generarMatriz(matriz,n):           
    cont=0
    for c in range(1,n+1):
        if c%2==0:
            #Columna Par
             for f in range(1,n+1):
                matriz[f][c]=cont
                cont=cont+1                              
        else:
            #Columna ImPar
            for f in range(1,n+1):
                matriz[f][c]=cont
                cont=cont+1        
     
def imprimirMatriz(matriz):    
    for f in range(1,n+1):
        for c in range(1,n+1):            
            print("%5d" %(matriz[f][c]), end="")
        print()
    
#Programa Principal
matriz=[]
#Inicializo Matriz con 0   
n=int(input("Ingrese Valor N: "))
matriz = [[0]*(n+1) for i in range(n+1)]
generarMatriz(matriz,n)
imprimirMatriz(matriz)


    