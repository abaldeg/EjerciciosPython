"""
Contraseñas! En general las contraseñas a crear deben cumplir reglas por seguridad
para que sean válidas. Desarrolle un programa que ingrese contraseñas hasta ingresar
una contraseña vacía. A medida que se ingresan verifique e informe si cumple con las reglas:

No puede comenzar con número. Debe contener al menos dos números, una letra mayùscula y
una longitud de 8 caracteres mínimo.

Resolver utilizando exclusivamente manejo de excepciones y estructura While-True, creando
una nueva excepción o utilizando una existente (ValueError) cuando no cumpla alguno de las
dos reglas, mostrar mensaje aclaratorio correspondiente en cada caso.
"""
import sys

# Crear una excepción propia
class ErrorLongitud(Exception):
    pass

while True:
        try:            
            contnum=0
            contmay=0
            password=input("Ingrese contraseña: ")
            if len(password)==0:
                break     
            #assert password[0].isdigit()== False, "La contraseña No puede comenzar con número."
            if password[0].isnumeric():
                raise ValueError()
            for letra in password:
              if letra.isdigit():
                contnum+=1
              if letra.isupper():
                contmay+=1
            assert contnum>1, "Debe contener al menos dos números."
            assert contmay>0, "Debe tener una letra mayúscula."
            #assert len(password)>7, "Longitud de 8 caracteres mínimo."
            if len(password)<7:
                raise ErrorLongitud("Longitud de 8 caracteres mínimo.")                
            print(password)                   
        except ValueError:
          print("No se acepta que comience con numeros.")
          print()
        except (ErrorLongitud) as error:
            print(error)
        except AssertionError as mensaje:
          print(mensaje)
