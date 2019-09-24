def fMultiplica(a,b):
    cont=1
    while cont < b:
        a=a+a
        cont=cont+1
    return a


print (fMultiplica(2,2))
print (fMultiplica(1,1))