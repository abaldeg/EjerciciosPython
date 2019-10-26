#Escribir la función comparar(a,b) que reciba como parámetros dos números
#enteros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1
#si el primero es menor que el segundo. Ejemplo: comparar(4,2) devuelve 1, y
#comparar(2,4) devuelve -1.

def fCompararNumeros(a,b):   
    
    if a > b:
        resultado = 1    
    else:
        resultado = -1
        
    return resultado

a=int(input("Ingrese número Entero a: "))
b=int(input("Ingrese número Entero b: "))

if fCompararNumeros(a,b) == 1:
    print ("El número",a,"es mayor al numero",b)
else:
    print ("El número",a,"es menor al numero",b)