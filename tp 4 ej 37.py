cont, leg, cat, sal, totsal, cant20k,cant5kc, mayorsal, legmayorsal, sueldomasbajo,importsueldo_a,importsueldo_b,importsueldo_c =0,0,0,0,0,0,0,0,0,0,0,0,0


while cont <= 4:
    leg=int(input("Ingrese Legajo: "))
    cat=input("Ingrese categoria: ")
    sal=float(input("ingrese salario:"))
    
    if cont==0:
        sueldomasbajo=sal        
    
    if sal > 20000:
        cant20k=cant20k+1
        
    if cat=="C" and sal < 5000:        
        cant5kc=cant5kc+1
    
    if sal > mayorsal:
        mayorsal=sal
        legmayorsal=leg
    
    if sal < sueldomasbajo:
        sueldomasbajo=sal
    
    if cat=="A":
        importsueldo_a=importsueldo_a+sal
    elif cat=="B":
        importsueldo_b=importsueldo_b+sal
    elif cat=="C":
        importsueldo_c=importsueldo_c+sal
    
    totsal=totsal+sal
    cont=cont+1

print("Importe total de salarios:", totsal)
print("")
print("Cantidad de empleados que ganan mas de 20000:", cant20k)
print("")
print("Cantidad de empleados que ganan menos de 5000 y su categoria es C:",cant5kc)
print("")
print("Legajo del empleado que mas gana:",legmayorsal)
print("")
print("Sueldo mas bajo:",sueldomasbajo)
print("")
print("Importe total de sueldos para categoria A:",importsueldo_a)
print("")
print("Importe total de sueldos para categoria B:",importsueldo_b)
print("")
print("Importe total de sueldos para categoria C:",importsueldo_c)
print("")
print("Salario promedio:", totsal/cont)

    
