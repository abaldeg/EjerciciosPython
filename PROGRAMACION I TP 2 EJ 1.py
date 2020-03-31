# PROGRAMACION I TP 2 EJ 1
#Trabajo Práctico 2: Listas 
#I. Desarrollar cada una de las siguientes funciones y escribir un programa que permi- 
#ta verificar su funcionamiento imprimiendo la lista luego de invocar a cada función: 
#
#Cargar una lista con números al azar de cuatro dígitos. La cantidad de ele- 
#mentos también será un número al azar de dos dígitos. 
#
#Calcular y devolver la sumatoria de todos los elementos de la lista anterior. 
#
#Eliminar todas las apariciones de un valor en la lista anterior. El valor a elimi- 
#nar se ingresa desde el teclado y la función Io recibe como parámetro.
#
#Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
#auxiliares. Un ejemplo de lista capicúa es [5O, 17, 91, 17, 5O].

import random
# Funciones
def cargarLista (listaRandom):    
    for i in range (random.randint(10,99)):
                    listaRandom.append(random.randint(1000,9999))
            
    return

def sumarLista (listaRandom):
    return(sum(listaRandom))

def eliminarElemento (listaRandom,e):    
    while e in listaRandom:
        listaRandom.remove(e)
    return
    

# Programa Principal
listaRandom=[]
cargarLista(listaRandom)
print ("Lista: ", listaRandom)
print()
print ("Suma de la lista: ", sumarLista(listaRandom))
print()
e=int(input("Indique el elemento a eliminar: "))
print("Eliminando elemento ", e, "de la lista.")
eliminarElemento (listaRandom,e)
print("Elemento ", e, "eliminado de la lista.")
print()
print ("Lista sin elemento ",e,": ", listaRandom)


                                             
                    