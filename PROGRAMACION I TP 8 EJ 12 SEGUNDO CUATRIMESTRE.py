"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""
import random
def crearlistaPrecios():
    productos = {x:random.randint(1,10000) for x in range(1,101)} 
    return productos

def incrementaPrecios(productos):
    """Incrementa un diccionario de precios en un 15%. Devuelve el diccionario con el precio incrementado."""
    for producto in productos:
        productos[producto]=float(productos[producto]*1.15)        

def imprimirPrecios(productos):
    for producto in productos:
        print(f"Producto: {producto}, precio: " + format(productos[producto],'.2f')) 
    return 

def precioMasCaro(productos):
    listavalores=(productos.values())    
    return max(listavalores)

"""
Programa Principal
"""
listaPrecios=crearlistaPrecios()
imprimirPrecios(listaPrecios)
print()
incrementaPrecios(listaPrecios)
imprimirPrecios(listaPrecios)
print()
print(f"El precio mas caro es: {precioMasCaro(listaPrecios)}")
