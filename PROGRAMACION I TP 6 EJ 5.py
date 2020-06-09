"""Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan
datos de empleados. Los formatos se indican más abajo. Desarrollar un programa
para cada uno de los formatos suministrados, que permitan leer cada uno
de los archivos y grabar los datos obtenidos en otro archivo de texto con formato
CSV.

Archivo 1: Todos los campos son de longitud fija.
1 2 3 4 5 6
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Archivo 2: Los campos están separados por el signo #.
Pérez Juan#20080211#Corrientes 348
González Ana M#20080115#Juan de Garay 1111 3er piso Dto A
Archivo 3: Todos los campos de este archivo están precedidos por un
número de dos dígitos que indica la longitud del campo a leer.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTA: Los espacios que se encuentren al final de las cadenas en el archivo 1 deberán ser eliminados.
"""
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
    