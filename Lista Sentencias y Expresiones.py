#Lista sentencias
#ctrl+f3 busca en Thonny

# Crear matriz
m=[]
for i in range(n):
    m.append([0]*n)

#Imprimir una matriz
for f in range(tam):
    for c in range(tam):
        print("%3d" %mat[f][c], end ="")
    print()

#Range negativo
print(list(range(5,-1,-1)))
#[5, 4, 3, 2, 1, 0]

#Sacar digitos numero entero
cociente=14209
cantDig=0

print("Cociente %5d" %cociente, end="")
print()
while cociente >= 10 :
    resto = cociente % 10 # del resto se sacan los digitos
    cociente = cociente // 10 # me voy quedando con el numero sin los digitos que voy sacando  
    cantDig = cantDig + 1
    print("Cosciente %5d" %cociente, end="")
    print()
    print("resto %5d" %resto, end="")
    print()
    print("Cantidad de digitos %5d" %cantDig, end="")
    print()

resto = cociente % 10
cociente = cociente // 10    
cantDig = cantDig + 1
print("Cociente %5d" %cociente, end="")
print()
print("Resto %5d" %resto, end="")
print()
print("Cantidad de digitos %5d" %cantDig, end="")
print()

#Palabras que cumplan condicion con listas por compresion
lstPalabrasN = [x for x in lstPalabras if len(x) >= 6]

#Convertir un string en lista de palabras
frase.split()

#Inicializacion de Matriz con for
for i in range(n):
    m.append([0]*n)

#Inicializacion de Matriz con listas por compresion
matriz = [[0]*(n) for i in range(n)]

#Inicializacion de Matriz con 0..n tanto en filas como en columnas
for i in range(n+1):
    matriz[0][i] = i
    matriz[i][0] = i
#
# Imprimir matrices
# 1 a n columnas para todas las filas
print("Lista de Ventas: ", [x[1:cantMeses+1] for x in mat])
#Generacion de numeros aleatorios no repetidos.
numeros=[]
for f in range(n):
    for c in range(n):
        azar = random.randint(0,cantidad-1)
        while azar in numeros:
            azar = random.randint(0,cantidad-1)
        mat[f][c] = azar
        numeros.append(azar)
        
# Creacion de matriz de ventas con la fila cero para los doce meses y columna cero para productos aleatorios del 1 al 12.
def crearMatVtas():
    mat=[]
    for i in range(0,14):
        mat.append([0]*14)    
     
    for col in range(1,14):
        mat[0][col]=col   
        
    for fil in range(1,14):
        r=lambda: random.randint(1,12) #Generacion aleatoria de las filas con id de productos.
        mat[fil][0]=r()
        
    for f in range(1,13):
        for c in range(1,13):                                   
            mat[f][c]=random.randint(0,2000) #Generacion de la ventas de los productos en cada mes
            
    for f in range(0,13):
        for c in range(0,13):            
            print("%5d" %(mat[f][c]), end="-")  #Impresion de la matriz    
        print()
    
# Intercambio de filas.
listaaux=matriz[numero1][:]
matriz[numero1][:]=matriz[numero2][:]
matriz[numero2][:]=listaaux
print(matriz[numero1][:])
print(matriz[numero2][:])

# Pasa una frase a lista de palabras
lstPalabras=frase.split()

#Lista por compresion con palabras mayores a seis letras.
lstPalabrasN=[x for x in lstPalabras if len(x)>=6]

# Mismo con funcion lambda y filter
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

# Generacion aleatoria de tamaño de lista y valores.
for i in range (random.randint(10,99)):
    listaRandom.append(random.randint(1000,9999))
    
