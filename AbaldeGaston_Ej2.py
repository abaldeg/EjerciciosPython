matriz=[1,2],[2,1]
print(matriz)
lista = [matriz[f][c] for f in range(len(matriz)) for c in range(len(matriz[0]))]
print(lista)
print(max(lista))
maximo=max(lista)
listamaximos= ['Fila: '+str(f)+ ' Columna: '+str(c) for f in range(len(matriz)) for c in range(len(matriz[0])) if matriz[f][c]==maximo]
print(f"Máximos: {listamaximos}")
    
    
