# Ejercicio 17: 
# 
# Modificar el programa anterior para que las pistas brindadas por el programa no 
# sean del tipo "es mayor" o -es menor" sino "M dígitos correctos y N dígitos 
# aproximados". Se considera que un dígito es correcto cuando tanto su valor 
# como Su posición coinciden con los del número secreto, mientras que un dígito 
# es aproximado cuando coincide el valor pero no su posición. Ejemplos: 
# Número secreto: 5739 
# Intento L: 1234 -> I correcto 
# Intento 2: 5678 I correcto y I aproximado 
# Intento 3: 9375 4 aproximados 

import random

def generarnumero():
    return random.randint(1000,9999)

def ordenarlista(listanombres,listaintentos):
    largo=len(listaintentos)
    for i in range(largo-1):
        for j in range (i+1,largo):
            if listaintentos[i] > listaintentos[j]:
                aux=listaintentos[i]
                aux2=listanombres[i]
                listaintentos[i]=listaintentos[j]
                listanombres[i]=listanombres[j]
                listaintentos[j]=aux                
                listanombres[j]=aux2
    return 

def busquedasecuencial (numero,numerousuario):
    numerolista = [int(x) for x in str(numero)]
    numerousuariolista = [int(x) for x in str(numerousuario)]
    correcto=0
    aprox=0    
    i=0
    u=0
    
    while u < len(numerousuariolista):
        while i < len(numerolista) and numerolista[i]!=numerousuariolista[u]:            
            i=i+1
        if i < len(numerolista):
            if numerolista[i] == numerousuariolista[u] and i==u:
                correcto=correcto + 1
            else:
                aprox = aprox + 1
        i=0
        u=u+1
    
    return correcto,aprox    

trampa=True
listaintentos=[]
listanombres=[]
continuarjuego=True
respuesta=''

while continuarjuego:
    numero = generarnumero()
    if trampa:
        print ("Esto es trampa!!",numero)
    numerousuario=int(input("Ingrese numero:"))    
    intentos=1
    while numerousuario != numero and numerousuario != -1:                
#         if numerousuario > numero:
#             print("El numero ingresado es mayor")
#         elif numerousuario < numero:
#             print("El numero ingresado es menor")
          
        print("Cantidad de dígitos correctos y aproximados:", busquedasecuencial(numero,numerousuario))                   
            
        intentos=intentos+1
        numerousuario=int(input("Ingrese numero:"))
    if numerousuario == -1:
        print("Te rendiste!!")
    else:
        print("Cantidad de intentos", intentos)
        if len(listaintentos) < 5:
            nombre=input("Ingrese su nombre:")
            listaintentos.append(intentos)
            listanombres.append(nombre)
            ordenarlista(listanombres,listaintentos)            
            print("Felicitaciones estas en el top 5")
        else:
            if intentos < listaintentos[4]:
                nombre=input("Ingrese su nombre:")
                listanombres[4] = nombre
                listaintentos[4] = intentos
                ordenarlista(listanombres,listaintentos)
                print("Felicitaciones estas en el top 5")
    respuesta=input("Queres continuar con el juego? (s/n)")
    if respuesta=='n':
        continuarjuego=False
    else:
        continuarjuego=True

largo=len(listaintentos)
print ()
print ("Ranking de los cinco mejores jugadores")
print ()
for i in range(largo):
    print("Jugador:",listanombres[i],".Sus intentos:",listaintentos[i])

        

        
    

    
