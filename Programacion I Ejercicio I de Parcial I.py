#
n=5
lista=list(range(1,n*n+1))
print(lista)
#lista2 = [[j for j in lista[:n]] for i in lista[0:n] ]
#print(lista2)

arregloDiag=[]
for i in range(n+1):
    arregloDiag.append([0]*(n+1))

numero=1
for c in range(0,n+1):
    if c%2==0:        
        for f in range(0,n):
            arregloDiag[f][c]=numero
            numero=numero+1
        numero=(numero+n)-1
    else:        
        for f in range(0,n):
            arregloDiag[f][c]=numero
            numero=numero-1
        numero=(numero+n)+1
for f in range(0,n):
    for c in range(0,n):
        print("%3d" %arregloDiag[f][c],end="")
    print()   
    

    
    