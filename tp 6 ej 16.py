
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
        if numerousuario > numero:
            print("El numero ingresado es mayor")
        elif numerousuario < numero:
            print("El numero ingresado es menor")
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

        

        
    

    