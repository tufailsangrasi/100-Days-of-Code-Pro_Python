# Argument and Parameters
def greet():
  print("Good evening, My Name is Tufail")

#greet()

def greet_with_name(name):
  print(f"Good evening {name}")
  print(f"How do you do {name}")
  print(f"is'nt the weather is nice {name}")

greet_with_name("Tufail")

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