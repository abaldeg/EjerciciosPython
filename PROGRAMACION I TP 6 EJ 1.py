#Desarrollar un programa para eliminar todos los comentarios de un programa escrito
#en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
#signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
#y que también se considera comentario a las cadenas de documentación (docstrings).
#C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\tp 6 ej 3.py

try:
    archentrada=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\tp 6 ej 3.py",rt)
    archsalida=open(r"C:\Users\abald\OneDrive\Documentos\GitHub\EjerciciosPython\tp_archivos\tp 6 ej 3_sinComentarios.py",wt)
    cantlineas=0
    for linea in archentrada:
        linea=linea.rstrip(r"\n#""")
        archsalida.write(linea)
        cantlineas+=1
except FileNotFound as mensaje:
    print("No se puede abrir el archivo: ", mensaje)
except OSError as mensaje:
    print("Error: ", mensaje)
else:
    print("Copia Finalizada")
    

    
        
        
            
            
