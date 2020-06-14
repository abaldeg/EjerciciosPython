def aVeryBigSum(ar):
    sum=0
    l=ar[0].strip().split(' ')
    for i in range(len(l)):        
        sum+=int(l[i])
    return(sum)

ar=['1000000001 1000000002 1000000003 1000000004 1000000005']
print(aVeryBigSum(ar))