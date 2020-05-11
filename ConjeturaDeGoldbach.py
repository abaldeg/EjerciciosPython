def esprimo(n):
    divisor = 2
    while (divisor<n and n%divisor!=0):
        divisor = divisor + 1
    if divisor<n:
        return False
    else:
        return True


n = int(input("Ingrese un número entero par: "))
while n%2!=0:
    n = int(input("El número debe ser par. Intente nuevamente: "))
n1 = 1
while n1 <= n/2:
    n2 = n - n1
    if esprimo(n1) and esprimo(n2):
        print(n1,"+",n2)
    n1 = n1 + 1
print()
    