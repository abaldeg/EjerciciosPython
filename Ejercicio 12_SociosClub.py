# Ejercicio 12 practica 2
'''Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos.
Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.'''

# Funciones
def contadorDigitos(numero):
    '''
    pre:Ingresa un número 
    pos:me retorna la cantidad de dígitos que tiene
    
    '''
    contDig=0
    while(numero!=0):
        ultimoDig=numero%10
        numero=numero//10
        contDig+=1
    return contDig

def validacionDigitos(numSocio):
    '''
    pre: Ingresa el número de socio y valida si tiene mas de 5 dígitos
    pos: me retorna el número de socio validado
    
    '''
    digitos=contadorDigitos(numSocio)
    while(digitos!=5): # Hago validacion de 5 dígitos
        print()
        print("El código ingresado es incorrecto")
        numSocio=int(input("Número de socio (5 Dígitos): "))
        digitos=contadorDigitos(numSocio)
    numValidado=numSocio
    return numValidado
    
def cargarListaSocios(numSocio):
    '''
    pre:Ingresa un número y lo agrega a una lista vacia
    pos: Me retorna una lista cargada
    
    '''
    numerosSocios=[]
    while(numSocio!=0):
        numeroValidado=validacionDigitos(numSocio)
        numerosSocios.append(numeroValidado)
        numSocio=int(input("Número de socio (5 Dígitos): "))
    return numerosSocios

def cantidadIngresosClub(lista): # Guardo en una lista los numeros de socio sin repetir
    '''
    pre: Ingresa una lista y busca los números que no estan repetidos
    pos: me retorna una nueva lista con los numeros sin repetirse 
    
    '''
    listaNueva=[]
    for i in lista:
        if  i not in listaNueva:
            listaNueva.append(i)
    return listaNueva

def mostrarNumeroDeIngresos(listaOri):
    '''
    pre: Ingresan dos lista y las compara para buscar la cantidad de veces que se repite un número
    pos: Muestra por pantalla la cantidad de ingresos del socio y su respectivo código
    
    '''
    listaNueva=cantidadIngresosClub(listaOri)
    for i in range (len(listaNueva)):
        contador=0
        for j in range(len(listaOri)):
            if(listaNueva[i]==listaOri[j]):
                contador+=1
        print("El socio numero ",listaNueva[i]," ingreso al club ",contador," veces")

def eliminarIngresos(lista,numEliminar):
    '''
    pre: Ingresa una lista y el número que quiero eliminar de la lista
    pos: retorna una lista nueva sin los números repetidos y tambien cuantos de ellos fueron eliminados
    
    '''
    numeroParaEliminar=validacionDigitos(numEliminar)
    eliminados=0
    for i in lista:
        if(i==numEliminar):
            lista.remove(numeroParaEliminar)
            eliminados+=1
    return lista,eliminados

def mostrarConIngresosEliminados(listaOri,numEliminar):
    '''
    pre: Ingresan dos listas y las compara buscando cuantas veces se repite un número de una en la otra
    pos: Muestra por pantalla el socio y la cantidad de veces de ingreso que se elimino
    
    '''
    listaNuevaEliminados,eliminados=eliminarIngresos(listaOri,numEliminar)
    listaEliminadosSinRepetir=cantidadIngresosClub(listaNuevaEliminados)
    for i in range (len(listaEliminadosSinRepetir)):
        contador=0
        for j in range(len(listaNuevaEliminados)):
            if(listaEliminadosSinRepetir[i]==listaNuevaEliminados[j]):
                contador+=1
        print("El socio numero ",listaEliminadosSinRepetir[i]," ingreso al club ",contador," veces")
    print()
    print("Se eliminaron",eliminados,"ingresos correspondientes al socio número",numEliminar)

        
    
    

# Programa principal

numSocio=int(input("Ingrese el número de socio (5 Dígitos): "))
ListaIngresosSocios=(cargarListaSocios(numSocio)) # Guarda todos los números de socios que se ingresaron 

# ListaIngresosSocios=[11111, 22222, 11111, 22222, 11234, 11111]  # Para prueba de escritorio, esta al final

print("___________________________________________________________________")
print("Número de ingresos de cada socio")
print()
mostrarNumeroDeIngresos(ListaIngresosSocios)
print()
numSocioEliminar=int(input("Ingrese el número de socio que desea eliminar "))
print()
print("Numero de ingresos de cada socio (Ya eliminado el que se dio de baja)")
print()
mostrarConIngresosEliminados(ListaIngresosSocios,numSocioEliminar)

''' PRUEBA DE ESCRITORIO

Se ingresa por teclado
11111, 22222, 11111, 22222, 11234, 11111

Número de ingresos de cada socio

El socio numero  11111  ingreso al club  3  veces
El socio numero  22222  ingreso al club  2  veces
El socio numero  11234  ingreso al club  1  veces

Ingrese el número de socio que desea eliminar 11111

Numero de ingresos de cada socio (Ya eliminado el que se dio de baja)

El socio numero  22222  ingreso al club  2  veces
El socio numero  11234  ingreso al club  1  veces

Se eliminaron 3 ingresos correspondientes al socio número 11111'''