# Calculo de año biciesto con lambda (True/False)
esBisiesto=lambda año: (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
#
l.sort(reverse=True)
#
l[i]=i**2
#Chequeo de que un elemento de la lista l1 esté en l2
if l1[i] in l2:
    comun=True 
#
# Function to demonstrate printing pattern 
def pypart(n):
    # outer loop to handle number of rows
    # n in this case 
    for i in range(0,n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop 
        for j in range(0, i+1):
            # printing stars
            print("* ",end="")
            # ending line after each row
            #print("\r")
            # Driver Code
n=5
pypart(n)
#* * * * * * * * * * * * * * * con   #print("\r")
#
"""Métodos para cadenas 
Ejemplos del método replace( ) """
a = "Hoy es un día frío, que frío está!" 
b = a.replace("frío", "húmedo") 
print(b) # Hoy es un día húmedo, qué húmedo está! 
c = a.replace("frío", "húmedo", 1) 
print(c) # Hoy es un día húmedo, qué frío está! 
#
# uso de % en print
precio=5.2
print("Precio: %5.2f" %precio)
#
print("X= %4d Y= %4d" %(x,y))
#Cociente, parte entera
print(10//3) #3
# Cociente decimal (posta)
print(10/3) #3.3333333333333335
#Resto de la division
print(10%3) # 1

#Resto de la division, voy descartando dígitos dividiendo por 10
print(105//10) # 1
#10

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
# potencia exponente lambda
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
    print("el año",a,"es biciesto")
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
#Write a Python program to clone or copy a list copiar una lista
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
new_list2 = original_list
print(original_list)
print(new_list)
print(new_list2)
#
#find the list of words that are longer than n from a given list of words. palabras de uns lista mayor que N
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
# Dadas dos lista si al menos tiene un elemento en comun devuelve verdadero.
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
"""Si además del elemento se requiere su subíndice, puede usarse la función enumerate( ). """
lista = ['a', 'e', 'i', 'o', 'u'] 
for i, letra in enumerate(lista):
    print(i, letra) # O a, 1 e, 2 i... 

lista = ['a', 'e', 'i', 'o', 'u'] 
for i, letra in enumerate(lista):
    print(i, letra, end=". ") # 0 a. 1 e. 2 i. 3 o. 4 u. 
#
#Write a Python program to generate a 3*4*6 3D array whose each element is *
#Generación de arreglo de n dimensiones con listas por compresión.
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
# Si lo corremos varias veces altera el orden de la lista de elementos
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color) #la vimos en clase
print(color)
"""
['Black', 'Pink', 'White', 'Red', 'Green', 'Yellow']
>>> %Run pypart.py
['Yellow', 'White', 'Pink', 'Black', 'Red', 'Green']
>>> %Run pypart.py
['Pink', 'Yellow', 'Green', 'Black', 'White', 'Red']
"""
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
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

# imprimir pares de elementos con listas por comprensión
my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

new_list2 = ['{}{}--------{}'.format(x, y,z) for z in range(1,10) for y in range(1, n+1) for x in my_list]
print(new_list2) #['p1--------1', 'q1--------1',...

# Sacar id de una variable
x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) #x es un codigo del format
#
#Convert a list of multiple integers into a single integer
#Convert a list of multiple integers into a single integer
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L))) #map aplica una funcion a cada elemento de una lista. aplica str a L
print("Single Integer: ",x)
print ("++".join(map(str, L))) # "++" porque ya no se pasa a int
#>>> help("str.join")
#Help on method_descriptor in str:
#str.join = join(self, iterable, /)
#    Concatenate any number of strings.
    
#    The string whose method is called is inserted in between each given string.
#    The result is returned as a new string.
#    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
#Split a list into different variables
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)
#
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
#
#Print a nested lists using the print() function
colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

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

#Write a Python program to find the list in a list of lists whose sum of elements is the highest.
num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num, key=sum))
#
# Count the occurrences of the number 4
print([1, 2, 9, 4, 5, 4, 1].count(4))

# Count the occurrences of the letter "a"
list = ["d", "a", "t", "a", "c", "a", "m", "p"]
list.count("a")

#
# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(5)]   
print(matrix) 
#

# 2-D List Como aplanar o hacer una lista de una lista de listas
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
  
flatten_matrix = [] 
  
for sublist in matrix: 
    for val in sublist: 
        flatten_matrix.append(val) 
          
print(flatten_matrix) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 2-D List. Como aplanar o hacer una lista de una lista de listas con listas por comprensión.
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]   
# Nested List Comprehension to flatten a given 2-D matrix
# aplanar una matriz
flatten_matrix = [val for sublist in matrix for val in sublist] 
print(flatten_matrix)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
# Nested List comprehension with an if condition 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
          
print(flatten_planets) #['Venus', 'Earth', 'Mars', 'Pluto']
#
# Python3 Program to Check is a nested 
# list is a subset of another nested list 

def checkSubset(list1, list2): 
    l1, l2 = list1[0], list2[0] 
    exist = True
    for i in list2: 
        if i not in list1: 
            exist = False
    return exist 
    
