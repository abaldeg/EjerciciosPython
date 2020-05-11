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



# Nested list comprehension 
matrix = [[j for j in range(5)] for i in range(5)] 
print(matrix)

# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
# Nested List comprehension with an if condition 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
          
print(flatten_planets) 

