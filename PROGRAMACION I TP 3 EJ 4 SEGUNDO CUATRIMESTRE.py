"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa
el día de la semana (Lunes columna 0, Martes columna 1…) y cada fila
representa a una de sus fábricas.
Se solicita:
a. Crear una matriz con datos generados al azar de N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna.
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica.
"""
import random
def llenarmatriz (mat):
    #mat=[[random.randint(0,150)] for x in range(1,8) for i in range(n)]
    for i in range (n):
        for x in range(6):
            mat[i][x]=random.randint(0,150)
    return (mat)

def totalporfabrica(mat):
    tot=0
    for i in range(n):
        for x in range(6):
            tot=tot+mat[i][x]
        print(f"Fábrica: {i+1}, Total: {str(tot)}")
        tot=0
    return

def maxproduccion(mat):
    maximo=0
    for i in range(n):
        for x in range(6):
            if maximo<mat[i][x]:
                maximo=mat[i][x]
                fabrica=i+1
                dia=x+1            
    return(fabrica,dia,maximo)

def diamasproductivo(mat):
    cantidad=0
    maximo=0
    dia=0
    for c in range(6):
        for f in range(n):
            cantidad+=mat[f][c]
        if cantidad>maximo:
            maximo=cantidad
            dia=c
        cantidad=0
    return(dia)

def menorcantxfabrica(mat):    
    """menor cantidad fabricada por cada fábrica."""    
    for f in range(n):
        menor=mat[0][0]
        for c in range(6):
            if mat[f][c]<menor:
                menor=mat[f][c]
                fabrica=f        
        print(f"Fábrica: {f+1}, menor cantidad de unidades fabricada: {menor}")
    return

def menorcantxfabricaxcomprension(mat):
    menor = [min(elemento) for elemento in mat]
    for i, menor in enumerate(menor):
        print(f"Fábrica: {i+1}, menor cantidad de unidades fabricada: {menor}")
    return
"""
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x+' '+str(i) for (i,x) in enumerate(color) if i not in (0,4,5)] #enumerate lo vimos asi que se puede usar en parcial.
print(color)
"""

n=10
mat=[[0]*(6) for i in range(n)]
mat=llenarmatriz(mat)
print("Lista de fabricación: ", [x[0:n+1] for x in mat])
totalporfabrica(mat)

fabrica,dia,maximo=maxproduccion(mat)
print(f"Fabrica:{fabrica}, dia: {dia}, cantidad:{maximo}")
diamasprod=diamasproductivo(mat)+1
print(f"Dia mas productivo: {diamasprod}")
menorcantxfabrica(mat)
menorcantxfabricaxcomprension(mat)



    