# Driver Code 
list1 = [[2, 3, 1], [4, 5], [6, 8]] 
list2 = [[4, 5], [6, 8]] 
print(checkSubset(list1, list2)) 
#
# python code to demonstrate 
# splitting nested list 
# into 2 lists 

# initialising nested lists 
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]] 

# printing initial lists 
print ("initial list", str(ini_list)) 

# code to split it into 2 lists 
res1 = [i[1] for i in ini_list] 
res2 = [i[0] for i in ini_list] 

# printing result 
print("final lists", str(res1), "\n", str(res2)) 
#initial list [[1, 2], [4, 3], [45, 65], [223, 2]]
#final lists [2, 3, 65, 2] 
#[1, 4, 45, 223]
#
# Python3 program to Count number 
# of lists in a list of lists 

def countList(lst): 
    return len(lst) 
    
# Driver code 
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
print(countList(lst)) #3
#https://www.geeksforgeeks.org/python-program-to-count-number-of-lists-in-a-list-of-lists/?ref=rp
#
#Ejercicio resuelto profesor PARCIAL 1. EJERCICIO 1. ZIG ZAG POR COLUMNAS
def rellenarporcolumnas(mat):
    n = len(mat)
    contador = 1
    for c in range(n):
        # Determinamos si la columna es par o impar para definir si se
        # rellena de arriba a abajo o de abajo a arriba
        if c%2==0:
            inicio = 0
            fin = n
            incremento = 1
        else:
            inicio = n-1
            fin = -1
            incremento = -1
        for f in range(inicio, fin, incremento):
            mat[f][c] = contador
            contador = contador + 1

def imprimirmatriz(mat):
    for f in mat:
        for c in f:
            print("%3d" %c, end="")
        print()

# Manejo de Excepciones
n = int(input("Tamaño de la matriz? "))
print()
matriz = [[0] * n for i in range(n)]
rellenarporcolumnas(matriz)
imprimirmatriz(matriz)
#
lista=[]
n=0
while n!=-1:
    try:
        n=int(input("Ingrese Numero Entero: -1 sale: "))
        lista.append(n)        
    except ValueError:
        print("Debe ser un numero entero")
        print()    
n=0
contError=1
while n!=-1:
    try:
        n=int(input("Ingrese el numero a buscar en la lista: -1 sale: "))                
        assert contError<3, "Se alcanzó el máximo número de errores"
        lista.index(n)        
        print("Numero %3d , encontrado!" %n)
    except ValueError:
        print("Numero %3d, no encontrado!" %n)
        print()
        contError+=1
    except AssertionError as mensaje:
        print(mensaje)
        break
#
#Funciones
def deterinarCapicua(cadena):
    mitad=len(cadena)//2
    if cadena[:mitad]==cadena[:(mitad)*(-1)-1:-1]: #El inicio es -1 y es el primer parametro, el valor final es la mitad y es el segundo parametro
        return True
    else:
        return False  
#Programa Principal
cadena="123321"
print(deterinarCapicua(cadena))
cadena="123123"
print(deterinarCapicua(cadena))
#
#Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
#misma tiene 80 columnas

#Programa Principal
cadena="Hola"
print(cadena.center(20,"-")) #No hace falta restarle el len de hola


matrix = open(r'C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\numeros.txt').read()
matrix = [item for item in matrix[:-1]]
print(matrix)

#Matrix a archivo
#matrix = [item for item in matrix[:-1]]
#['1', ' ', '2', ' ', '3', '\n', '4', ' ', '5', ' ', '6', '\n', '7', ' ', '8', ' ', '9']

#matrix = [item for item in matrix.split('\n')[:-1]]
#['1 2 3', '4 5 6', '7 8 9']

#matrix = [item.split() for item in matrix.split('\n')[:-1]]
#[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

#matrix = [item.split() for item in matrix.split('\n')[:]]
#[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], []]

#segundo parcial
try:
    a = int(input("Dividendo ?"))
    b = int(input("Divisor ?" ))
    cociente = a // b
    resto = a % b
    print( )
    print("Cociente:", cociente)
    print("Resto: ", resto)
except ZeroDivisionError:
    print("No se puede dividir por cero.")

"""
>>> %Run pypart.py
Dividendo ?10
Divisor ?5

Cociente: 2
Resto:  0

>>> %Run pypart.py
Dividendo ?10
Divisor ?0
No se puede dividir por cero.
"""

