#Lista sentencias
while cociente >= 10 :
    resto = cociente % 10
    cociente = cociente // 10
    cont = cont + 1
    cantDig = cont + 1
#
lstPalabrasN = [x for x in lstPalabras if len(x) >= 6]
#
frase.split()
#
for i in range(n):
    m.append([0]*n)
#
matriz = [[0]*(n) for i in range(n)]
#
for i in range(n+1):
    matriz[0][i] = i
    matriz[i][0] = i
#
# 1 a n columnas para todas las filas
print("Lista de Ventas: ", [x[1:cantMeses+1] for x in mat])
#
numeros=[]
for f in range(n):
    for c in range(n):
        azar = random.randint(0,cantidad-1)
        while azar in numeros:
            azar = random.randint(0,cantidad-1)
        mat[f][c] = azar
        numeros.append(azar)
#
def crearMatVtas():
    mat=[]
    for i in range(0,14):
        mat.append([0]*14)    
     
    for col in range(1,14):
        mat[0][col]=col   
        
    for fil in range(1,14):
        r=lambda: random.randint(1,12) 
        mat[fil][0]=r()
        
    for f in range(1,13):
        for c in range(1,13):                                   
            mat[f][c]=random.randint(0,2000) 
            
    for f in range(0,13):
        for c in range(0,13):            
            print("%5d" %(mat[f][c]), end="-")      
        print()
    
#
listaaux=matriz[numero1][:]
matriz[numero1][:]=matriz[numero2][:]
matriz[numero2][:]=listaaux
print(matriz[numero1][:])
print(matriz[numero2][:])
#
lstPalabras=frase.split()
#
lstPalabrasN=[x for x in lstPalabras if len(x)>=6]
#
lstPalabrasN=list(filter(lambda x:len(x)>=6,lstPalabras))
#
List.insert(3, 12)
List.insert(0,'Geeks')
#
List=["Geeks","For","Geeks"]
List=[['Geeks','For'],['Geeks']]
#
Sliced_List=List[3:8]
#
Sliced_List=List[5:]
#
Sliced_List=List[:]
Sliced_List=List[:-6]
#
lista=[1,2,3,4]
print(lista[1:1]) #[] Rebanada nula
#
lista=["a","b","c"]
lista[1:1]=["B","C","D"]
print (lista) #['a', 'B', 'C', 'D', 'b', 'c']
#
Sliced_List=List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
#
lista=[1,2,3,4,5,6]
a=0
b=4
sublista=lista[a:b]
print(sublista) # [1, 2, 3, 4]
#
for i in range (random.randint(10,99)):
    listaRandom.append(random.randint(1000,9999))
