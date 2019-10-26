#Desarrollar la función signo(n), que reciba un número entero y devuelva un 1, -1
#o 0 según el valor recibido sea positivo, negativo o nulo.
def fCalcularSigno(n):   
    
    if n < 0:
        resultado=-1
    elif n == 0:
        resultado=0
    else:
        resultado=1
        
    return resultado

n=int(input("Ingrese número Entero: "))

print ("El signo del numero",n,"es",fCalcularSigno(n))
    