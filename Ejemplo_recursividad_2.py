'''
Desarrollar una función para mostrar una cuenta
regresiva desde N por pantalla.
'''

def cuentaRegRec(n):
    # Caso Base 
    if n==0:
        print("0")
    else:
        print(n)
        cuentaRegRec(n-1)
        
cuentaRegRec(10)
