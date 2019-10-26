#Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24.
def fFactorial(n):
    cont=n-1
    resultado=n
    while cont > 1:
        resultado=resultado*cont
        cont=cont-1
    return resultado

n=int(input("Ingrese número Entero: "))

print ("El factorial del numero",n,"es",fFactorial(n))
    