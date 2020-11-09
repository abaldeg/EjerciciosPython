def contarRecursivoDic(matriz, valor, f=0):
    if f == len(matriz):
        return 0
    else:
        #recorro toda una fila:
        sumaFila=0
        for c in range(len(matriz[f])):
            if matriz[f][c] == valor:
              sumaFila+=1
        return sumaFila + contarRecursivo(matriz,valor, f+1) 
Dic={[1,1],[1,1]}
print(contarRecursivo(matriz,1))