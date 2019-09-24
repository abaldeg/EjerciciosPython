import statistics
int1 = int(input("Ingrese primer numero entero:"))
int2 = int(input("Ingrese segundo numero entero:"))
int3 = int(input("Ingrese tercer numero entero:"))
#promedio = int(statistics.mean(int1,int2,int3))
promedio = int((int1+int2+int3)/3)
print
print ("El promedio es: ",promedio)
