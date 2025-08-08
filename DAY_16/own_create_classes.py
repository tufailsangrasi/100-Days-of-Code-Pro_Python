# Creating own Classes in Python
# PascalCase is used for naming the class
# Intendation error comes you used pass keyword for this in Both Classes and Functions

class User:
    # Initilize the Attributes
    def __init__(self , seat):
        print("Always print when new object is created")
        self.seat = seat
        self.username = 'Tufail'
        self.followers = 0
        self.following = 0

    def follow(self , user):
        user.followers += 1
        self.following += 1


    # Adding method to User class
    # When function is attached to a object it called Method


# Create the Object of class
user_01 = User(5)
#print(user_01.id)
# It will give the error
user_02 = User(5)

user_01.follow(user_02)
print(user_01.followers)
print(user_01.following)