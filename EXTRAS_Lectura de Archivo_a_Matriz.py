matrix = open(r'C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\numeros.txt').read()
matrix = [item for item in matrix[:-1]]
print(matrix)

#matrix = [item for item in matrix[:-1]]
#['1', ' ', '2', ' ', '3', '\n', '4', ' ', '5', ' ', '6', '\n', '7', ' ', '8', ' ', '9']

#matrix = [item for item in matrix.split('\n')[:-1]]
#['1 2 3', '4 5 6', '7 8 9']

#matrix = [item.split() for item in matrix.split('\n')[:-1]]
#[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

#matrix = [item.split() for item in matrix.split('\n')[:]]
#[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], []]