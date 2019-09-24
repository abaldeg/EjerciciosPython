imp=float(input("Ingrese importe factura:"))

if (imp * 0.98) < (imp - 120):
    imp_1_10 = imp * 0.98
else:
    imp_1_10 = imp - 120

if (imp*1.10) > (imp + 150):
    imp_21 = imp * 1.10
else:
    imp_21 = imp + 150

print("El importe a pagar del 1 al 10 es:", imp_1_10, ". Del 11 al 20:", imp, ". Despues del 21:",imp_21)