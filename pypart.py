def leerentero(msj="Ingrese un entero: " ):
    """ Función para ingresar un número entero """
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print("Dato inválido.")
            print("lntente nuevamente.")
    return n

leerentero()