#Escribir un programa que permita grabar un archivo los datos de lluvia caída durante
#un año. Cada línea del archivo se grabará con el siguiente formato:
#<dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
#Los datos se generarán mediante números al azar, asegurándose que las fechas
#sean válidas. La cantidad de registros también será un número al azar entre 50 y
#200.
#Por último se solicita leer el archivo generado e imprimir un informe en formato
#matricial donde cada columna represente a un mes y cada fila corresponda a
#los días del mes. Imprimir además el total de lluvia caída en todo el año.
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
        m[linea[0]][linea[1]] += linea[2]                   
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


