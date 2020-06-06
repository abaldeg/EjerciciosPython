#Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
def calcularProductos(n,m):
    if m==1:
        return(n)
    else:
        return(calcularProductos(n,m-1) + n)

print(calcularProductos(2,8))
    