"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad
que indique si la operación fue exitosa. Desarrollar también un programa para verificar
su comportamiento.
"""
def eliminarclaves(diccionario,listaAeliminar):  
    correcto=True        
    while True:
        try:
            for i in listaAeliminar:
                valor=diccionario.pop(i)
            break
        except KeyError:
            correcto=False
            break
    return diccionario, correcto

colores={
    "Rojo":[255,0,0],
    "Verde":[0,255,0],
    "Azul":[0,0,255]         
         }
#listaAeliminar=["Azul","Verde"]
#listaAeliminar=["Amarillo","Verde"]
listaAeliminar=["Verde","Amarillo"]
colores,correcto=eliminarclaves(colores,listaAeliminar)
print(colores)
print(listaAeliminar)
print(correcto)
print(colores)