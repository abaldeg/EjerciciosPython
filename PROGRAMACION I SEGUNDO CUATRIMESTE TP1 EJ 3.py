"""
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa
para verificar el comportamiento de la función.

Cantidad de viajes Valor del pasaje
1 a 20 Averiguar valor actualizado
21 a 30 20% de descuento sobre tarifa máxima
31 a 40 30% de descuento sobre tarifa máxima
Más de 40 40% de descuento sobre tarifa máxima
"""
def calcularGastos(c):
    tarifa=1
    if c >=1 and c<=20:        
        total=tarifa*c
    if c >=21 and c <=30:
        total=(tarifa*20)+((tarifa*0.80)*(c-20))
    if c >=31 and c <=40:
        """seguro que 10 al 80% hay porque estamos en el rango de 31 a 40"""
        """por eso tarifa con 80% de descuento por 10 pasajes"""
        total=(tarifa*20)+((tarifa*0.80)*10)+((tarifa*0.70)*(c-30))
    if c>=40:
        total=(tarifa*20)+((tarifa*0.80)*10)+((tarifa*0.70)*(c-30))+((tarifa*0.60)*(c-40))    
    return(total)
        
print(calcularGastos(21))
print(calcularGastos(31))

