import random
print("Welcome to Pypassword Generator")
letters = ['a', 'b', 'c','x', 'y', 'z', 'A', 'B', 'C', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# Easy level
password = ""
for char in range(1 , nr_letters+1):
    password += random.choice(letters)

for char in range(1 , nr_numbers+1):
    password += random.choice(numbers)

for char in range(1, nr_symbols+1):
    password += random.choice(symbols)


print(password)

# Hard Level
password_list= []
for char in range(1 , nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1 , nr_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")
