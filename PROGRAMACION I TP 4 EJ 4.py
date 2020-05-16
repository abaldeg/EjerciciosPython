#Escribir una función que reciba como parámetro un número entero entre 0 y 3999
#y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
#¿En qué cambiaría la función si el rango de valores fuese diferente?

#Funciones
def convertirRomano(n):    
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] #lista para mapear los numeros romanos
    sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    if n >= 0 and n <=3999:
        while n: #mientras no sea 0
            div = n // num[i]
            #va dividiendo desde 1000, 900, etc. HASTA QUE EL COCIENTE NO DA 0.
            #Por ej. 3//900=0 PERO 3//1 (num[i=0]) = 3. dando 3,2,1 se repite el while
            #con el mismo numero romano sym[i=0]. Tres I.
            
            n %= num[i]
            # Esto divide el numero num[i] con el numero que vino para ir sacando
            # digitos a medida que los procesa. % Es el resto.
            # Por ej 990: 990%900=90. 90 vuelve a repetir el bucle while n:
            # y sigue procesando.
            
            while div:
                print(sym[i], end = "")
                div -= 1
            i -= 1    

#Programa Principal
convertirRomano(990)