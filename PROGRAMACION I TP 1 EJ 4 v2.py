#Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
#dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
#de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
#una función que reciba como parámetro la cantidad de viajes realizados en un
#determinado mes y devuelva el total gastado en viajes. Realizar también un programa
#para verificar el comportamiento de la función.
#
#Cantidad de viajes Valor del pasaje
#1 a 20 Averiguar valor actualizado
#21 a 30 20% de descuento sobre tarifa máxima
#31 a 40 30% de descuento sobre tarifa máxima
#Más de 40 40% de descuento sobre tarifa máxima
def CalcularGastos(cantViajes):
    tarifa=float(input("Valor de la tarifa: "))
    costoTotal=0
    
    if cantViajes >= 1 and cantViajes <= 20:
        costoTotal=cantViajes*tarifa
    
    elif cantViajes >= 21 and cantViajes <= 30:
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa*0.80))
    
    elif cantViajes >= 31 and cantViajes <= 40:
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa*0.80))+((cantViajes-30)*(tarifa*0.70))
    
    elif cantViajes > 40:
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa*0.80))+((cantViajes-30)*(tarifa*0.70))+((cantViajes-40)*(tarifa*0.60))
    
    return costoTotal

# Bloque Programa Principal.
cantViajes=int(input("Cantidad de viajes: "))
print("Gasto total: ", CalcularGastos(cantViajes))

#-----------------------------------------------------------------------------------
#BIEN RESUELTO:

# Práctica 1, Ejercicio 4

def calculargasto(viajes, tarifa):
    """ Devuelve el importe a pagar segun la cantidad de viajes realizados,
        considerando el esquema de tarifas decrecientes vigente """
    tarifa1 = tarifa*0.80  # tarifa con el 20% de descuento
    tarifa2 = tarifa*0.70  # tarifa con el 30% de descuento
    tarifa3 = tarifa*0.60  # tarifa con el 40% de descuento
    if viajes<=0:
        total=0
    elif viajes<=20:
        total = viajes*tarifa
    elif viajes<=30:
        total = 20*tarifa+(viajes-20)*tarifa1
    elif viajes<=40:
        total = 20*tarifa+10*tarifa1+(viajes-30)*tarifa2
    else:
        total = 20*tarifa+10*tarifa1+10*tarifa2+(viajes-40)*tarifa3
    return total

# Programa principal
n = int(input("Cantidad de viajes? "))
p = float(input("Precio del pasaje? "))
importe = calculargasto(n, p)
print()
print("Por", n, "viajes se gastaron $", importe)
print()

        
        
        
        
                   
    