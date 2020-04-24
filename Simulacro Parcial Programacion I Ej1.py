#Desarrollar un programa para ingresar un numero entero N, impar y no menor que 3, 
#verificando que se cumplan estas condiciones. Rechazar el número y volverlo a ingresar 
#en caso de no satisfacer alguna de ellas. Luego se solicita imprimir un patrón de aste-
#riscos con forma de triángulo sólido centrado, tal como se indica a continuación. Ejem-
#plo para N=5:

#funciones
def imprimir_Asteriscos(n):
    e=n
    a=n
    for i in range(n+1): #altura                
        for x in range(1,e): #espacios
            print(end="-")                     
        for j in range(0, i): #asteriscos
            print("*", end="")
        print("\r")
    return
    

#Programa Principal
n = int(input("Ingrese número impar y no menor que 3: "))
while n % 2 == 0 or n < 3:
    n = int(input("Ingrese número impar y no menor que 3: "))
imprimir_Asteriscos(n)
#print("*", end=' ')
#print("*", end='')

    
