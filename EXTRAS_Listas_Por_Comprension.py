# Create `new_list`
numbers = range(10)
# Initialize `new_list`
new_list = []

# Add values to `new_list`
for n in numbers:
    if n%2==0:
        new_list.append(n**2)

# Print `new_list`
print(new_list)

#Lo mismo!!!
new_list = [n**2 for n in numbers if n%2==0]
print(new_list)



