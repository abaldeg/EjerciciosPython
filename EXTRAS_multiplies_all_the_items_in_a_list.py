#Write a Python program to multiplies all the items in a list
def multiplicarItems(lista):
    r=1
    for i in range(len(lista)):
        r=lista[i]*r
    return(r)    

lista=[1,2,-8]
print(multiplicarItems(lista))
#####
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))    