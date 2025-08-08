# Global Variable
enemies = 1

def increase_enemies(enemy):
    # Local Variable just have scope within function
    # If you want to modify the global variable you have to Do like this way
    # In python modifying global var is confusing to avoid used return statement
    global enemies
    enemies = 2
    print(f"Enemies inside the function: {enemies}")
    return enemies + 1

increase_enemies(enemies)
print(f"Enemies outside the function: {enemies}")



def is_prime_num(num):
    if num != 2 and num % 2 == 0:
        return False
    else:
        return True

number = int(input("Enter a number: "))
print(is_prime_num(number))

# Global Constant

PI = 3.14
GOOGLE_URL = "https://www.google.com/search?q="

def my_fun():
    print(GOOGLE_URL)


# Rem there is no block scope in python.if else while for code block is the same
def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()