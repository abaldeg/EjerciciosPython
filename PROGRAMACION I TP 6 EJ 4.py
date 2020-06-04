#Escribir un programa que lea un archivo de texto conteniendo un conjunto de
#apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
#ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
#cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
#ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
#Arslanian, Gustavo –> ARMENIA.TXT
#Rossini, Giuseppe –> ITALIA.TXT
#Pérez, Juan –> ESPAÑA.TXT
#Smith, John –> descartar
#El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
#escribir un programa para generarlo.
#C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\apellidos.txt
try:
    archentrada=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\apellidos.txt","rt")
    archarmenia=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\ARMENIA.txt","wt")
    architalia=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\ITALIA.txt","wt")
    archespaña=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\ESPAÑA.txt","wt")
    
    cantlineas=0
    for linea in archentrada:        
        lstpalabras=linea.split(",")
        apellido=lstpalabras[0]        
        if apellido[-1:-4:-1]=="nai":
            archarmenia.write(linea)
            cantlineas+=1
        elif apellido[-1:-4:-1]=="ini":
            architalia.write(linea)
            cantlineas+=1
        elif apellido[-1:-3:-1]=="ze":
            archespaña.write(linea)
            cantlineas+=1
        
        
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Proceso Finalizado. Lineas procesadas: ", cantlineas)
finally:
    try:
        archentrada.close()
        archarmenia.close()
        architalia.close()
        archespaña.close()
    except NameError:
        pass
