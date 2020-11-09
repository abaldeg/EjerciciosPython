"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar)."""

def splitmail(mail):
    mail = mail.replace("@",".")    
    listamail = mail.split(".") #split devuelve una lista, ojo.
    tuplamail=()    
    for i in listamail:
        tuplamail = tuplamail + (i,)
    return tuplamail

mail=splitmail("alguien@uade.edu.ar")
print(f"Mail desarmado: {mail}")