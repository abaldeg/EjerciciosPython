#Lista sentencias
lstPalabrasN = [x for x in lstPalabras if len(x) >= 6]
#
frase.split()
#
for i in range(n):
    m.append([0]*n)
#
for i in range(n+1):
    matriz[0][i] = i
    matriz[i][0] = i
#
numeros=[ ]
for f in range(n):
    for c in range(n):
        azar = random.randint(0,cantidad-1)
        while azar in numeros:
            azar = random.randint(0,cantidad-1)
        mat[f][c] = azar
        numeros.append(azar)
#
for f in range(tam):
    for c in range(tam):
        print("%3d" %mat[f][c],end ="")
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
Sliced_List=List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
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

