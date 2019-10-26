
def fUltimosDigitos(d,e):
               
    resultado = -1
    
    div = 1   
    cont = 1
    
    while cont <= e :
        
        div = div * 10
        
        cont = cont + 1      
    
    if (d//div) == 0:
        return -1
    else:
        return d % div

a=int(input("Ingrese número Entero para analizar: "))
b=int(input("Ingrese número Entero a extraer: "))

print ("Resultado:",fUltimosDigitos(a,b))

