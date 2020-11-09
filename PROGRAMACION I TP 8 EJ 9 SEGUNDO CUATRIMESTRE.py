"""
Escribir una función que reciba un número entero N y devuelva un diccionario con
la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar
la función.
"""
def convierteAtabla(n):
    """Recibe un número entero y devuelve su tabla de múltiplos"""
    dic = {x:n*x for x in range(1,13)}    
    
    return dic

print(convierteAtabla(2))