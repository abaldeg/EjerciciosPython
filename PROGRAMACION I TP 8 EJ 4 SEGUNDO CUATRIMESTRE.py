"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento.
"""
def validarfichas(ficha1,ficha2):
    encajan=False
    if ficha1[0] in ficha2 or ficha1[1] in ficha2:
        encajan=True     
    return encajan
    
ficha1= (3,5)
ficha2= (5,2)
enc=validarfichas(ficha1,ficha2)
print(f"Las fichan encajan: {enc}")