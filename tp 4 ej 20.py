a,b,resto,cociente=0,0,0,0

a=int(input("Ingrese numero positivo:"))
b=int(input("Ingrese numero positivo:"))

while a < b or b < 0:
    a=int(input("Ingrese numero positivo:"))
    b=int(input("Ingrese numero positivo:"))

resto=a
while resto >= b:
    resto=resto-b    
    cociente=cociente+1

print("divisor",a)
print("dividendo",b)
print("Cociente",cociente)
print("Resto",resto)


    