#
try:
    a = int(input("Dividendo? "))
    b = int(input("Divisor? "))
    cociente = a // b
    resto = a % b
    print()
    print("Cociente:", cociente)
    print("Resto: ", resto)
except ZeroDivisionError:
    print("No se puede dividir por cero") 
except ValueError:
    print("Sólo se permiten números enteros")
except:
    print("Error desconocido. Intente más tarde.")

#
def leerentero(msj="Ingrese un entero: " ):
    """ Función para ingresar un número entero """
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print("Dato inválido.")
            print("lntente nuevamente.")
    return n

leerentero()
"""
Ingrese un entero: 2.20
Dato inválido.
lntente nuevamente.
Ingrese un entero: a
Dato inválido.
lntente nuevamente.
Ingrese un entero: 2
"""
#
def leerentero(msj="lngrese un entero: "):
    while True:
        try:
            n = int(input(msj))
            break
        except ValueError:
            print("Dato inválido.")
            a = input("Desea ingresarlo otra vez? (S/N) ")
            if a.upper() =='N':
                raise
    return n
leerentero()
"""
lngrese un entero: s
Dato inválido.
Desea ingresarlo otra vez? (S/N) n
Traceback (most recent call last):
  File "C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\pypart.py", line 12, in <module>
    leerentero()
  File "C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\pypart.py", line 4, in leerentero
    n = int(input(msj))
ValueError: invalid literal for int() with base 10: 's'
"""
#

"""
Dividendo? 10
Divisor? 2.90
Sólo se permiten números enteros
"""

"""Escribir una función que sume todos los elementos de una matriz de M x N y de-
vuelva el resultado."""
def summation_recursive(m, i=0, j=0, s=0):
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return s
    elif j == len(m[i]) - 1:
        return summation_recursive(m, i + 1, 0, s)
    else:
        return summation_recursive(m, i, j + 1, s + m[i][j])

"""Leer el archivo generado en el ejemplo anterior e imprimir por pantalla los datos 
de aquellos alumnos cuyo número de legajo sea menor a 1.000.000. """
try:
    arch = open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\alumnos.txt","rt")
    for linea in arch:
        lu, nombre = linea.split(';')
        nombre = nombre.rstrip('\n')
        if print(f"LU: {lu:>7} - Nombre: {nombre}"):
            print("Archivo leido correctamente.")
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:", mensaje)
except OSError as mensaje:
    print("No se puede leer el archivo:", mensaje) 
finally:
    try:
        arch.close( )
    except NameError:
        pass
""" print(f"LU: {lu:>1}    
LU: 12 - Nombre: Juan
LU: 1234567 - Nombre: Juana
LU: 1234567 - Nombre: Juanito
LU: 1234567 - Nombre: JuanPablo
LU: 1234567 - Nombre: JuanAndrÃ©s
"""
""" print(f"LU: {lu:>7}
LU:      12 - Nombre: Juan
LU: 1234567 - Nombre: Juana
LU: 1234567 - Nombre: Juanito
LU: 1234567 - Nombre: JuanPablo
LU: 1234567 - Nombre: JuanAndrÃ©s
"""
#
def leerentero(msj="Ingrese un entero: "):
    while True:
        try:
            n = int(input(msj))
        except ValueError:
            print("Dato inválido.")
            print("lntente nuevamente.")
        else:
            break
    return n
leerentero()
"""
Ingrese un entero: a
Dato inválido.
lntente nuevamente.
Ingrese un entero: a
Dato inválido.
lntente nuevamente.
Ingrese un entero: 1
"""
#
"""Leer un archivo de texto y mostrar la 
palabra más larga que contenga. 
Si hay más de una se mostrará cualquiera 
de ellas. """
try:
    arch = open("notas.txt","rt")
    maslarga = ""
    for linea in arch:
        linea = linea.rstrip("\n")
        listadepalabras = linea.split( )
        for palabra in listadepalabras:
            if len(palabra) > len(maslarga):
                maslarga = palabra
    print("La palabra más larga es:", maslarga)
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:", mensaje) 
except OSError as mensaje:
    print("No se puede leer el archivo:", mensaje) 
finally:
    try:
        arch.close()
    except NameError:
        pass

