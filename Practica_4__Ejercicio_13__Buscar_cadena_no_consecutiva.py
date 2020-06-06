# Práctica 4, Ejercicio 13

# NOTA: Las cadenas son fijas para facilitar la prueba del programa, pero pueden ser modificadas a voluntad.

cad = "Platero es pequeño, peludo, suave. Tan blando por fuera, que se diría todo de algodón. Que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros, cual dos escarabajos de cristal negro."
cad2 = "uade"
cad1 = cad.lower()
veces = 0
inicio = 0
seguir = True
while seguir:
    for letra in cad2:
        pos = cad1.find(letra, inicio)
        if pos!=-1:
            inicio = pos + 1
            # Descomentar las dos líneas siguientes para visualizar dónde se halló la letra
            # print(cad1[pos:])
            # print()
        else:
            seguir = False
            break
    else:
        veces = veces + 1
print("La subcadena '",cad2,"' se encontró ",veces," veces", sep="")