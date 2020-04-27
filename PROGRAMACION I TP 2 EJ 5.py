#Escribir un programa que calcule la suma acumulada a partir de una lista de números.
#El programa debe generar una nueva lista donde el primer elemento es el mismo
#de la lista original, el segundo elemento es la suma del primero más el segundo,
#el tercer elemento es la suma del primero más el segundo más el tercero y así
#sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].

#Funciones
def sumaAcumulada(listaOriginal):    
    listaAcumulada.append(listaOriginal[0])
    sumaAcumulada=listaOriginal[0]
    for i in range(1,len(listaOriginal)):        
        listaAcumulada.append(listaOriginal[i]+sumaAcumulada)
        sumaAcumulada=sumaAcumulada+listaOriginal[i]
    return

#Programa Principal
listaOriginal=[1,2,3]
listaAcumulada=[]
sumaAcumulada(listaOriginal)
for i in range(len(listaAcumulada)):    
    print("%3d" %listaAcumulada[i], end="")
