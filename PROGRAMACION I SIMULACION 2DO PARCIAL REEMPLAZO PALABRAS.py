try:
    palabraVieja=input("Ingrese palabra para buscar: ") #elementos
    palabraNueva=input("Ingrese palabra para buscar: ") #sub-elementos    
    
    archentrada=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\PalabraVieja.txt","rt")
    archsalida=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\PalabraNueva.txt","wt")
    cantlineas=0
    for linea in archentrada:
        palabras=linea.split()
        for i in range(len(palabras)):
            if palabras[i]==palabraVieja:
                palabras[i]=palabraNueva
        linea=' '.join(palabras) + "\n"
        archsalida.write(linea)
        cantlineas+=1
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Copia Finalizada. Lineas procesadas: ", cantlineas)
finally:
    try:
        archentrada.close()
        archsalida.close()
    except NameError:
        pass