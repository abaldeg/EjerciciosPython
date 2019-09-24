"""Ejercicio 1
Se ingresa por teclado el nro de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1, en la variable del legajo.
Se debe validar que la nota ingresada sea entre 1 y 10.
Se pide informar:
a)  Cantidad de alumnos con nota >= 7
b)  Cantidad de alumnos con nota >= 4 y <7
c)  Cantidad de alumnos con nota menor a 4
d)  Porcentaje de alumnos que están aplazados.
e)  Cantidad total de alumnos.
f)  Promedio de las calificaciones >= a 7.
g)  La nota mas alta."""

legajo=int(input("Ingrese un legajo"))
mayor,nota4,notaint,nota7,alumno,suma=0,0,0,0,0,0
while legajo != -1:
         nota=float(input("Ingrese una nota"))
         while nota<1 or nota >10:
             print ("Ingrese otra nota entre 1 y 10:")
         if nota<4:
             nota4=nota4+1
         elif nota>=4 and nota<7:
             notaint=notaint+1
         else:
             nota7=nota7+1
             suma=suma+nota
         if nota > mayor:
             mayor=nota
         alumno=alumno +1
         legajo=int(input("Ingrese un legajo"))
if alumno != 0:
    print ("Cantidad de alumnos con nota >= 7 ",nota7)
    print ("Cantidad de alumnos con nota <4 ",nota4)         
    print ("Cantidad de alumnos con nota >= 4 y <7 ",notaint)
    print ("Cantidad de alumnos",alumno)
    print ("Nota mas alta",mayor)
    print ("Porcentajes de alumnos aplazados ",nota4 *100/alumno)
    if nota7!=0:
        print ("Promedio de calificaciones >= 7", suma/nota7)
    else:
        print ("No se ingresaron notas mayores o iguales que 7")
else:
    print ("No se ingresaron notas")