#El método index permite buscar un elemento dentro de una lista, devolviendo la
#posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
#produce una excepción de tipo ValueError. Desarrollar un programa que cargue
#una lista con números enteros ingresados a través del teclado (terminando con -1)
#y permita que el usuario ingrese el valor de algunos elementos para visualizar la
#posición que ocupan, utilizando el método index. Si el número no pertenece a la
#lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
#proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

lista=[]
n=0
while n!=-1:
    try:
        n=int(input("Ingrese Numero Entero: -1 sale: "))
        lista.append(n)        
    except ValueError:
        print("Debe ser un numero entero")
        print()    
n=0
contError=1
while n!=-1:
    try:
        n=int(input("Ingrese el numero a buscar en la lista: -1 sale: "))                
        assert contError<3, "Se alcanzó el máximo número de errores"
        lista.index(n)        
        print("Numero %3d , encontrado!" %n)
    except ValueError:
        print("Numero %3d, no encontrado!" %n)
        print()
        contError+=1
    except AssertionError as mensaje:
        print(mensaje)
        break
    
    
