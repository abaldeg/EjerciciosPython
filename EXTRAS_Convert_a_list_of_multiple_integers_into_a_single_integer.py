#Convert a list of multiple integers into a single integer
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L))) #map aplica una funcion a cada elemento de una lista. aplica str a L
print("Single Integer: ",x)
print ("++".join(map(str, L))) # "++" porque ya no se pasa a int

#>>> help("str.join")
#Help on method_descriptor in str:
#str.join = join(self, iterable, /)
#    Concatenate any number of strings.
    
#    The string whose method is called is inserted in between each given string.
#    The result is returned as a new string.
#    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'