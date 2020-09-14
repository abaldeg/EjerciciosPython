def capicua(palabra):
    cap=True
    tamaño=len(palabra)
    i=0
    d=tamaño-1
    while i<(tamaño//2) and cap:
        if palabra[i]!=palabra[d]:
            cap=False                    
        i=i+1
        d=d-1
    return (cap)
print(capicua("anaa"))


"""
def capicua(palabra):
    cap=True
    tamaño=len(palabra)
    i=0
    d=tamaño-1
    while i<(tamaño//2) and cap:
        if palabra[i]!=palabra[d]:
            cap=False
        i=i+1
        d=d-1
    return (cap)
print(capicua("123321"))
"""