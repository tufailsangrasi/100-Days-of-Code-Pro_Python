import random
# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

#
Scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for rock , 1 for paper or 2 for Scissors"))
# o , 1 , 2
game_images = ['rock', 'paper', 'scissors']
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.ranint(0 , 2)
print(f"Computer choice: {computer_choice}")
print(game_images[computer_choice])
# Test your code at every time it good practice


if user_choice >=  3 or user_choice <=0:
    print("You choose invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == 1 and user_choice == 0:
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")
