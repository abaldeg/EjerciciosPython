cantconsumidores,cantambos,canta,cantb,cantninguno,cantsoloa,cantsolob = 0,0,0,0,0,0,0

while cantconsumidores <= 2:
    proda=int(input("Acepta producto A: "))
    prodb=int(input("Acepta producto B: "))
    
    if proda == 1:
        canta=canta+1
    
    if prodb == 1:
        cantb=cantb+1
        
    if proda == 1 and prodb == 0:
        cantsoloa=cantsoloa+1
    
    if proda == 0 and prodb == 1:
        cantsolob=cantsolob+1
        
    if proda == 0 and prodb == 0:
        cantninguno=cantninguno+1        
    
    if proda == 1 and prodb == 1:
        cantambos=cantambos+1
    
    cantconsumidores=cantconsumidores+1
   
print("Porcentaje de consumidores que aceptan el producto A", canta)
print("Porcentaje de consumidores que aceptan el producto B", cantb)
print("")
print("Porcentaje de consumidores que aceptan SOLAMENTE el producto A", cantsoloa)
print("Porcentaje de consumidores que aceptan SOLAMENTE el producto B", cantsolob)
print("")
print("Porcentaje de consumidores no que aceptan NINGUNO de los dos", cantninguno)
print("")
print("Porcentaje de consumidores que aceptan ambos", cantambos)
