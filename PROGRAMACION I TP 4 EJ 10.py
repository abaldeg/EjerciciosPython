# Escribir un programa que permita ingresar una cadena de caracteres e imprima un
# mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo, si se
# ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números

cadena=input("Ingrese cadena: ")
contcad=0
contnum=0
for c in cadena:
    if c.isalpha():
        contcad+=1
    elif c.isdigit():
        contnum+=1
print(contcad)
print(contnum)
        
        

