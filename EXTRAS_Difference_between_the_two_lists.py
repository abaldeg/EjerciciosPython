#Difference between the two lists
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

listaResultado=[]
for e in list1:
    if e not in list2:
        listaResultado.append(e)
print(listaResultado)
        