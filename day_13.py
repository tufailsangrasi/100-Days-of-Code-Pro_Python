#Describe the Problem
#1.What is for loop doing
#2.When the function meant to print ("You got it")
#3.What are your assumption for the value of i
def function():
  for i in range(1,20):
    if i==20:
      print("You got it")

# Reproduce the Bug Himself and explain like you are a debugger

# Debugging the odd and even problem
def odd_or_even(number):
    if number % 2 == 0:    #<if number % 2 = 0>
        return "This is an even number."
    else:
        return "This is an odd number."

# Debugging Leap Year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  #<if year % 4000 == 0:>
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:    #<and instead of or>
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)                        #<number instead of [number]>
