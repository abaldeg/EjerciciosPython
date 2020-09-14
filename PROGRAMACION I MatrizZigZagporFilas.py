
"""
Zig Zag por filas
"""

def generamatzigzagxfila(n):
    mat=[[0]*n for i in range(n)]
    numero=1
    for f in range(n):
        if f%2!=0:
            for c in range(n-1,-1,-1):
                mat[f][c]=numero
                numero+=1
        elif f%2==0 or f==0:
            """es par"""
            for c in range(n):
                mat[f][c]=numero
                numero+=1            
        
    return(mat)   

def imprimirmatriz(mat):
    for fila in mat:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

"""programa principal"""
n=6

mat=generamatzigzagxfila(n)
imprimirmatriz(mat)