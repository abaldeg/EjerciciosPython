my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

new_list2 = ['{}{}--------{}'.format(x, y,z) for z in range(1,10) for y in range(1, n+1) for x in my_list]
print(new_list2) #['p1--------1', 'q1--------1',...