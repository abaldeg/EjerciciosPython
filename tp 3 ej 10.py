l1=float(input("Ingrese lado 1:"))
l2=float(input("Ingrese lado 2:"))
l3=float(input("Ingrese lado 3:"))

if l1 > l2 and l1 > l3:
    a=l1
    b=l2
    c=l3

if l2 > l1 and l2 > l3:
    a=l2
    b=l1
    c=l3

if l3 > l1 and l3 > l2:
    a=l3
    b=l1
    c=l2

if a >= b + c:
    resultado='No es un triangulo.'

print (a**2)
print (b**2 +c**2)

if a**2 == (b**2 +c**2):
    resultado="ES un triangulo rectangulo"
  
if a**2 > (b**2+c**2):
        resultado="ES un triangulo obstusangulo"

if a**2 < (b**2+c**2):
        resultado="ES un triangulo acutangulo"

print ("Resultado: ", resultado)

