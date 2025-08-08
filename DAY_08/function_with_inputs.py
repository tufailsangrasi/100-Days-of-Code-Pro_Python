def greet():
    print("Good morning tufail")
    print("How do you do tufail")
    print("isn't the weather is nice , tufail")
#greet()

def greet_with_name(name): # here name is paramater
    print(f"Good morning {name}")
    print(f"How do you do {name}")
    print(f"isn't the weather is nice {name}")

greet_with_name("Tufail") # Here Tufail is Argument , because its a real data

def life_in_weeks(years):
    weeks = years * 12 * 4
    print(f"The Weeks in 90 years old life is {weeks}")

life_in_weeks(90)

# Function with more than 2 parameters
def name_of_person(first_name , last_name):
    print(f"Hello {first_name} {last_name}")
print("Tufail" , "Ahmed")

def info(name , location):
    print(f"Hello {name} {location}")
