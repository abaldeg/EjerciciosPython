#Frequency of the elements
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

lista_cantidades=[[0]*2 for i in range(len(my_list))] #mal, hay que hacer la lista de totales con los distintos de la lista original.
for f in range(len(lista_cantidades)):
    for c in range(len(lista_cantidades)-1):
        lista_cantidades[f][c]=my_list[f]
        lista_cantidades[f][c+1]=my_list.count(my_list[f])

print(lista_cantidades)
