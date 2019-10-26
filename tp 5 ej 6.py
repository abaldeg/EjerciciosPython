#Devolver True si el número entero recibido como primer parámetro es múltiplo
#del segundo, o False en caso contrario.
#Ejemplo: esmultiplo(40,8) devuelve True
#y es multiplo(50,3) devuelve False.

def fVerificarMultiplo(a,b):    
    
    if a % b == 0:
        Multiplo = True
    else:
        Multiplo = False
    
    return Multiplo

a=int(input("Ingrese número a: "))
b=int(input("Ingrese número b: "))

if fVerificarMultiplo(a,b):
    print (a,"es múltiplo de ",b)
else:
    print (a,"no es múltiplo de ",b)
    
    