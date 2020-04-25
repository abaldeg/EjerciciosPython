#Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores
#de la lista.

#Funciones
def crearListaCuadrados(l,n):
    l=[0]*(n+1)
    for i in range(1,n+1):
        l[i]=i**2
    return (l)
    
def imprimirLista(l):
    l.sort(reverse=True)
    for i in range(1, 11):
        print(l[i])    

#Programa Principal
l=[]
n=int(input("Ingrese Ultimo valor de la lista: "))
l=crearListaCuadrados(l,n)
imprimirLista(l)