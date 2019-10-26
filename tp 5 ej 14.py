# Obtener digito central si el numero es impar, sino -1

def fObtenerDigitoCentral(d):
                   
    resultado = -1
    cociente=d
    digito=d    
    resto = 1   
    cont = 0
        
    while cociente >= 10 :
        
        resto = cociente % 10
        cociente = cociente // 10                                            
        cont = cont + 1        
    
    cantDig = cont + 1
    
    cont = 0
    
    if cantDig % 2 != 0 :        
        while cont < ( (cantDig) // 2 )  :
            dig = d % 10
            d = d // 10
            cont = cont + 1
        resultado = d % 10

a=int(input("Ingrese número Entero para analizar: "))

print ("Resultado:",fObtenerDigitoCentral(a))