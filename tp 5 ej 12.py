
def fExtraerDigito(d,e):
               
    resultado = -1
    
    while d > 0 :
      
      da = d % 10
      
      if da == e:
          
          resultado = da       
                
      d = d // 10      
    
    return resultado

a=int(input("Ingrese número Entero para analizar: "))
b=int(input("Ingrese número Entero a extraer: "))

print ("Resultado:",fExtraerDigito(a,b))
