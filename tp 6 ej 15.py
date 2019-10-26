# """ Ejercicio 15: 
# Leer dos listas de números M y N, ambas ordenadas de menor a mayor. Generar 
# e imprimir una tercera lista que resulte de intercalar los elementos de M y N. La 
# nueva lista también debe quedar ordenada, sin utilizar ningún método de orde- 
# namiento. 

M=[1,2,3,4,5]
N=[100,200,300,400,500]
l=[]
largo=len(M)

for i in range(largo):
    l.append(M[i])
    l.append(N[i])

largo=len(l)
for i in range(largo):
    print(l[i],end=" ")
    



