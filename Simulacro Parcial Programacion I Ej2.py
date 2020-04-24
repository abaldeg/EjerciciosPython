
# Funciones
def crearMatrix1(n):    
    mat=[ ]
    for i in range(n+1):
        mat.append([0] * (n+1))
        
    for i in range(n+1):
        mat[0][i] = i
    
    for i in range(n+1):
        mat[i][0] = i
    
    return (mat)

def crearMatrix2(n):    
    mat=[ ]
    for i in range(n+1):
        mat.append([0] * (n+1))
        
    for f in range(n+1):
        for c in range(n+1):
            mat[f][c] = f*c
    
    return (mat)

# Programa Principal
n = int(input("Ingrese número entero positivo: "))
mat=crearMatrix1(n)
for f in range(n+1):
    for c in range(n+1):
        print("%3d" %mat[f][c], end ="")
    print()
mat=crearMatrix2(n)
for f in range(n+1):
    for c in range(n+1):
        print("%3d" %mat[f][c], end ="")
    print()