"""Ejemplo 5 
Convertir a mayúsculas el contenido del 
archivo "notas.txt". 
Como los archivos de texto no se pueden 
alterar, crearemos una versión 
modificada llamada "notas2.txt" """
try:
    entrada = open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\notas.txt","rt")
    salida = open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\notas2.txt","wt")
    cantlineas=0
    for linea in entrada:
        salida.write(linea.upper( ))
        cantlineas+=1
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:" , mensaje) 
except OSError as mensaje:
    print("ERROR: ", mensaje)
else:
    print("Copia finalizada. Líneas copiadas:" , cantlineas) 
finally:
    try:
        entrada.close( )
        salida.close( )
    except NameError:
        pass
    
"""Recomendaciones 
No debe leerse ni grabarse por campos; toda lectura o grabación debe afectar al registro completo. 
Esto se debe a razones de eficiencia.
Es necesario minimizar* la cantidad de 
veces que se recorren los archivos. """
"""Una excepción de tipo SyntaxError (unicode error) se debe a que la ruta del archivo contiene secuencias de 
escape que no fueron tratadas.
SyntaxError: (unicode error) 'unicodeescape' codec can 't decode bytes in position 2-3: truncated \UXXXXXXXX escape """

"""Si se produce una excepción de tipo UnicodeDecodeError o si los caracteres 
regionales aparecen dañados, el archivo f'" creado con codificación UTF8. 
En estos casos es necesario agregar un parámetro más en la apertura del mismo: 
arch = open("datos.txt", "rt", """

"""Los archivos de texto generados con odificación UTF8 contienen bytes 
adicionales al inicio, lo que se conoce como cabecera. 
Por ese motivo el parámetro  encoding="UTF8" sólo se agregará a la 
función open() cuando sea estrictamente necesario. """

"""
Reemplazar las vocales con tilde en 
una cadena de caracteres por sus 
equivalentes sin tilde. 
"""
vocalescontilde = "áéíóúÀÉiÓÚ" 
vocalessintilde = "aeiouAElOU" 
frase = input("lngrese una frase: ") 
nueva = '"' 
for caracter in frase: 
if caracter in vocalescontilde: 
posicion = vocalescontilde.index(caracter) 
nueva = nueva + vocalessintilde[posicion]
else: 
nueva = nueva + caracter 
print(nueva)

#
def imprimirmatriz(mat):
    filas = len(mat)
    columnas= len(mat[0])
    elementos = filas * columnas
    f=0
    c=0
    for i in range(elementos):
        try:
            print("%3d" %mat[f][c], end="")
        except IndexError:
            f=f+1
            print()
            print("%3d" %mat[f][c], end="")
        finally:
            c=c+1
mat=[[1,2,3],[4,5,6]]
imprimirmatriz(mat)
"""
Traceback (most recent call last):
  File "C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\pypart.py", line 18, in <module>
    imprimirmatriz(mat)
  File "C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\pypart.py", line 13, in imprimirmatriz
    print("%3d" %mat[f][c], end="")
IndexError: list index out of range
"""
#
while True:
    try:
        mes = int(input("lngrese el mes: "))
        assert 1<= mes <=12
        break
    except ValueError:
        print("Sólo se permiten números.")
    except AssertionError:
        print("El mes debe estar entre 1 y 12.")
    print("intente nuevamente.")
print("mes ingresado es", mes)
"""
>>> %Run pypart.py
lngrese el mes: 1
mes ingresado es 1
>>> %Run pypart.py
lngrese el mes: 23
El mes debe estar entre 1 y 12.
intente nuevamente.
lngrese el mes: 1
mes ingresado es 1
"""
#
while True:
    try:
        n = float(input("lngrese el numero decimal: "))        
        break
    except ValueError:
        print("Sólo se permiten decimales.")    
    print("intente nuevamente.")
print("decimal ingresado es", n)
""">>> %Run pypart.py
lngrese el numero decimal: 1.10
decimal ingresado es 1.1
>>> %Run pypart.py
lngrese el numero decimal: 1
decimal ingresado es 1.0
>>> %Run pypart.py
lngrese el numero decimal: a
Sólo se permiten decimales.
intente nuevamente.
lngrese el numero decimal: 1
decimal ingresado es 1.0
>>> 
"""
# Para detectar un número decimal
n=0.2
if n==int(n):
    print('entero')
else:
    print("real")
#
#
"""Métodos para cadenas 
<str>.split([<sep>]): Divide <str> en 
una lista de cadenas, buscando 
<sep> como separador. Si <sep> se 
omite se asumen los espacios.
"""
a = "Hola Mundo" 
b = a.split() # ['Hola', 'Mundo'] 
c, d = a.split() # 'Hola' y 'Mundo' 

