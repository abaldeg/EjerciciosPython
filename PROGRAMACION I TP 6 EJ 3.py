"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio() Graba en un archivo los promedios de las alturas de los atletas
presentes en el archivo generado en el paso anterior. La disciplina y el promedio
deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.


"""


def GrabarRangoAlturas():
    """<Deporte 1>
    <altura del atleta 1>
    <altura del atleta 2>"""
   
    
    try:
        rangoalturas=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\rangoalturas.txt","wt")
        cantlineas=0
        linea=''
        deporte=(input("Ingrese deporte (Enter Sale)"))
        while deporte != "":
            linea=deporte + '\n'
            rangoalturas.write(linea)
            altura=input("Altura del Atleta: (Enter Sale)")
            while altura != "":
                linea=altura + '\n'
                rangoalturas.write(linea)
                cantlineas+=1
                altura=input("Altura del Atleta: (Enter Sale)")
            deporte=(input("Ingrese deporte (Enter Sale)"))                            
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Archivo procesado. Lineas procesadas: ", cantlineas)
    finally:
        try:
            rangoalturas.close()            
        except NameError:
            pass    
    

def GrabarPromedio():
    """
    Graba en un archivo los promedios de las alturas de los atletas
    presentes en el archivo generado en el paso anterior. La disciplina y el promedio
    deben grabarse en líneas diferentes. Ejemplo:
    <Deporte 1>
    <Promedio de alturas deporte 1>
    <Deporte 2>
    <Promedio de alturas deporte 2>
    < . . . >
    """
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
                promediolturas.write(str(prom)+"\n") 
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

#GrabarRangoAlturas()
GrabarPromedio()