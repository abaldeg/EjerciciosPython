#Escribir un programa que tenga una función que devuelva un número al azar entre A y B cuyos 
# dígitos no se repitan(ej: 121 no es válido porque se repite el 1). A y B deben ingresarse por teclado
#y A siempre debe ser menor que B, en caso contrario invertir los números.
import random

def DevolverNumeroAlAzar(a,b):
    while True:
        numAzar = random.randint(a,b)
        numerosRepetidos = [1 for num in str(numAzar) if str(numAzar).count(num) > 1]
        if len(numerosRepetidos) == 0:
            return numAzar


def ingresarDosNumerosValidos():
    while True:
        try:
            a = int(input("Ingrese un número: "))
            b = int(input("Ingrese otro número: "))
            if a >= b:
                c = b
                b = a
                a = c
            return a,b
        except:
            print("Numeros ingresados no válidos.")


a,b = ingresarDosNumerosValidos()
numero = DevolverNumeroAlAzar(a,b)
print("Número generado: ", numero)