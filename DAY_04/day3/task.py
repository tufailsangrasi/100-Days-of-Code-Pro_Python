# control statement
# comparison operator > < >= <= ==
height = input("Enter the height")
if height < 180:
    print("You can allow to rollercoaster")
else:
    print("You can not allow to rollercoaster")

# module operator
numb_to_check = int(input("Enter the number"))
# if else
if numb_to_check % 2:
    print("Even")
else:
    print("Odd")

# Nested if else
if height > 120:
    print("You are allowed to rollercoaster")
    age = int(input("Enter the age"))
    # if inside if statement
    if age >= 18:
        print("You have to buy ticket")
    else:
        print("Not buy the ticket")
else:
    print("You are not allowed to rollercoaster")

# if / elif use for more than 2 condition WHat is intention level
age_of_person = int(input("Enter the age"))
if age_of_person > 18:
    print("You are eligible")
elif age_of_person < 18:
        print("You are not eligible")
else:
    print("You are too short")

height = int(input("Enter the height"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter the age"))
    if age <= 12:
        bill = 5 ;
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want your photo? Type y for Yes and n for No")
    if want_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
