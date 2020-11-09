# Ejercicio 9 Practica 1
'''Resolver el siguiente problema diseñando y utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar el camión de reparto.
La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500 kilogramos).
En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una.
Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo.

Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden
llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión
no debe ser inferior al 80%; en caso contrario el camión no serán despachado por su alto costo. '''

import random

# Funciones

def clasificacionNaranjas(totalNaranjas):
    '''
        pre: Ingresa la cantidad de naranjas de toda la cosecha y las selecciona segun su peso
        pos: retorna la cantidad de naranjas aptas para transporte, jugo y el peso de las naranjas que se van a transportar
             en gramos        
        '''
    contador=0
    naranjasAtransportar,naranjasJugo=0,0
    pesoTotalNaranjas=0
    while (contador<totalNaranjas):
        pesoNaranja=random.randint(150,350)
        if(pesoNaranja>=200 and pesoNaranja<=300):
            naranjasAtransportar+=1
            pesoTotalNaranjas+=pesoNaranja
        else:
            naranjasJugo+=1            
        contador+=1
    return naranjasAtransportar,naranjasJugo,pesoTotalNaranjas


def camionesNecesarios(pesoTotal):
    '''
    pre: Con el peso total de las naranjas,el porcentaje minimo de transporte y la capacidad de cada camion calculo
         numero de camiones necesarios
    pos: Retorna total de camiones necesarios para transportar y la cantidad de naranjas sobrantes para proximo viaje
    
    '''
    totalCamiones=pesoTotal//500
    pesoRestante=pesoTotal%500
    
    restante=0
    if(pesoRestante<400):
        restante=pesoRestante
    else:
        totalCamiones+=1
    
    return restante,totalCamiones
        


# Programa principal

cantNaranjasCosechadas=int(input("Cantidad de naranjas cosechadas: "))
print()

transporte,jugo,peso=clasificacionNaranjas(cantNaranjasCosechadas)
print("Cantidad de naranjas aptas para transporte son",transporte)
print("Cantidad de naranjas aptas para jugo son: ",jugo)
print()

if(cantNaranjasCosechadas>=100):
    print("Cantidad de cajones que se pueden llenar para transportar es: ",transporte//100," cajones")
    print("Cantidad de naranjas sobrantes para un proximo envio es: ",transporte%100," naranjas")
    
    print()
    sobrante,camiones=camionesNecesarios(transporte)
    print("Camiones necesarios para transportar ",camiones)
    print("Cantidad de naranjas sobrantes para un proximo envio ",sobrante," naranjas")
    
else:
    print("La cantidad de naranjas cosechadas",cantNaranjasCosechadas," naranjas no son suficientes para llenar un cajón")
    
    
    
'''PRUEBA DE ESCRITORIO
como los valores que cada naranja toma son aleatorios no puedo dar un valor exacto para la prueba de escritorio pero los datos
de abajo ilustran un posible caso y su solución.

Cantidad de naranjas cosechadas: 1000

Cantidad de naranjas aptas para transporte son 495
Cantidad de naranjas aptas para jugo son:  505

Cantidad de cajones que se pueden llenar para transportar es:  4  cajones
Cantidad de naranjas sobrantes para un proximo envio es:  95  naranjas

Camiones necesarios para transportar  1
Cantidad de naranjas sobrantes para un proximo envio  0  naranjas'''

