a=int(input("Ingrese numero a:"))
b=int(input("Ingrese numero b:"))

while a <= 0 or b <= 0:
    a=int(input("Ingrese numero a:"))
    b=int(input("Ingrese numero b:"))

cont=1
resultado=1

while cont <= b:
    resultado=resultado*a
    cont=cont+1

print("La potencia",b,"del numero:",a,"es:",resultado)


    

