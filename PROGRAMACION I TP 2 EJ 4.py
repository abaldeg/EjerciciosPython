#Definir una función superposición() que reciba como parámetros dos listas de cualquier
#tipo y devuelva True si tienen al menos un elemento en común, o False en
#caso contrario. Desarrollar un programa para verificar su comportamiento.

#Funciones
def superposición(l1,l2):
    comun=False
    for i in range(len(l1)):
        if l1[i] in l2:
            comun=True            
    return(comun)
            

#Programa Principal
l1=[1,2,3,4,5,6]
l2=[6,7,8,9,10]
print(superposición(l1,l2))

