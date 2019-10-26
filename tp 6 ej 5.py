# En los siguientes ejercicios utilice la función del ejercicio I para ingresar datos en una lista y:
# Escribir una función para devolver la posición que ocupa un valor pasado como 
# parámetro, utilizando búsqueda secuencial en una lista desordenada. La función 
# debe devolver -1 si el elemento no se encuentra en la lista.
def CrearLista ():
    l = []
    pos=0
    n=int(input("Ingrese un número (-1 para finalizar)"))    
    while n != -1:        
        while (n < 1 and n != -1) or n > 20:
            n=int(input("Error. Ingrese un número entre 1 y 20 (-1 para finalizar)"))
        if n != -1:
            l.append(n)
            pos=pos+1
            n=int(input("Ingrese un número (-1 para finalizar)"))    
    return l

def BuscarLista (n,l):
    posicion=-1
    largo=len(l)
    for i in range(largo):
        if l[i]==n:
            posicion=l[i]       
    return posicion  
    

#Programa Principal
l=CrearLista()
n=int(input("Numero a buscar: "))
print("Posicion del numero buscado (-1 no se encontro)",BuscarLista(n,l))
