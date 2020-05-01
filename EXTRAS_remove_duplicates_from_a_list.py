#Write a Python program to remove duplicates from a list
#set() method is used to convert any of the iterable to
#sequence of iterable elements with dintinct elements, commonly called Set.
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)