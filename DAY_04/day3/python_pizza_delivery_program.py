print("Welcome to python Pizza Deliveries")
size = input("What size pizza do you want? S , M or L")
pepporoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
bill = 0

if size == "S":
    bill = bill + 15
    if pepporoni == "Y":
        bill = bill + 2
        if extra_cheese == "Y":
            bill = bill + 1
            print("Your bill is", bill)
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
else:
    print("You type the wrong size")



# logical operator and or not!
# ASCII code