#
esBisiesto=lambda año: (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
#
l.sort(reverse=True)
#
l[i]=i**2
#
if l1[i] in l2:
    comun=True 
#
# Function to demonstrate printing pattern 
def pypart(n):
    # outer loop to handle number of rows
    # n in this case 
    for i in range(0, n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop 
        for j in range(0, i+1):
            # printing stars
            print("* ",end="")
        # ending line after each row
        print("\r")
        # Driver Code 
n=5
pypart(n) 
#
precio=5.2
print("Precio: %5.2f" %precio)
#
print("X= %4d Y= %4d" %(x,y))
#
print(10//3) #3
#
print(10/3) #3.3333333333333335
#
print(10%3) # 1
#
for i in range(2,11,2):
    print(i, end="") #246810
#
for i in range(2,11,2):  #2  4  6  8 10  
    print("%2d " %i, end="")
#
for i in range(2,11,2):    
    print("%2d " %i)
# 2 
# 4 
# 6 
# 8 
#10

#
print(1,12,2019,sep="/") #1/12/2019
print(1,"/",12,"/",2019,sep="") #1/12/2019
#
cuadrado=lambda x:x**2
print (cuadrado(3)) #9
#
alaN=lambda x,y=2:x**y #y puede no venir, hay default = 2
print (alaN(3,3)) #27
print (alaN(3)) #9
#
lista=[1,2,3,4,5,6,7,8,9,10]
lista.index(1) #0
lista.index(7) #6
lista.index(7,0,3)
#Traceback (most recent call last):
  #File "<pyshell>", line 1, in <module>
#ValueError: 7 is not in list
lista.index(7,0,8) #6
#
def sumaAcumulada(listaOriginal):    
    listaAcumulada.append(listaOriginal[0])
    sumaAcumulada=listaOriginal[0]
    for i in range(1,len(listaOriginal)):        
        listaAcumulada.append(listaOriginal[i]+sumaAcumulada)
        sumaAcumulada=sumaAcumulada+listaOriginal[i]
    return
listaOriginal=[1,2,3]
listaAcumulada=[]
sumaAcumulada(listaOriginal)
for i in range(len(listaAcumulada)):    
    print("%3d" %listaAcumulada[i], end="")
#1  3  6
#
#Funciones
def eliminaPalabras(listaPalabras):    
    for i in range(len(listaPalabras)):
        if listaPalabras[i] not in ListaPalabraEliminar:
            NuevaLista.append(listaPalabras[i])           
#Programas
listaPalabras=["Ave", "Programa", "Azul"]
NuevaLista=[]
print(listaPalabras)
print()
ListaPalabraEliminar=["Programa"]
print(ListaPalabraEliminar)
print()
eliminaPalabras(listaPalabras)
print(NuevaLista)
#['Ave', 'Programa', 'Azul']
#['Programa']
#['Ave', 'Azul']
#
r1 = a%b
r2 = b%a
if a==b:
    print("Ambos son multiplos entre si")
elif r1 == 0:
    print("El numero, A",a,"es multiplo de B",b)
    print("El numero, B",b,"NO es multiplo de A",a)
elif r2 == 0:
    print("El numero B",b,"es multiplo de A",a)
    print("El numero, A",a,"NO es multiplo de B",b)
#
if (a%4 == 0 and a%100!=0) or (a%400==0):
    print("el anio",a,"es biciesto")
#
# En los siguientes ejercicios utilice la función del ejercicio I para ingresar datos en una lista y:
# Determinar Si una lista es capicúa.
# 4554 45454
def CrearLista ():
    l = []
    pos=0
    n=int(input("Ingrese un número (-1 para finalizar)"))    
    while n != -1:        
        while (n < 1 and n != -1) or n > 20:
            n=int(input("Error. Ingrese un número entre 1 y 20 (-1 para finalizar)"))
        if n != -1:
            l.append(n)
            pos=pos+1
            n=int(input("Ingrese un número (-1 para finalizar)"))    
    return l

l=CrearLista()
largo=len(l)
capicua=False
derecha = 0
if largo % 2 !=0:
    for i in range(largo):
        if l[i]==l[(largo-1)-derecha]:
            capicua=True
        else:
            capicua=False
        derecha=derecha+1
else:
    print("La cantidad de elementos de la lista debe ser impar")

if capicua==True:
    print("La lista es capicua")
else:
    print("La lista NO es capicua")
#
#Write a Python program to sum all the items in a list
lista=[1,2,3,4,5,6,]
print("Suma de los item de la lista: ", sum(lista), end="")
#
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
#
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
#
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
#
def contarCadenas(lista):
    cont=0
    for c in lista:
        if len(c) > 1 and c[0]==c[-1]:
            cont=cont+1
    return(cont)

lista=['abc', 'xyz', 'aba', '1221']
print(contarCadenas(lista))
#
#Write a Python program to check a list is empty or not.
#not de un vacio es True
l = []
if not l:
  print("List is empty")
print(l)
#
#Write a Python program to clone or copy a list
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
new_list2 = original_list
print(original_list)
print(new_list)
print(new_list2)
#
#find the list of words that are longer than n from a given list of words
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len 
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
#['quick', 'brown', 'jumps', 'over', 'lazy']
#
#Write a Python function that takes two lists and returns True if they have at least one common member.
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
#
#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)] #enumerate lo vimos asi que se puede usar en parcial.
print(color)
#
#Write a Python program to generate a 3*4*6 3D array whose each element is *
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
array = [[ ['*' for col in range(6)] for col in range(4)] "-" for row in range(3)] #No funca: SyntaxError: invalid syntax
print(array)
#
#Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)

num = [7,8, 120, 25, 44, 20, 27,0]
num = [x for x in num if x==0] #Ejemplo con operador booleano.
print(num)
#
#Write a Python program to shuffle and print a specified list
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color) #la vimos en clase
print(color)
#
#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers
#between 1 and 30 (both included).
def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
printValues()
#
#Difference between the two lists
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

listaResultado=[]
for e in list1:
    if e not in list2:
        listaResultado.append(e)
print(listaResultado)
#




