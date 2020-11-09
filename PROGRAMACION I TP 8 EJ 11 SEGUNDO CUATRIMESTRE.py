"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras
"a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados.
Desarrollar un programa para leer una frase e invocar a la función por cada
palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales
hallada.
"""
def contarvocales(palabra):
    vocales="aeiou"
    #cantvocales={"a":0,"e":0,"i":0,"o":0,"u":0}
    cantvocales=dict.fromkeys(vocales,0)
    for letra in palabra:
        #cantidad=cantvocales.get(letra,-10)+1
        if letra in vocales:
            cantvocales[letra] = cantvocales.get(letra, 0) + 1                  
    return cantvocales

cant=0
frase=input("Ingrese Frase: ")
frase=frase.split(" ")
for p in frase:
    print(p)
    print(contarvocales(p))
    
    
    
