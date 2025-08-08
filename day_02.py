# Print the datatypes using f string
marks = 90
grade = "A+"
# Ask from user
name = input("Whats your name?")
print(f"Congratulations!{name} you scored is {marks} and your grade is {grade}")

# As python is dynamic language , how to find the datatype of variable
print(type(marks))
print(type(grade))
print(type(name))

# Typecasting Converting string into integer
print(int('123')+int('345'))

# BMI Calculator
height = float(input("Enter the height in metres:"))
weight = float(input("Enter the weight in kilograms:"))

bmi = round((weight / (height**2)) , 2)
#bmi = round(bmi , 2)
print(f"Your BMI is {bmi}")
print()

#                                  Tasks
# Write a python program to add two numbers
num_01 = float(input("Enter the first number:"))
num_02 = float(input("Enter the second number:"))
print(f"The sum is {num_01 + num_02}")

# Write a python program to find remainder when a number is divided by z.
print()
dividend = int(input("Enter the dividend:"))
divisor = int(input("Enter the divisor:"))

remainder = dividend % divisor
print(f"The remainder is {remainder} of {dividend} / {divisor}")


#Use comparison operator to find out whether ‘a’ given variable a is greater than
#‘b’ or not. Take a = 34 and b = 80
a = 34
b = 80
print(a>b)

# Write a python program to find an average of two numbers entered by the user
print("Average of two numbers")
first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

average = (first_num + second_num) / 2
print(f"The average of {first_num} and {second_num} is {average}")

# Write a python program to calculate the square of a number entered by the user.
print("Square of a number")
sq_num = int(input("Enter the square number:"))
square = sq_num * sq_num
print(f"The square of {sq_num} is {square}")

# outdoor management
print("Welcome to Tip Calculator")
bill = float(input("Enter the total bill in $:"))
tip = int(input("How much tip do you want to give $10,$12 and $15:"))
bill_distribution = int(input("How many people do you want to distribute the bill:"))

tip_amount = bill / (tip/100)
total_bill = bill + tip_amount
each_person = round(total_bill / bill_distribution , 1)
print(f"Each person should pay  +${each_person}")


