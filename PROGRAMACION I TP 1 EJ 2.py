#PROGRAMACION I TP 1 EJ 2.py
#Desarrollar una función que reciba tres números enteros positivos y verifique si
#corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
#según la fecha sea correcta o no. Realizar también un programa para verificar el
#comportamiento de la función.

#Bloque Funciones
def VerificaFecha (d,m,a):
    meses28Dias=[2]
    meses30Dias=[4,6,9,11]
    meses31Dias=[1,3,5,7,8,10,12]
    
    if mes in meses28Dias:
        if d > 28:
            return False
        else:
            return True
        
    if mes in meses30Dias:
        if d > 30:
            return False
        else:
            return True
    
    if mes in meses31Dias:
        if d > 31:
            return False
        else:
            return True
   
   if mes >= 1 and mes <= 12:
       return True
    else:
        return False
    
    

#Bloque programa Principal