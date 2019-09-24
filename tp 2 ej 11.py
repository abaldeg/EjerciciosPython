binario = int(input("Ingrese numero binario de 4 digitos: "))

#descomponemos los digitos
digito1 = int(binario%10)



binario = binario/10

digito2 = int(binario%10)

binario = binario/10

digito3 = int(binario%10)

binario = binario/10

digito4 = int(binario%10)

#print (digito1,digito2,digito3,digito4)
print (2**0*digito1+2**1*digito2+2**2*digito3+2**3*digito4)
       
       
       
       


