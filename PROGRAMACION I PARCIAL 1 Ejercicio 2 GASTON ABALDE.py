#Para determinar si un número es divisible por 7

#Funciones
def determinarDiv7(n):   
    l_invertida=[]
    c=n
    while c>=10:        
        c=n//10
        d=n%10
        n=c        
        lista.append(d)
        if c<10:
            lista.append(n%10)            
    l_invertida=lista[::-1]
    for i in range(len(lista)):
        ru=2*lista[i]
        if i==0:
            lista.pop()
        print(lista)
        

#Programa Principal
lista=[]
determinarDiv7(8143)