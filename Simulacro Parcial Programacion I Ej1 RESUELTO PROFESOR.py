# Simulacro Primer Parcial P1 - Ejercicio 1

while True:
    n = int(input("Ingrese un número entero impar y mayor o igual a 3: "))
    if n<3 or n%2==0:
        print("Número inválido. Intente nuevamente.")
        continue
    break
espaciosizq = n-1
# Primera fila
for i in range(espaciosizq):
    print("-", end="")
print("*")
# laterales
for i in range(n-2):
    espaciosizq = espaciosizq - 1
    for j in range(espaciosizq):
        print("1", end="")
    for j in range(i*2+3):
        print("*", end="")
    print( )    
# Ultima fila
for i in range(n*2-1):
    print("*", end="")