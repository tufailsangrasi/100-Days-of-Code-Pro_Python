import random

random_heads_or_tails = random.randint(0 , 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# list randomisation
# way 1
friends = ["Ali" , "Muzammil" , "Sanjay" , "Varoon" , "Zaheer" , "Sajid"]
print(random.choice(friends))

total_index = friends.len(friends)

#way 2
random_index = random.randint(0 , 5)
print(friends[random_index])