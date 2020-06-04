#Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
#las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
#un programa para imprimir los números enteros entre 1 y 100000, y que solicite
#confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
n=1
while n<=10000:
    try:
        n+=1
        print(n)
        print()
    except KeyboardInterrupt:        
        r=input("Seguro que quiere terminar? (S=confirma)")
        if r=="S":
            break      
    