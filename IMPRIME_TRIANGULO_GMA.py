def imprimetriangulo(n):
    #e=n+(n//5)-3
    e=n*2-2
    for i in range(0,n):
        for x in range (0,e):
                print("-",end="")
        for j in range(0,i+1):            
            print("* ",end="")            
        print("\r")
        e-=1    
imprimetriangulo(15)