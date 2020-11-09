"""1) Desarrollar un programa de categorización, que asigne a cada libro un código especial basado en su título:
El código es igual a la primera letra del libro, seguido del número de caracteres del título.
Por ejemplo, para el libro “Harry Potter”, el código sería: H12, ya que contiene 12 caracteres (incluyendo el espacio).
Se tiene el archivo libro.txt, que incluye el título del libro, cada uno escrito en una línea. Debe leer cada título
y listar por pantalla el código de cada libro.
Por ejemplo, si el archivo libros.txt contiene:
Harry Potter
The Shining
Emotional Intelligence
Por pantalla se debería visualizar:
H12
T11
E22
Además, deberá determinar cuál es la palabra más larga de todo el archivo de texto y mostrarla por pantalla.
Para el ejemplo anterior, se debería informar: 
Palabra más larga del archivo: Intelligence
Deberá crear una función lambda para generar el código de cada libro. 
Cree el archivo libros.txt para verificar el correcto funcionamiento del programa.
"""
def procesararchlibros():
    try:
        cont=0
        archlibros=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\libro.txt","rt")
        for linea in archlibros:
            cont=cont+1
            linea=linea.rstrip("\n")
            linea=linea.split(" ")
            cantpalabras=len(linea)
            titulo=linea[0]
            primercar=titulo[0].upper()
            cantidad=0
            cantpml=0
            for palabra in linea:
                cantidad=cantidad+len(palabra)
                if len(palabra)>cantpml:
                    cantpml=len(palabra)
                    palabraml=palabra
                    cantidad=cantidad+(cantpalabras-1)
            listalibros.append(primercar+str()+str(cantpalabras))
            codigo=primercar+str(cantidad)
            
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Proceso Finalizado. Lineas procesadas: ", cont)
    finally:
        try:
            archlibros.close()
        except NameError:
            pass
    return codigo, palabraml, listalibros

"""programa principal"""
listalibros=[]
codigo, palabraml, listalibros=procesararchlibros()
print(f"Palabra más larga del archivo: {palabraml}")
for libro in listalibros:
    print(f"Palabra más larga del archivo: {libro}")

      
      