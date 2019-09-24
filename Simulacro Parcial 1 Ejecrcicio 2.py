"""Ejercicio 2:
Ingresar un número positivo. Rechazar el número y volverlo a ingresar en caso de ser negativo.
Luego se solicita imprimir un mensaje indicando si dicho número es oblongo o no. Se dice que un número es oblongo
cuando se obtiene como resultado de multiplicar dos números enteros consecutivos.
Ejemplos:
2 es oblongo porque resulta de multiplicar 1*2
6 es oblongo porque resulta de multiplicar 2*3
20 es oblongo porque resulta de multiplicar 4*5
24 no es oblongo porque ningún producto de dos enteros consecutivos da 24
Luego informar si el numero ingresado es primo.
Un número primo es aquel que unicamente es divisible por si mismo y por la unidad."""

nro=int(input("Ingrese un nro entero positivo "))
while nro<0:
    nro=int(input("Ingrese un nro entero positivo "))
base=1
producto=0
producto = base * (base+1)
while producto<nro:
    base=base+1
    producto = base * (base+1)
if producto==nro:
    print ("el nro es oblongo", nro)
else:
    print ("el nro NO es oblongo", nro)
divisor=1
cant=0
while divisor<nro:
    if nro%divisor == 0:
        cant=cant+1
    divisor=divisor+1
if cant>=2:
    print ("El nro NO es primo",nro)
else:
    print("El nro  es primo",nro)

    
    
    
    


    
    


