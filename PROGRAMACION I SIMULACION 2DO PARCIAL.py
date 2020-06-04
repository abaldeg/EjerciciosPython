def determinarPrimo2(n, divisor=None):
    flagPrimo=True
    #Primera pasada
    if divisor is None:
        divisor = n - 1
    if divisor >= 2 and n % divisor == 0:
        flagPrimo=False    
    elif divisor >= 2:
        return determinarPrimo2(n, divisor-1)
    else:
        flagPrimo=True        
    return (flagPrimo)

n=int(input("Enter number: "))
print(determinarPrimo2(n))


