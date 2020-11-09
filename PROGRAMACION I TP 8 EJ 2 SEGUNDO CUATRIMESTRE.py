"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
2017". Escribir también un programa para verificar su comportamiento."""
def conviertExtendida(fecha):
    """Recibe una tupla representando una fecha y la devuelve en formato extendido"""
    d,m,a=fecha
    fechaext=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")    
    m=fechaext[m]
    a=a+2000
    #fechaextendida=d,m,a
    return d,m,a

fecha=(12,10,17)
d,m,a=conviertExtendida(fecha)
print(f"Fecha extendida: {d} de {m} del {a}")