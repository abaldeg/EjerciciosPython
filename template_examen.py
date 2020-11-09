#Listas, Tuplas, Conjuntos, Diccionarios
mail = mail.replace("@",".")    
listamail = mail.split(".") #split devuelve una lista, ojo.
tuplamail=()
for i in listamail:
    tuplamail = tuplamail + (i,)

conjunto=set()
conjunto={3,4,5}
conjunto.add(6)
print(conjunto)
conjunto.remove(6)
print(conjunto)
conjunto.add(6)
print(conjunto)
conjunto.discard(6)
print(conjunto)
x=conjunto.pop()
numeros.remove(num)

edades={"Dante":27,"Brenda":18,"Malena":23}
print(edades["Brenda"])
colores={
    "Rojo":[255,0,0],
    "Verde":[0,255,0],
    "Azul":[0,0,255]         
         }
claves=list(colores.keys())
valores=list(colores.values())
items=list(colores.items())
a= colores.get("negro","no está") #si no esta no da runtime error
dic = {x:x**2 for x in range(1,5)}
for color, RGB in colores.items():
  print(color," ", RGB)
dias="Lunes","martes" #Tupla
d1=dict.fromkeys(dias)
productos = {x:random.randint(1,10000) for x in range(1,101)}
for producto in productos:
    print(f"Producto: {producto}, precio: " + format(productos[producto],'.2f'))
def precioMasCaro(productos):
    listavalores=(productos.values())    
    return max(listavalores)
for i, letra in enumerate(lista):
    print(i, letra) # O a, 1 e, 2 i... 
print(max(cad))
print(min(cad))
print(cad.count("a"))
print(cad.index("rama"))
# lo contrario a split
cad="12345"
cad=";".join(cad)
print(cad)
cad=cad.replace("frío","húmedo")

#invertir la lista o cadena
cad="Programar me encanta"
cad=cad[::-1]
#atnacne em ramargorP

#estás como Hola
frase="Hola como estás"
palabras=frase.split()
palabras.reverse()
frase=" ".join(palabras)
print(frase)
print(cad.isalpha())
print(numero.isalnum())
print(cad.upper())
print(cad.lower())
print(frase.capitalize())
print(frase.title())
print(cad.center(80,"-"))
print(cad.ljust(80,"-"))
print(cad.rjust(80,"-"))
print(cad.zfill(50))
print(cad.lstrip("-"))
print(cad.rstrip("-"))
print(cad.strip("-"))
print(cad.find("mundo"))
print(1,"/",12,"/",2019,sep="") #1/12/2019

# Excepciones
# Crear una excepción propia
class Errorpersonalizado(Exception):
    pass

raise ValueError()
assert cont>1, "cont debe ser mayor a 1."
raise Errorpersonalizado("Mensaje de error.")  

except ValueError:
    print("No se acepta que comience con numeros.")
    print()
except (ErrorLongitud) as error:
    print(error)
except AssertionError as mensaje:
    print(mensaje)
#-----------------------------------------------------------------------
#Archivos
try:
    archivo=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\archivo.txt","rt") #wt
    
    for linea in archivo:
        linea=linea.rstrip("\n")
        linea=linea.split(";")        
                         
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Proceso Finalizado. Lineas procesadas: ", cont)
finally:
    try:
        archivo.close()
    except NameError:
        pass
#-----------------------------------------------------------------------