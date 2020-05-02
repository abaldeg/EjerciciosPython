#Generate groups of five consecutive numbers in a list
l = [[5*i + j for j in range(1,6)] for i in range(15) ] #La exp de afuera son las filas: for i in range(15)]
print(l)
print()

l = [[j for j in range(1)] for i in range(6) ] #La exp de afuera son las filas
print(l) #[[0], [0], [0], [0], [0], [0]]
print()

l = [[j for j in range(2)] for i in range(6) ] #i=filas j=columnas
print(l) #[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
print()

l = [[j for j in range(3)] for i in range(2) ] #i=filas j=columnas
print(l) #[[0, 1, 2], [0, 1, 2]]
print()
