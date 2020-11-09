'''
Conversión binario a decimal:
Validar números positivos.
Validar que sólo contenga 0 y 1.
Convertir a decimal.
Crear una excepción propia para lanzar e informar el error.
Capturarla desde otra función o bien desde el programa ppal.
Utilizar assert y raise

'''
import sys

# Crear una excepción propia
class NumberNotBinaryError(Exception):
    pass

def es_binario(valor):
    valorStr= str(valor) # Lo convierto en un objeto iterable
    esBin= True
    for car in valorStr:
        if car!="0" and car!="1" and car!="-":
            esBin= False
    return esBin

def binario_decimal(binarioStr):
    '''Convierte a decimal o lanza una excepción si detecta un error.
    '''
    
    if not es_binario(binarioStr):
        raise NumberNotBinaryError("El número " + str(binarioStr) + " no es binario.")
    binario= int(binarioStr)
#     Validar números positivos
    # Lanzar una excepción (assert)
    assert (binario>=0), "No se aceptan números negativos."
    # Lanzar una excepción (raise)
#     if binario<0:
#         raise ValueError("No se aceptan números negativos.")
#     if binario<0:
#         raise NumberNotBinaryError("No se aceptan números negativos.")
    
    expo= 0
    decimal= 0
    while binario>0:
        ultDig= binario%10
        decimal= decimal + ultDig*2**expo
        expo+= 1
        binario= binario//10
    return decimal

def main():
    # Ejemplos: 101 -> 5, 102: Error, a1: Error, -101: Error
    # print(100/0)
    # Manejo de excepciones
    while True:
        # Capturar la excepción
        try:
            binario= input("Ingrese un número binario: ")
            print(binario_decimal(binario))
        except (AssertionError) as error:
            print("AssertionError: " + str(error))
        except (NumberNotBinaryError) as error:
            print(error)
        except:
            print("Error inesperado!")  # No se recomienda
                                        # Porque no vemos el tipo de error que se genera
            print(sys.exc_info()[0])
        else: # Cuando NO ocurre una excepción
            break
        
# Prog Ppal
main()
