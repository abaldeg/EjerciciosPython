#por otro lado, muchas personas me dijeron que thompson suele evaluar pidiendo que hagas una matriz simulando un juego de ajedrez (no sé jugar al ajedrez, pero trato de explicarme):
#que emules el movimiento de la reina, de un peón, etc.


#Una linea de ropa deportiva cuenta con N productos para la venta, cuenta con un listado donde se visualiza para cada mes del año pasado la cantidad total de ventas por producto.
#El archivo adjunto presenta un ejemplo.

#Se solicita creando al menos una función para cada informe:
#1.    Crear una matriz con las ventas creadas al azar de N productos para todo el año. Considerando que la cantidad máxima de ventas es de 2000 unidades y la mínima es 0.
# N se icrea al azar entre 1 y 12 productos.
#Crear una funcion lambda para obtener el valor al azar entre 1 y 12. (25%)
#2.  Determinar si las ventas totales van decreciendo hasta mitad de año y creciendo hasta fin de año. (25%)
#3.  Cual fue el mes que realizó la mayor cantidad de ventas, dentro de ese mes cuál es el producto que menos se vendió. (En lo posible mostrar el nombre del mes contando con una lista de los
#nombres de los meses.) (25%)
#4.  Crear una lista las cantidades vendidas por cada mes para la cantidad de meses que se reciba por parámetro, por omision debe considerar la mitad de los meses de la matriz.
#Resolver utilizando rebanadas. (25%)

import random

#Funciones

#1
def crearMatVtas():    
    for i in range(0,13):
        mat.append([0]*13)    
     
    for col in range(1,13):
        mat[0][col]=col   
        
    for fil in range(1,13):
        r=lambda: random.randint(1,12) 
        mat[fil][0]=r()
        
    for f in range(1,13):
        for c in range(1,13):                                   
            mat[f][c]=random.randint(0,2000) 
            
    for f in range(0,13):
        for c in range(0,13):            
            print("%5d" %(mat[f][c]), end="-")      
        print()
   

#2 Determinar si las ventas totales van decreciendo hasta mitad de año y creciendo hasta fin de año. (25%)
#def calcularTendencia(mat):
#    n=len(mat)
#    for f in range(1,13):
#        for c in range(1,7):        
#            mat[f][c]= 
    

#3 Cual fue el mes que realizó la mayor cantidad de ventas, dentro de ese mes cuál es el producto que menos se vendió. (En lo posible mostrar el nombre del mes contando con una lista de los
#nombres de los meses.) (25%)
def calcularMesMayorVta(mat):
    n=len(mat)
    acum=0
    listaAux=[0]*13
    cm=0
    for c in range(1,13):
        for f in range(1,13):
            acum=acum+mat[f][c]
        if acum > max(listaAux):
            cm=c
        listaAux[c]=acum
        acum=0
    
    print(listaAux)            
    print("Ventas Máxima: ", max(listaAux))
    print("El mes en el que mas vendió:" ,cm)            

#4 Crear una lista las cantidades vendidas por cada mes para la cantidad de meses que se reciba por parámetro,
#por omision debe considerar la mitad de los meses de la matriz.
#Resolver utilizando rebanadas. (25%)
def calcularCantVtas(cantMeses=6):
    listaCantVtas=[0]*(cantMeses+1)
    acum=0
    #acum=sum(mat[1:][c])        
    print("Lista de Ventas: ", [x[1:cantMeses+1] for x in mat])
    
        
    


#Programa Principal
mat=[]
crearMatVtas()
#calcularTendencia()
calcularMesMayorVta(mat)
#calcularCantVtas()
calcularCantVtas(2)
    