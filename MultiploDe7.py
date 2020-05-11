# Primer parcial - Tema 2, Ejercicio 2

def esmultiplode7(n):
    while n>9:
        n = n // 10 - n % 10 * 2
        if n < 0:
            n =- n
    if n==0 or n==7:
        return True
    else:
        return False

n = int(input("Ingrese un número entero: "))
if esmultiplode7(n):
    print(n, "es múltiplo de 7")
else:
    print(n, "no es múltiplo de 7")
  

