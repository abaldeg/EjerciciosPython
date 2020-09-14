"""Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según la
fecha sea correcta o no. Realizar también un programa para verificar el comportamiento
de la función."""

def verificarFecha(d,m,a):
    valida=False
    meses31Dias=[1,3,5,7,8,10,12]
    meses30Dias=[4,6,9,11,12]
    esBisiesto=lambda a: (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
    if m in meses31Dias:
        if d<=31 and d>0:
            valida=True
    elif m in meses30Dias:
        if d<=30 and d>0:
            valida=True
    elif (d==29 and m==2 and esBisiesto(a)) or (d<=28 and d>0 and m==2):
        valida=True
    return(valida)
        
print(verificarFecha(29,2,2020))
print(verificarFecha(29,2,2021))
print(verificarFecha(28,2,2021)) 
        
    