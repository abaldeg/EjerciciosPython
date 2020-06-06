# Práctica 5, ejercicio 1

def ingresarnumeronatural():
    while True:
        cad = input("\nIngrese un número natural: ")
        try:
            n =float(cad)
            assert n>=0, "El número debe ser positivo."
            assert n==int(n), "El número debe ser entero."
            break
        except ValueError:
            print("Sólo se permiten números.")
            print("Intente nuevamente.")
        except AssertionError as error:
            print(error)
            print("Intente nuevamente.")
    return int(n)

# Programa principal
a = ingresarnumeronatural()
print("El número ingresado es", a)
            
        
