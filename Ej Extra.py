#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# ## 1
# nombre=input("ingrese nombre: ")
# edad=int(input("Ingrese edad actual: "))
# anio=(100-edad) + 2019
# print("Cuando tengas 100 años será el año:",anio)

# #Solucion
# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2014 - age)+100)
# print(name + " will be 100 years old in the year " + year)


#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# num=int(input("Ingrese numero:"))
# num=num%2
# if num==0:
#     print("Numero par")
# else:
#     print("Numero impar")

# num = input("Enter a number: ")
# mod = num % 2
# if mod > 0:
#     print("You picked an odd number.")
# else:
#     print("You picked an even number.")


# num = int(input("give me a number to check: "))
# check = int(input("give me a number to divide by: "))

# if num % 4 == 0:
#     print(num, "is a multiple of 4")
# elif num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")

# if num % check == 0:
#     print(num, "divides evenly by", check)
# else:
#     print(num, "does not divide evenly by", check)


#Exercise 3 (and Solution)
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elemento in a:
    if elemento < 5:
        print(elemento)
    


