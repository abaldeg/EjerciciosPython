# Resolución Segundo Parcial (Todos los temas)

def formatearnumero(num):
    return f"$ {num:,}"

try:
    arch = open("ProduccionFinal.txt", "rt")
    produccion = [0] * 32   # La posicion 0 no se utiliza
    termotanques = [0] * 32 # La posicion 0 no se utiliza
    heladeras = [0] * 32    # La posicion 0 no se utiliza
    aires = [0] * 32        # La posicion 0 no se utiliza
    productos = []          # Lista con la descripcion de los productos
    cantidadproducida = []  # Lista con la cantidad producida de cada artículo
    dias = []               # Esta lista se usa para calcular el promedio de unidades por día
    totalinvertido = 0
    lavarropas = 0
    lavavajillas = 0
    microondas = 0
    cant = 0
    for linea in arch:
        dia, descripcion, costo = linea.rstrip("\n").split(";")
        produccion[int(dia)] += 1
        if descripcion not in productos:
            productos.append(descripcion)
            cantidadproducida.append(1)     # Estas dos listas son paralelas. Una contiene el nombre y la otra lacantidad fabricada.
            dias.append([int(dia)])         # Lista de listas con los dias de fabricación de cada artículo
        else:
            posicion = productos.index(descripcion)
            cantidadproducida[posicion] += 1
            if int(dia) not in dias[posicion]:
                dias[posicion].append(int(dia))   # Agregamos el día a la sublista de este producto
        if descripcion.lower()=="lavarropas":
            lavarropas += int(costo)
        if descripcion.lower()=="lavavajillas":
            lavavajillas += int(costo)
        if descripcion.lower()=="microondas":
            microondas += int(costo)
        if descripcion.lower()=="termotanque":
            termotanques[int(dia)] += 1
        if descripcion.lower()=="heladera":
            heladeras[int(dia)] += 1
        if descripcion.lower()=="aire acondicionado":
            aires[int(dia)] += 1
        totalinvertido += int(costo)
        cant = cant + 1
except (FileNotFoundError, OSError) as error:
    print("ERROR DE ARCHIVO:", error)
finally:
    try:
        arch.close()
    except NameError:
        pass
print(cant, "registros procesados")
# Dias del mes con mayor produccion
maximo = max(produccion)
print("\nLa mayor producción diaria fue de", maximo, "unidades, y se verificó los días", end = " ")
for dia, valor in enumerate(produccion):
    if valor==maximo:
        print(dia, end=" ")
print()
# Producto con menor cantidad de unidades fabricadas
productomenosfab = min(cantidadproducida)
print("Los productos menos fabricados fueron", end= " ")
for i, cantidad in enumerate(cantidadproducida):
    if cantidad==productomenosfab:
        print(productos[i].lower(), end=" ")
print("con", productomenosfab, "unidades")
print("Total de dinero invertido en lavarropas:", formatearnumero(lavarropas))
# Dias del mes con menor produccion
minimo = min(produccion[1:])  # El subíndice 0 no se usa
print("\nLa menor producción diaria fue de", minimo, "unidades, y se verificó los días", end = " ")
for dia, valor in enumerate(produccion):
    if valor==minimo:
        print(dia, end=" ")
print()
# Producto con mayor cantidad de unidades fabricadas
productomasfab = max(cantidadproducida)
print("Los productos más fabricados fueron", end= " ")
for i, cantidad in enumerate(cantidadproducida):
    if cantidad==productomasfab:
        print(productos[i].lower(), end=" ")
print("con", productomasfab, "unidades")
print("Total de dinero invertido en toda la produccion:", formatearnumero(totalinvertido))
print()
# Dias del mes con mayor produccion de termotanques
maximo = max(termotanques)
print("La mayor producción diaria de termotanques fue de", maximo, "unidades, y se verificó los días", end = " ")
for dia, valor in enumerate(termotanques):
    if valor==maximo:
        print(dia, end=" ")
print()
# Promedio de unidades producidas de cada producto
print("Promedio de unidades fabricadas por día:")
for i, descripcion in enumerate(productos):
    cantdias = len(dias[i])
    print("  - "+descripcion+f": {cantidadproducida[i]/cantdias:.2f} unidades")
print("Total de dinero invertido en lavavajillas:", formatearnumero(lavavajillas))
# Dias del mes con mayor produccion de heladeras
maximo = max(heladeras)
print("\nLa mayor producción diaria de heladeras fue de", maximo, "unidades, y se verificó los días", end = " ")
for dia, valor in enumerate(heladeras):
    if valor==maximo:
        print(dia, end=" ")
print()
# Dias del mes con mayor produccion de aires acondicionados
maximo = max(aires)
print("La mayor producción diaria de aires acondicionados fue de", maximo, "unidades, y se verificó los días", end = " ")
for dia, valor in enumerate(aires):
    if valor==maximo:
        print(dia, end=" ")
print()
print("Total de dinero invertido en microondas:", formatearnumero(microondas))
