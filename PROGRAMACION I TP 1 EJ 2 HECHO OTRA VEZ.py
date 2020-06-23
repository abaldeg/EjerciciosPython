"""Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
según la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función."""

def validarFecha(d,m,a):
    meses31Dias=[1,3,5,7,8,10,12]
    meses30Dias=[4,6,9,11,12]
    #añobisiesto=lambda a: (a % 4==0 and a % 100 !=0) or (a % 400 == 0)
    esBisiesto=lambda a: (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
    valido=False
    
    if m in meses31Dias:
        if d<=31:
            valido=True
    if m in meses30Dias:
        if d<=30:
            valido=True
    if m==2 and esBisiesto(a):
        if d<=29:
            valido=True
    elif m==2 and not esBisiesto(a):
        if d<=28:
            valido=True
    
    return (valido)

print(validarFecha(30,4,2020))
        
            
    