n=int(input("Ingrese un Numero:"))
while n <= 0:
    n=int(input("Ingrese un Numero:"))    
p=0
while p < n:
    p=p+1
    if p%2==0:
        print("El numero",p," es par")
    

