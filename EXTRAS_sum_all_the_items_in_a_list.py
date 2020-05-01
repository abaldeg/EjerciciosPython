#Write a Python program to sum all the items in a list
lista=[1,2,3,4,5,6,]
print("Suma de los item de la lista: ", sum(lista), end="")

###
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
