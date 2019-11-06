# cargar lista
import random
def cargarlista(lista,elementos):
    i=0
    while i < elementos:
        lista.append(random.randint(1,9))
        i=i+1
    return lista

# ordenar lista
def ordenarlista(lista):
    largo=len(lista)
    for i in range (largo-1):
        for j in range (i+1,largo):
            if lista[i] > lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista
     

# buscar elementos
def buscarlista (lista,numero):
    i=0
    while i < len(lista) and lista[i] != numero:
        i=i+1
    if i < len(lista):
        return i
    else:
        return -1
    
# eliminar elementos
def eliminarelementos(lista):
    i=0
    while i < len(lista):
        if lista[i]==lista[i+1]:
            del lista[i]
        i=i+1

# Imprimir lista


# Calcular biciesto
def calcularbiciesto(año):
    if (año % 4 == 0 and año % 100 == 0) or año % 400 == 0:
        bicisto=True
    else:
        biciesto=false
   

# Extraer digitos de un numero
def extraerdigitos(numero):
    numero=0
    while numero <= 10:
        digito=numero%10
        print (digito)
        numero=numero/10
    print (numero)
    

# Ordenar dos listas


# coincidir por valor y posicion
def comparalistas(lista1,lista2):
    largo1=len(lista1)
    largo2=len(lista2)
    exacto=0
    aprox=0
    for i in range(largo1):
        for j in range (largo2):
            if lista1[i]==lista2[j] and i==j:
                exacto=exacto+1
            elif lista1[i]==lista2[j]:
                aprox=aprox+1
    return exacto, aprox
                
            
    


