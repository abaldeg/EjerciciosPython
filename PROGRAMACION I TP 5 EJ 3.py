#Desarrollar una función que devuelva una cadena de caracteres con el nombre del
#mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
#obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
#Devolver una cadena vacía si el número de mes es inválido. La detección de meses
#inválidos deberá realizarse a través de excepciones.

def nombrarMes(mes):
    try:
        cadenames=""
        listaMeses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]        
        cadenames=listaMeses[mes-1]
        
    except IndexError:
        print("Numero de Mes inválido: ", mes)
        cadenames=""
    
    finally:
        return(cadenames)
          
print(nombrarMes(13))
print()
print(nombrarMes(12))
    