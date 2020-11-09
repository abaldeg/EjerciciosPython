"""Escribir un programa que permita ingresar dos cadenas de caracteres no vacías, cada cadena debe contener al menos 3 palabras.
Crear una nueva cadena intercalando las palabras de ambas cadenas, donde cada palabra solo tiene en mayúscula la primer letra.
Solo un espacio entre cada palabra, se pueden dejar los símbolos ingresados. 
Ejemplo:
cadena1 ingresada es "Hola como estas?"
cadena2 ingresada es "bien, estoy programando!"
resultado debe ser "Hola Bien, Como Estoy Estas? Programando!"
Pueden tener distinta cantidad de palabras cada cadena.
"""
cad1=input("Ingrese cadena 1: ")
cad1=cad1.lower()
cad1=cad1.title()
cad1=cad1.split()
while len(cad1)<3:
    cad1=input("Ingrese cadena 1: ")
    cad1=cad1.lower()
    cad1=cad1.title()
    cad1=cad1.split()
    
cad2=input("Ingrese cadena 2: ")
cad2=cad2.title()
cad2=cad2.split()
while len(cad2)<3:
    cad2=input("Ingrese cadena 2: ")
    cad2=cad2.lower()
    cad2=cad2.title()
    cad2=cad2.split()
tam1=len(cad1)
tam2=len(cad2)
i=0
intercalado=[]
if tam1<tam2:
    #recorro la cadena mas chica
    while i < len(cad1):
        intercalado.append(cad1[i])
        intercalado.append(cad2[i])
        i+=1
else:
    #recorro la cadena mas chica
    while i < len(cad2):
        intercalado.append(cad1[i])
        intercalado.append(cad2[i])
        i+=1    
intercalado=" ".join(intercalado)
print(intercalado)


        
        
        