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
    estado=False
    for i in range (len(listaNumeros)):
        if listaNumeros.count(listaNumeros[i]) > 1:
            estado=True # PREGUNTA: ESTA BIEN RETORNAR DENTRO DE UN FOR?
    return estado

def eliminarRepetidos (listaNumeros):
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
listaRepetidos=[1,2,3,4,4,5,6,7,8,9]
repetidos=encontrarRepetidos(listaRepetidos)
if repetidos:
    print("Se encontraron numeros repetidos")
else:
    print("NO se encontraron numeros repetidos")
print()
print("Lista sin repetidos :",eliminarRepetidos (listaRepetidos))











