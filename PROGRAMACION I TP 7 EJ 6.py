"""La función de Ackermann A(m,n) se define de la siguiente forma:
                                                n+1 si m = 0
                                                A(m-1,1) si n = 0
                                                A(m-1,A(m,n-1)) de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de m entre
0 y 3 y de n entre 0 y 7."""
def a(m,n):
    if m==0:        
        return(n+1)
    elif n==0:
        return a(m-1,1)
    else:
        return(a(m-1,a(m,n-1)))
print(a(3,7))
    

 # Por falta de Return!!!! TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'