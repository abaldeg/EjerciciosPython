#Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)


num = [7,8, 120, 25, 44, 20, 27,0]
num = [x for x in num if x==0] #Ejemplo con operador booleano.
print(num)
