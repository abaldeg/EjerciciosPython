"""Cree un programa que ingrese primero el apellido y a continuación el nombre,
deberá crear una cadena que contenga Apellido una coma un espacio y el Nombre
(si tiene doble apellido o doble nombre, debe contener un solo espacio entre cada palabra).
Luego se solicita que lo muestre por pantalla centrado (Considerando una pantalla con 80 columnas de ancho)
y alternando mayúsculas y minúsculas por palabra. Ejemplo: Martinez, Juan Pedro
MaRtInEz, JuAn PeDrO"""
apellido=input("Ingrese Apellido: ")
nombre=input("Ingrese Nombre: ")
apellido=apellido.split()
if len(apellido)>1:
    apellido[1:1]=" "
apellido.append(", ")
apellido="".join(apellido)
nombre_completo=apellido+nombre
print(nombre_completo.center(80))
    