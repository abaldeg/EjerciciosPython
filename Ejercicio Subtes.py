"""
[20:05] Galati Veronica Alejandra
    
Metrovias lo contrata para renovar el sistema de cartelera de subtes.

Le brinda un archivo que contiene un registro por línea de subte con el siguiente formato:
letra del subte;estacion1;estacion2:combinacion;estacion3

Para cada estacion separa con : indicando la letra correspondiente si existe combinacion,
en caso de mas de una combinacion en esa estacion se separan por comas.

Ejemplo:
A;San Pedrito;Primera Junta;Acoyte;Rio de Janeiro;Plaza Miserere:H;Congreso;Saenz Peña;Lima:C;Av de Mayo;Peru:D,E;Plaza de Mayo


Desea implementar un programa interactivo, como prueba piloto en la estación cabecera donde el usuario del subte puede
seleccionar la linea de subte y le muestra solamente las estaciones con combinaciones y cuales son.
El programa finaliza cuando no se ingresa linea.


Espera el siguiente comportamiento y formato de salida de la información:
ingrese linea a consultar: A
Linea A
Combinacion con linea C en Miserere
Combinación con línea D,E en Lima
ingrese linea a consultar: enter
finaliza el programa.


La empresa cuenta con un sector de calidad que le asignará un % de cumplimiento si logra respetar:
1. Toda función debe estar documentada, ser pura y estar implementada en un módulo separado al programa principal.
2. Uso de variables y funciones con nombres significativos.
3. El algoritmo planteado no supera las 50 líneas de código en total.


No le aceptarán el programa si no cumple lo siguiente:
1. El algoritmo planteado no resuelve el problema planteado.
2. La lectura del archivo se debe realizar Una sola vez y no debe cargar el contenido completo en memoria.


La empresa confía en su experiencia para diseñar una solución!
"""
def ingresarlinea():
    """Solicita al usuario la linea de subte para obtener sus combinaciones, la imprime en pantalla
    y devuelve la línea solicitada."""
    linea=input("Ingrese linea a consultar: ")
    """print()
    print(f"Línea: {linea}")
    print()"""
    return linea

def procesararchivo():
    """Procesa el archivo de líneas de subte y combinaciones.
    Carga una lista con combinaciones para la linea que entra por parámetro."""
    try:
        cont=1
        subtes=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\subtes.txt","rt",encoding='utf-8')        
        for linea in subtes:
            linea=linea.rstrip("\n")
            linea=linea.split(";")
            combinacion.append(linea[0])
            for lin in linea:
                for c in lin:
                    if c==":":
                        combinacion.append(lin.split(":"))    
        cont=+1
        print(linea)
        print(combinacion)
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)    
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Proceso Finalizado. Lineas procesadas: ", cont)
    finally:
        try:
            subtes.close()
        except NameError:
            pass    
    return

def imprimircombinaciones(linea):
    """Imprime las combinaciones según línea."""
    print()
    i=0
    while i < (len(combinacion)):
        if len(combinacion[i]) and combinacion[i]==linea.upper():
            i+=1
            while i < (len(combinacion)) and len(combinacion[i]) !=1 :
                print(f"Combinacion con linea {linea.upper()} en {combinacion[i]}")
                i+=1               
        i+=1
    return
              
#Programa Principal
combinacion=[]
procesararchivo()
linea="x"
while linea!="":
    linea=ingresarlinea()    
    imprimircombinaciones(linea)

        
