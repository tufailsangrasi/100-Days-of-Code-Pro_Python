# List and Read the Data Structure Documentation from python doc
states_of_america = ["Alabama" , "Alaska" , "Arizona" , "Arkansas" , "California"]
print(states_of_america[1])
# the last item in the list strated with -1
print(states_of_america[-2])
print(states_of_america[-1])

states_of_america[0] = "Canada"
print(states_of_america)

states_of_america.append("france")
print(states_of_america)

# Nested List

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
 # dirty_dozen = [fruits , vegetables]