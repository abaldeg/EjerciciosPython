#Escribir un programa para crear una lista por comprensión con los naipes de la baraja
#española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros",
#"2 Oros"... ]. Imprimir la lista por pantalla.
new_list = [ (n,p) for p in ["Oro", "Copas", "Espada", "Basto"] for n in range (1,13) ]
print(new_list)

           
