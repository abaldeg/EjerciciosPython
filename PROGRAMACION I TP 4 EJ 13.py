#13. Escribir un programa que cuente cuántas veces se encuentra una subcadena den- 
#tro de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que 
#los caracteres de la subcadena no necesariamente deben estar en forma consecu- 
#tiva dentro de la cadena, pero sí respetando el orden de los mismos.

#Funciones
def contarCadena(cadena,subcadena):
    cantidad=0   
    if len(cadena) > 0 and len(subcadena) > 0:
        cadena=cadena.upper()
        subcadena=subcadena.upper()
        sc=0
        cantidad=0
        c=0
        while len(cadena) > 0:        
            if cadena.find(subcadena[sc]) != -1: # Encontro caracter de subcadena
                c=cadena.find(subcadena[sc]) #saltea hasta el nuevo caracter encontrado
                c+=1                
                if sc==len(subcadena)-1:
                    todoEncontrado=True
                    cantidad += 1
                    sc=0
                else:
                    sc+=1
            else:
                encontrado=False
                sc=0
                c+=1
            cadena=cadena[c:]    
    return(cantidad)       
        
#Programa Principal
cadena="El Principio DEl fin. E l"
print(contarCadena(cadena,"el"))
