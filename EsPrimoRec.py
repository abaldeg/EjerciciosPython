# Ejercicio 1

def esprimo(n, divisor=2):
    if n==divisor:
        return True
    else:
        return False if n%divisor==0 else esprimo(n, divisor+1)

# Programa principal
n = int(input("Ingrese un número entero: "))
if esprimo(n):
    print(n,"es primo")
else:
    print(n,"no es primo")