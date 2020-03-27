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