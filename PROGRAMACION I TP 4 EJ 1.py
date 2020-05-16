#Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
#utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
#funcionamiento

#Funciones
def deterinarCapicua(cadena):
    mitad=len(cadena)//2
    if cadena[:mitad]==cadena[:(mitad)*(-1)-1:-1]: #El inicio es -1 y es el primer parametro, el valor final es la mitad y es el segundo parametro.        
        return True
    else:
        return False  
#Programa Principal
cadena="123321"
print(deterinarCapicua(cadena))
cadena="123123"
print(deterinarCapicua(cadena))