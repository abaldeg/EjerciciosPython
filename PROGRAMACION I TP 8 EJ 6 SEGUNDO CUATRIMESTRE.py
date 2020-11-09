"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud."""

def ordenarlista(lista):       
    return len(lista)
   
palabras=set()
palabra=input("Ingresar palabra: ")
while palabra != "":
    palabras.add(palabra)   
    palabra=input("Ingresar palabra: ")
lista=list(palabras)
#lista.sort(key=ordenarlista)
lista.sort(key=lambda pal:len(pal))
print(palabras)
print(lista)