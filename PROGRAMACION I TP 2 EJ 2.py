# Escribir funciones para:
# a. Generar una lista de 50 números aleatorios del 1 al 100.
# b. Recibir una lista como parámetro y devolver True si la misma contiene algún
# elemento repetido. La función no debe modificar la lista.
# c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
# únicos de la lista original, sin importar el orden.
# Combinar estas tres funciones en un mismo programa.
import random
def generarLista (listaNumeros):
    for i in range (50):
        listaNumeros.append(random.randint(1,100))

def encontrarRepetidos (listaNumeros):
    for i in range (len(listaNumeros)):
        if lista.count(listaNumeros[i]) > 0:
            return True # PREGUNTA: ESTA BIEN RETORNAR DENTRO DE UN FOR?
    return false

def eliminarRepetidos(listaNumeros):
     listasinRep = listaNumeros
     for i in range (len(listaNumeros)):
         #no!!! listasinRep.remove(listaNumeros [i])
         while listaNumeros.count(listaNumeros[i]) > 1:
             listasinRep.remove(listaNumeros [i])
    return (listasinrep)
      

# Programa Principal
listaNumeros=[]
generarLista(listaNumeros)
print(listaNumeros)
print()
if encontrarRepetidos (listaNumeros) = True:
    print("Se encontraron numeros repetidos")
print()
Print(" Lista sin repetidos :",eliminarRepetidos (listaNumeros))











