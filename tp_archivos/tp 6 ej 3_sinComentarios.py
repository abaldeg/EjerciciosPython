


def CrearLista ():
    # para tp de archivos. esta linea tiene que quedar eliminada.
    l = []
    pos=0
    n=int(input("Ingrese un número (-1 para finalizar)"))    
    while n != -1:        
        while (n < 1 and n != -1) or n > 20:
            n=int(input("Error. Ingrese un número entre 1 y 20 (-1 para finalizar)"))
        if n != -1:
            l.append(n)
            pos=pos+1
            n=int(input("Ingrese un número (-1 para finalizar)"))    
    return l

l=CrearLista()
largo=len(l)
capicua=False
derecha = 0
if largo % 2 !=0:
    for i in range(largo):
        if l[i]==l[(largo-1)-derecha]:
            capicua=True
        else:
            capicua=False
        derecha=derecha+1
else: 
    print("La cantidad de elementos de la lista debe ser impar")

if capicua==True:
    print("La lista es capicua")
else:
    print("La lista NO es capicua")
    