# Function with Output

def my_function(num):
  square = num * num
  return square

print(my_function(5))

def add_two_num(num1 , num2):
  return num1 + num2

def subtrack_two_num(num1 , num2):
    return num1 - num2

def multi_two_num(num1 , num2):
    return num1 * num2

def div_two_num(num1 , num2):
   if num2 == 0:
      return "Undefined"
   else:
      return num1 / num2
   
num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))
addition = add_two_num(num1 , num2)
substraction = subtrack_two_num(num1 , num2)
multiplication = multi_two_num(num1 , num2)
division = div_two_num(num1 , num2)

print(f"The sum of {num1} +  {num2} =" , addition)
print(f"The subtraction of {num1} -  {num2} =" , substraction)
print(f"The multiplication of {num1} *  {num2} =" , multiplication)
print(f"The division of {num1} /  {num2} =" , division)

# Recursive has two condition base and recursive
