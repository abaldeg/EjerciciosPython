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
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa-tarifa*0.20))
    
    elif cantViajes >= 31 and cantViajes <= 40:
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa-tarifa*0.20))+((cantViajes-30)*(tarifa-tarifa*0.30))
    
    elif cantViajes > 40:
        costoTotal=(20*tarifa)+((cantViajes-20)*(tarifa-tarifa*0.20))+((cantViajes-30)*(tarifa-tarifa*0.30))+((cantViajes-40)*(tarifa-tarifa*0.40))
    
    return costoTotal

cantViajes=int(input("Cantidad de viajes: "))
print("Gasto total: ", CalcularGastos(cantViajes))

        
        
        
        
                   
    