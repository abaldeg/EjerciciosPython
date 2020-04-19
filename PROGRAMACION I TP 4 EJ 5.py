#Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
#una frase y un entero N, y devuelva otra cadena con las palabras que tengan
#N o más caracteres de la cadena original. Escribir también un programa para
#verificar el comportamiento de la misma. Hacer tres versiones de la función, para
#cada uno de los siguientes casos:
#a. Utilizando sólo ciclos normales
#b. Utilizando listas por comprensión
#c. Utilizando la función filter
# Aclaracion:
#Tenés que ingresar una frase y un entero N, y devolver otra frase luego de borrar
#las palabras que tengan menos de N caracteres de largo.
#Si se ingresa "lunes martes miércoles" y un 6, hay que devolver "martes miércoles"
#, porque lunes tiene 5 caracteres y 5 es menor que 6.

#Funciones

#a. Utilizando sólo ciclos normales
def filtrar_palabrasA(frase, n):    
    lstPalabras = frase.split()
    lstPalabrasN = []
    for i in range(len(lstPalabras)):
        if len(lstPalabras[i]) >= n:
            lstPalabrasN.append(lstPalabras[i])
    return (lstPalabrasN)

#b. Utilizando listas por comprensión
def filtrar_palabrasB(frase,n):
    lstPalabras = frase.split()
    lstPalabrasN = [x for x in lstPalabras if len(x) >= 6]
    return (lstPalabrasN)    

#c. Utilizando la función filter
def filtrar_palabrasC(frase,n):    
    #Hay que hacer split para que tome a frase como lista de palabras sino
    #la función lambda toma cada caracter del parámetro frase
    lstPalabras = frase.split()
    lstPalabrasN = list(filter(lambda x:len(x)>=6,lstPalabras))
    return (lstPalabrasN)

#Programa Principal
frase='Lunes Martes Miércoles'
print(filtrar_palabrasA(frase,6))
print()
print(filtrar_palabrasB(frase,6))
print()
print(filtrar_palabrasC(frase,6))

