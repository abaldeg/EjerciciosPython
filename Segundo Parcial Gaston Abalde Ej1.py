"""
EJERCICIO 1

Crear una función recursiva para crear una nueva cadena que contenga sólo los caracteres alfabéticos
y espacios de otra cadena. Se espera que lo resuelva mediante una función recursiva.
Desarrollar un programa para ingresar frases  hasta que sea vacía y para cada frase mostrar
la cadena creada con la función recursiva.
Ejemplo: Programar en Python 3.1 me encanta! la función recursiva debe retornar:
Programar en Python me encanta en una variable de tipo cadena de caracteres.

"""
def crearCadena(cadena,cadenalf=""):
    """Ingresa una cadena de caracteres y los devuelve sin números. Se da por supuesto que los dígitos numéricos siempre están separados por espacios. hola9hola no esválido."""
    if len(cadena)==0:
        return ""
    else:
        letra=cadena[0].lower()
        if letra.isalpha() or letra==" ":
            return letra+crearCadena(cadena[1:])
        else:
            return crearCadena(cadena[2:])    

#Programa principal
frase=input("Ingrese Frase: ")
while frase !="":
    cadenafinal=crearCadena(frase)
    print(f"Cadena con caracteres alfabéticos y espacios: {cadenafinal}")
    print()
    frase=input("Ingrese Frase: ")        
    print()
