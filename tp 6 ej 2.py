# En los siguientes ejercicios utilice la función del ejercicio I para ingresar datos en una lista y:
# Calcular la suma de los números de una lista.

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
suma=0
for i in range(largo):
    suma=l[i]+suma

print("La suma de los elementos de la lista es: ", suma)