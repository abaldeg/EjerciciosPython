numleg=0
nota=0
cant_notas_mayor_7=0
cant_notas_4_6=0
cant_notas_menor_4=0
porc_aplazados=0
canttotal=0
promedio_mayor_7=0
suma_mayor_7=0
nota_mayor=0


numleg=int(input("Ingrese numero legajo: "))

while numleg !=-1:
    
    nota=int(input("Ingrese nota: "))
    
    if nota >=1 and nota <= 10:    
        if nota>=7:
            cant_notas_mayor_7=cant_notas_mayor_7 + 1
            suma_mayor_7=suma_mayor_7 + nota
            
        if nota > nota_mayor:
            nota_mayor=nota
            
        if nota>=4 and nota<7:
            cant_notas_4_6=cant_notas_4_6 + 1
            
        if nota <4:
            cant_notas_menor_4=cant_notas_menor_4 + 1
            
        canttotal=canttotal+1
            
    else:
        while not (nota >=1 and nota <= 10):
            nota=int(input("Ingrese nota entre 1 y 10: "))
        
    
    numleg=int(input("Ingrese numero legajo: "))
    
    
porc_aplazados=(cant_notas_menor_4*100)/canttotal

print("Cantidad de alumnos con nota mayor o igual a 7:",cant_notas_mayor_7)
print("Cantidad de alumnos con nota entre 4 y 6:",cant_notas_4_6)
print("Cantidad de alumnos con nota menor a 4:",cant_notas_menor_4) 
print("Porcentaje de alumnos aplazados:", porc_aplazados)
print("Cantidad total de alumnos:", canttotal)
if cant_notas_mayor_7 > 0:
    print("Promedio calificaciones mayores a 7:", suma_mayor_7/cant_notas_mayor_7)
print("La nota mas alta es:", nota_mayor)

            