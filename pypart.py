#Alinear un número a la izquierda: 
c="*{:<8}*".format(4)
print(c)
"""
*4       *
"""
#Alinear una cadena a la derecha: 
c="*{:>8}*".format("Hola") # * Hola*
print(c)

#Alinear una cadena a la centrada: 
c="*{:^8}*".format("Hola") # * Hola*
print(c)