"""
<sep>.join(<secuencia>): Devuelve 
una cadena con los elementos de 
<secuencia> separados por <sep>. 
<secuencia> puede ser una caden 
o una lista de cadenas. 
"""
cad = ', '.join('abc') 
print(cad) # a, b, c


"""
Ejemplos del método replace() 
"""
a = "Hoy es un día frío, que frío está!" 
b = a.replace("frío", "húmedo") 
print(b) # Hoy es un día húmedo, qué húmedo está! 
c = a.replace("frío", "húmedo", 1) 
print(c) # Hoyes un día húmedo, qué frío está! 

# Centrado con cualquier caracter
cad1 = 'Hola' 
cad2 = cad1.center(10,'-') 
print(cad2) # ---Hola--- 
# alineados a la derecha o izquiera con cualquier caracter
cad1 = 'Hola' 
cad2 = cad1.ljust(10,'-') 
print(cad2) # Hola--- 
#
#
a = "Continuará..."
b = a.rstrip('.') # 'Continuará'
print (b)
"""
Continuará
"""
#
# alineado con ceros
n=3
cad = str(n).zfill(5) 
print(cad) # 00003
"""
00003
"""
#
"""
<str>.isalpha(): Devuelve True si 
todos los caracteres de <str> son 
alfabéticos (letras), o False en caso 
contrario. Reconoce caracteres 
regionales."""
cad = 'Hola' 
print(cad.isalpha()) # True 

"""
<str>.isdigit( ): Devuelve True si todos 
los caracteres de <str> son dígitos 
numéricos. 
"""
cadl = '1234' 
cad2 = '3.1416' 
print(cad1.isdigit(), cad2.isdigit()) 
#True False

#Desarrollar una función que reciba un número binario y lo devuelva convertido a
#base decimal.
def convertirBaD(cadena):
    if not cadena:
        return 0
    return convertirBaD(cadena[:-1]) * 2 + (cadena[-1] == '1')
#convertirBaD(cadena[:-1]) va contando el digito donde esta parado.
print(convertirBaD("110"))

#Escribir una función que devuelva la suma de los N primeros números naturales.
def sumarNaturales(n,suma=0):
    if n==1:
        suma+=n
        return(suma)
    else:
        suma+=n
        n-=1
        return(sumarNaturales(n,suma))
print(sumarNaturales(3))

#Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
#utilizar cadenas de caracteres.
def contarCantDigitos(n,cantdigitos=None):
    if cantdigitos is None:
        cantdigitos=1
    n=n//10
    if  n>0:
        cantdigitos+=1
        return (contarCantDigitos(n,cantdigitos))
    else:
        return(cantdigitos) 
print(contarCantDigitos(12))

#Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
def calcularProductos(n,m):
    if m==1:
        return(n)
    else:
        return(calcularProductos(n,m-1) + n)
print(calcularProductos(2,8))
    
#
try:
    longfija=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\longfija.txt","rt")
    longfija_a_csv=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\longfija_a_csv.txt","wt")
    cantlineas=0
    lineaorig=''
    lineadest=''       
    cant=0
    suma=0
    prom=0
    primeralinea=True
    for lineaorig in longfija:
        lineadest=lineaorig[0:15]+";"+lineaorig[15:23]+";"+lineaorig[23:63] #+"\n"
        cantlineas+=1        
        longfija_a_csv.write(lineadest)
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Archivo procesado. Lineas procesadas: ", cantlineas)
finally:
    try:
        longfija.close()
        longfija_a_csv.close()
    except NameError:
        pass

#
import random

try:
    archlluvias=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\lluvias.txt","wt")    
    cantreg=random.randint(50,200)
    cont=0
    cantlineas=0
    while cont<=cantreg:
        dia=str(random.randint(1,28))
        mes=str(random.randint(1,12))
        mm=str(random.randint(200,1000))
        linea=dia +';'+ mes +';'+ mm +'\n'                       
        archlluvias.write(linea)
        cont+=1
        cantlineas+=1
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Proceso Finalizado. Lineas procesadas: ", cont)
finally:
    try:
        archlluvias.close()
    except NameError:
        pass

