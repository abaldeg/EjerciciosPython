# Programacion I Parcial 2. Ejercicio 1.


def determinarminimo(m, i=0, min=None):
    if min is None:
        min=m[0]
    if i == len(m) - 1:
        return min    
    else:
        if min > m[i]:
            min=m[i]            
        return determinarminimo(m, i, min)

def determinarmaximo(m, i=0, max=None):
    if max is None:
        max=m[0]
    if i == len(m) - 1:
        return max    
    else:
        if max < m[i]:
            max=m[i]            
        return determinarmaximo(m, i, max)

#Programa Principal.
try:
    produccionfinal=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\ProduccionFinal.txt","rt")
    cantlineas=0
    dia=0   
    
    ProdMenorCant=[]
    cantProdMenorCant=[]
    
    productos=[]
    
    dia=0
    dias=[]
    
    dineroLavarropas=0
    
    for linea in produccionfinal:
        linea=linea.rstrip("\n")
        linea=linea.split(";")
        
        #Dia y cant max
        producto=linea[1]        
        productos.append(producto)
        
        dia=linea[0]
        dias.append(dia)       
            
        if linea[1]=="Lavarropas":
            dineroLavarropas+=int(linea[2])                             
        cantlineas+=1
    
    print("Producto de mínima producción: " + str(determinarminimo(productos)))        
    print("Dia de máxima producción: " + str(determinarmaximo(dia)))                            
    
    print("Cantidad dinero invertida en lavarropas: " + str(dineroLavarropas))
         
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Proceso Finalizado. Lineas procesadas: ", cantlineas)
finally:
    try:
        produccionfinal.close()
    except NameError:
        pass
    

        
