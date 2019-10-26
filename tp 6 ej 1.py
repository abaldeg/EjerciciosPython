#Ejercicio I: Escribir una función para ingresar desde el teclado una serie de números entre I 
#y 20 y guardarlos en una lista. En caso de ingresar un valor fuera de rango el 
#programa mostrará un mensaje de error y solicitará un nuevo número. para fi- 
#nalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y 
#devuelve la lista cargada (o vacía, SI el usuario no ingresó nada) como valor de 
#retorno.

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

l=CrearLista()
largo=len(l)
for i in range(largo):
    print("Elemento ", l[i],end=" ")

        
        
