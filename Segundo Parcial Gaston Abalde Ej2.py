"""
EJERCICIO 2
Hora de jugar!: Se requiere desarrollar un juego de preguntas, en que se puede
responder "si" o "no". 
Las preguntas a formular se encuentran en un archivo de texto enumeradas desde el 1 hasta 8,
la pregunta a formular y la respuesta correcta (si o no) separada por punto y coma.

Ejemplo:
1;Los diccionarios en Python poseen índice?;no
2;El caracter $ se utiliza para comentarios en Python;no
3;se pueden crear funciones con la instrucción lambda?;si

Gana quien responde correctamente 3 preguntas seleccionadas al azar entre las 8 existentes del archivo.

Si se responde mal alguna, no se formula la siguiente y termina el juego. Resolver utilizando
estructura while-true y manejo de excepciones.
(utilizar el block de notas para crear el archivo de preguntas, crear 8 preguntas relacionadas a
PrograI con su correspondiente respuesta si o no) (No utilice las preguntas de ejemplo)
No olvide entregar el archivo preguntasApellido.txt, las preguntas y respuestas que formule en el
archivo se tendrán en cuenta para asignar la nota del exámen.

"""
import random

# Excepción respuesta incorrecta
class ErrorRespuesta(Exception):
    pass

def leerarchivo():
    """Lee el archivo de preguntas y respuestas retornando su contenido en la lista de preguntas y respuestas modificadas. """
    try:
        cont=0
        archivo=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\preguntasAbalde.txt","rt",encoding='utf8') #wt
        for linea in archivo:
            linea=linea.rstrip("\n")
            linea=linea.split(";")            
            listapreguntas.append(linea[1])
            listarespuestas.append(linea[2])
            cont+=1                    
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Proceso Finalizado. Lineas procesadas: ", cont)
        print()
    finally:
        try:
            archivo.close()
        except NameError:
            pass
    return

def preguntar():    
    """Realiza las preguntas del juego sobre las listas ya cargadas en leerarchivo()"""
    cantpreg=1
    while True:
        try:            
            assert cantpreg<4, "Se alcanzó el máximo de respuestas correctas, ganó el juego!!!!."
            numpreg=random.randint(0,7)
            listapreghechas.append(numpreg)
            while numpreg not in listapreghechas:
                numpreg=random.randint(0,7)
                listapreghechas.append(numpreg)
            print("-"*len(listapreguntas[numpreg]))
            print(f"{listapreguntas[numpreg]}")
            print("-"*len(listapreguntas[numpreg]))
            respuesta=input("Contestar SI/NO: ")
            while respuesta.lower()!="si" and respuesta.lower()!="no":
                respuesta=input("Contestar SI/NO: ")                
            if respuesta.lower()==listarespuestas[numpreg].lower():                
                print()
                print("Excelente! La respuesta es correcta.")
                print()
                cantpreg+=1
            else:
                print()
                raise ErrorRespuesta("Que pena! La respuesta es incorrecta. Se terminó el juego.")
        except AssertionError as mensaje:
            print(mensaje)
            print()
            break
        except (ErrorRespuesta) as error:
            print(error)
            print()
            break        
    return

#Programa principal
listapreguntas=[]
listarespuestas=[]
listapreghechas=[]
leerarchivo()
preguntar()
    