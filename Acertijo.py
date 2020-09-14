import random
num=10
n1=random.randint(1,num)
n2=random.randint(1,num)
while n1%2==0:
    n1=random.randint(1,num)
while n2%2==0:
    n2=random.randint(1,num)
    
print(n1)
print(n2)