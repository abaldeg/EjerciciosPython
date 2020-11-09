"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido
del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes."""
numeros=set()
numeros={0,1,2,3,4,5,6,7,8,9}
num=int(input("Número a eliminar:"))
while True:
    try:        
        assert num in numeros
        numeros.remove(num)
        print(numeros)
        print()
                
    except ValueError:
        print("Debe ser un numero entero")
        
    except AssertionError:
        print("El numero no está en el conjunto de números")
        print()
    finally:        
        num=int(input("Número a eliminar:"))
        if num == -1:
            break