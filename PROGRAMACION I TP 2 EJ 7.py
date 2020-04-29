#Escribir una función que reciba una lista como parámetro y devuelva True si la lista
#está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
#ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
#además un programa para verificar el comportamiento de la función.

#Funciones
def analizaOrdenLista(lista):
    ordenada=True
    if len(lista) <= 1:
        #
        print ("La lista esta vacía o tiene un solo elemento. ", end="")
        ordenada=False
    else:
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                ordenada=False    
    return(ordenada)
#Programa Principal
lista=[1,2,3]
print(analizaOrdenLista(lista))
lista=[2,1,3]
print(analizaOrdenLista(lista))
lista=[2]
print(analizaOrdenLista(lista))
