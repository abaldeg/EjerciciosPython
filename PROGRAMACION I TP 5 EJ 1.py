# Trabajo Practico numero 5, ejercicio 1
#Desarrollar una función para ingresar a través del teclado un número natural. La
#función rechazará cualquier ingreso inválido de datos utilizando excepciones y
#mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
#número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
#éste sea correcto. Escribir también un programa que permita probar el correcto
#funcionamiento de la misma

def ingresarNumNatural():
    while True:
        try:
            n=int(input("Ingrese Numero Natural: "))
            assert 0 < n
            break
        except ValueError:
            print("Debe ser un numero entero")
            print()
        except AssertionError:
            print("El numero debe ser mayor a 0")
            print()
    return(n)

print(ingresarNumNatural())