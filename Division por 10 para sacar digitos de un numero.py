cociente=14209
cantDig=0

print("Cociente %5d" %cociente, end="")
print()
while cociente >= 10 :
    resto = cociente % 10
    cociente = cociente // 10    
    cantDig = cantDig + 1
    print("Cosciente %5d" %cociente, end="")
    print()
    print("resto %5d" %resto, end="")
    print()
    print("Cantidad de digitos %5d" %cantDig, end="")
    print()

resto = cociente % 10
cociente = cociente // 10    
cantDig = cantDig + 1
print("Cociente %5d" %cociente, end="")
print()
print("Resto %5d" %resto, end="")
print()
print("Cantidad de digitos %5d" %cantDig, end="")
print()