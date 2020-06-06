# Practica 6 - Ejercicio 4

try:
    entrada = open("Apellidos.txt")
    armenia = open("armenia.txt", "wt")
    italia = open("italia.txt", "wt")
    españa = open("españa.txt", "wt")
    print("\nLeyendo datos...")
    datos = entrada.readline()
    while datos:
        if datos.upper().find("IAN,")!=-1:
            armenia.write(datos.title()+"\n")
        elif datos.upper().find("INI,")!=-1:
            italia.write(datos.title()+"\n")
        elif datos.upper().find("EZ,")!=-1:
            españa.write(datos.title()+"\n")
        datos = entrada.readline()
    print("Archivos generados correctamente")
except FileNotFoundError:
    print("No se encontró el archivo de entrada")
except OSError as error:
    print("ERROR:",str(error))
finally:
    try:
        entrada.close()
        armenia.close()
        italia.close()
        españa.close()
    except NameError:
        pass