try:
    archlluvias=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\lluvias.txt","rt")
    m=[]
    for i in range(31):
        m.append([0]*13)        
    for linea in archlluvias:
        linea=linea.rstrip("\n")
        linea=linea.split(";")        
        m[linea[0]][linea[1]] += linea[2]   # Importante usa los datos de la linea del archivo para ubicarlos en filas y columnas                
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Proceso Finalizado. Lineas procesadas: ", cont)
finally:
    try:
        archlluvias.close()
    except NameError:
        pass

#
    try:
        rangoalturas=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\rangoalturas.txt","rt")
        promediolturas=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\promediolturas.txt","wt")
        cantlineas=0
        lineaorig=''
        #lineadest=''
        cant=0
        suma=0
        prom=0
        primeralinea=True
        for lineaorig in rangoalturas:
            cantlineas+=1
            if not lineaorig.rstrip("\n").isalpha():
                cant+=1
                suma+=float(lineaorig.rstrip("\n"))
                prom=suma/cant
                #lineadest=''.join(lineaorig) + "\n"
                #linea=lineaorig
            elif primeralinea:
                primeralinea=False
                promediolturas.write(lineaorig)            
            else:
                promediolturas.write(str(prom)+"\n") #Si llegó acá es porque en origen leyó un NUEVO deporte. Así que a imprimir el último cálculo de promedio del deporte anterior
                promediolturas.write(lineaorig)                                               
                cant=0
                suma=0
        promediolturas.write(str(prom)+"\n")                
                
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Archivo procesado. Lineas procesadas: ", cantlineas)
    finally:
        try:
            rangoalturas.close()
            promediolturas.close()  
        except NameError:
            pass   
def MostrarMasAltos():
    pass

#
"""La función de Ackermann A(m,n) se define de la siguiente forma:
                                                n+1 si m = 0
                                                A(m-1,1) si n = 0
                                                A(m-1,A(m,n-1)) de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de m entre
0 y 3 y de n entre 0 y 7."""
def a(m,n):
    if m==0:        
        return(n+1)
    elif n==0:
        return a(m-1,1)
    else:
        return(a(m-1,a(m,n-1)))
print(a(3,7))
    

 # Por falta de Return!!!! TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'


#
"""Realizar una función recursiva para imprimir una matriz de M x N."""

def print_recursive(matrix, i=0, j=0):
    if i < len(matrix):
        row = matrix[i]
        if i == len(matrix) and j == len(row):
            return
        elif j == len(row):
            print_recursive(matrix, i + 1)
        else:
            print(row[j])
            print_recursive(matrix, i, j + 1)


if __name__ == '__main__':
    matrix = []
    row1 = [1, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    print_recursive(matrix)
    
    
#
"""Escribir una función que sume todos los elementos de una matriz de M x N y de-
vuelva el resultado."""


def summation_recursive(m, i=0, j=0, s=0):
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return s
    elif j == len(m[i]) - 1:
        return summation_recursive(m, i + 1, 0, s)
    else:
        return summation_recursive(m, i, j + 1, s + m[i][j])

#
def determinarminimo(m, i=0, j=0, min=None):
    if min is None:
        min=m[0][0]
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return min
    elif j == len(m[i]) - 1:
        return determinarminimo(m, i + 1, 0, min)
    else:
        if min > m[i][j]:
            min=m[i][j]            
        return determinarminimo(m, i, j + 1, min)


if __name__ == '__main__':
    matriz = []
    row1 = [10, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matriz.append(row1)
    matriz.append(row2)
    matriz.append(row3)
    print(determinarminimo(matriz))

#
cad = ','.join('abc') 
print(cad) # a, b, c
#
a = 15 
cad = '*{:5}*'.format(a) 
print(cad) # * 15*
"""
*   15*
"""
#
#
print("-" 
* 40) 
print("Industrias Alimenticias S.A.".center(40)) 
print( ) 
print("Avenida del Campo 279".ljust(20), end="") 
print( ) 
numero = 12 
print("Factura NO", str(numero).zfill(8)) 
print( ) 
articulo = "94156 Aceite de oliva premium" 
print(articulo.lstrip("0123456789 ").ljust(30,"."),end="")
precio = 416 
print(str(precio).rjust(10,'.')) 
print("-" * 40)
"""
----------------------------------------
      lndustrias Alimenticias S.A.      

Avenida del Campo 279
Factura NO 00000012

Aceite de oliva premium..............416
----------------------------------------
"""
#