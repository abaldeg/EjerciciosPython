cant=int(input("Ingrese cantidad: "))
pciobase=float(input("Ingrese precio base: "))

if cant <=12:
    precio = pciobase * cant

if cant > 12 and cant <= 100:
    precio = pciobase*12 + (pciobase*0.9)*(cant-12)
    #Para los primeros 100 menos 12 que ya calculamos.
    
if cant > 100:
    precio = pciobase*12 + (pciobase*0.9)*(cant-88) + (pciobase * 0.75) * (cant-100)
    #Para los ultimos 100. por eso cantidad menos 100
    
print ("El precio a pagar es", precio)

