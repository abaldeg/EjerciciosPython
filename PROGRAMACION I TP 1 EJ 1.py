#PROGRAMACION I TP 1 EJ 1
#Bloque Funciones
def ObtenerMayor(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            return n1        
    elif n2 > n3:
            return n2
    elif n3 > n1:
        return n3
    else:
        return -1
        
# Programa Principal    
n1=int(input("Ingrese N1:"))
n2=int(input("Ingrese N2:"))
n3=int(input("Ingrese N3:"))
r=ObtenerMayor(n1,n2,n3)
if r==-1:
    print("No hay mayor")
else:
    print ("El número mayor es: ",r)
