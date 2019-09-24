'''
#EJ1
legajo = int(input("ingrese el legajo del alumno:"))
#nota= int(input("ingrese la nota del alumno:"))
MuyBien = 0
Bien=0
Mal=0
PorcMal=0
alumnos=0
mayor=0
sumaNotas=1
prom=0



while legajo != -1 :
    nota= int(input("ingrese la nota del alumno:"))
    #cantidad total de alumnos
    alumnos = alumnos + 1
    if nota >0 and nota<11:
        #guardar cantidad de alumnos por nota
        if nota >=7 :
            MuyBien = MuyBien+1
            sumaNotas=sumaNotas+nota
        elif nota >= 4 and nota < 7 :
            Bien = Bien + 1
        elif nota < 4:
            Mal = Mal +1
    else :
        print("esa nota no es valida")
        nota=int(input('ingrese la nota del alumno correcta'))
            
    #guardar el mayor dato
    if nota>mayor:
        mayor=nota
    
    #calcular procentaje de aplazados
    PorcMal = (Mal/alumnos)*100
    #Promedio de las calificaciones hay que poner un if por si MuyBien es 0
    if MuyBien>0:
        prom = sumaNotas/MuyBien
    
    legajo = int(input("ingrese el legajo del alumno:"))
    

print('hay',MuyBien,'alumnos con notas mayores a 7')
print('hay',Bien,'alumnos con notas entre 7 y 4')
print('hay',Mal,'alumnos con aplazos')
print('el procentaje de alumnos aplazados es del',PorcMal,'%')
print('la cantidad totalde alumnos es', alumnos)
print('el promedio total de clasificaciones mayores a 7 es de:',prom)
print('la nota mas alta es:', mayor)
'''

#ej2

n = int(input("ingrese un nro positivo"))
#hay que hacer un while que multiplique nros consecutivos y que corte cuando te psas de n
a=0
b=1

while (a*b) < n :
    a=a+1
    b=b+1
    if (a*b)==n :
        oblongo = True
        #print("el nro es oblongo")
    else :
        oblongo = False
        #print('el nro no es oblongo')

if oblongo == True:
    print('es oblongo')
else :
    print('no es oblongo')


'''
#Ej1
Se ingresa por teclado el numero de legajo de los alumnos de un curso, y su nota de examen final.
El fin de la carga se determina ingresando -1 en el legajo y se debe validar que la nota sea entre 1 y 10
Se pide informar:
                a)cantidad de alumnos con nota >= 7
                b) cantidad de alumnos con nota >= 4 y < 7
                c) cantidad de alumnos con nota <4
                d) porcentaje de alumnos que estan aplazados
                e) cantidad total de alumnos
                f) promediototal de las calificaciones >= 7
                g) la nota mas alta
                
#Ej2
Ingresar un numero positivo. Rechazarel numero y volverlo a ingresar en caso de ser negativo
se solicita imprimir un mensaje si dicho numero es oblongo o no
se dice que un nro es oblongo cuando se obtiene de multiplicar 2 numeros consecutivos
ejemplo 2 es oblongo porque resulta de multiplicar 1*2
        6 es oblongo porque resulta de multiplicar 2*3
        20 es oblongo porque resulta de muliplicar 4*5
        24 no lo es porque ningun producto de 2 nros consecutivos da 24
por ultimo informar si es el nro ingresado un nro primo un nro primo es que unicamente es divisible por la unidad y por si mismo
'''



























