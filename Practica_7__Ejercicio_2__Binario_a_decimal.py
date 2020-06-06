# Práctica 7 - Ejercicio 2

def bin2dec(bin, pos=0):
    if bin==0:
        return 0
    else:
        return bin%10*2**pos + bin2dec(bin//10, pos+1)
    
# Programa principal
n = int(input("Numero binario? "))
print(n, "equivale a", bin2dec(n), "en decimal")