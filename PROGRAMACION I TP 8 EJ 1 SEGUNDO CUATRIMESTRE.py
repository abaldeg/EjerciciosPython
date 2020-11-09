"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
y luego escribir un programa para verificar su comportamiento:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

def verificarfecha(d,m,a):
    """Ingresa día mes y año representando una fecha. Devuelve True/False si la fecha es válida."""
    meses31Dias=(1,3,5,7,8,10,12)
    meses30Dias=(4,6,9,11,12)
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
            
    return valido

def sumarDiasFecha(d,m,a,dias):
    """Dada una fecha representada como día, mes y año, suma "dias" a esa fecha, devolviendo el resultado como una nueva fecha"""
    cont=1
    nd=d
    nm=m
    na=a
    while cont<=dias:
        if not verificarfecha(nd+1,nm,na): #día inválido, siguiente mes.
            if not verificarfecha(1,nm+1,na): #mes inválido, siguiente año.
                na+=1
                nm=1
                nd=1
            else: #Siguiente mes
                nm+=1
                nd=1                
        else:
            nd+=1
        cont=cont+1
    return nd,nm,na

def verificarHorario(h,m,s):
    """Ingresar un horario desde teclado, verificando que sea correcto."""
    horas=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
    minutos=()
    segundos=()
    unidad=0        
    while unidad <=60:        
        minutos=minutos + (unidad,)
        segundos=segundos + (unidad,)
        unidad+=1
    if (h not in horas) or (m not in minutos) or (s not in segundos):
        valido=False
    else:
        valido=True
    return(valido)

def difHorarios(horario1,horario2):
    """d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
       segundo se considerará que el primero corresponde al día anterior. En ningún
       caso la diferencia en horas puede superar las 24 horas.
    """
    if not verificarHorario(h1,m1,s1) or not verificarHorario(h2,m2,s2):
        return(0,0,0)
    
    if sum(horario1)<sum(horario2):
        h1,m1,s1=horario1
        h2,m2,s2=horario2   
        hdif=h2-h1
        mdif=m2-m1
        sdif=s2-s1            
    else:
        """por ahora 0 ideas"""
        print()     
    
    return hdif,mdif,sdif


"""
año=int(input("Ingrese año: "))
mes=int(input("Ingrese mes: "))
dia=int(input("Ingrese dia: "))
"""
año=2020
mes=12
dia=31
print(f"Fecha válida (True/False) {verificarfecha(dia,mes,año)}")
print(f"Suma de día a fecha: {sumarDiasFecha(dia,mes,año,10)}")
print(f"Verificar horario válido (True/False): {verificarHorario(25,61,61)}")
horario1=(20,30,1)
horario2=(21,31,3)
h,m,s=difHorarios(horario1,horario2)
print(f"Diferencia de {h} horas, {m} minutos, {s} segundos.")