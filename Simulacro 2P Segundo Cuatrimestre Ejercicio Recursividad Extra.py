"""Utilizando una función recursiva determine cuál es la palabra de una lista
que repite más veces el último caracter."""
def mayorRepeticion(listapalabras, palabramayor="",cantmax=0):
    if len(listapalabras)==0:
        return palabramayor
    else:
        cantrepe=0
        palabraactual=listapalabras[0].upper()
        ultimaletra=palabraactual[len(palabraactual)-1]
        for letra in palabraactual:
            if letra==ultimaletra:
                cantrepe+=1        
        if cantrepe>cantmax:
            return mayorRepeticion(listapalabras[1:],palabraactual,cantrepe)
        else:
            return mayorRepeticion(listapalabras[1:],palabramayor,cantmax)

listapalabras=["Verd","Rojo","Azullllllllll"]
print(mayorRepeticion(listapalabras))