#Los números de claves de dos cajas fuertes están intercalados dentro de un número
#entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
#para obtener ambas claves, donde la primera se construye con los dígitos
#impares de la clave maestra y la segunda con los dígitos pares. Los dígitos se
#numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería
#123 y la clave 2 sería 89.

clave="18293"
clave1=""
clave2=""
for i in range(len(clave)):
    if i%2==0:
        clave1+=clave[i]
    else:
        clave2+=clave[i]
print (clave1)
print()
print (clave2)