# For While if/else List Range Module Strings
from mimetypes import guess_type

# Step # 01
word_list = ["aardvark" , "baboon" , "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign their answer to a variable called chosen_word.Then Print it
import random
chosen_word = random.choice(word_list)
print(chosen_word)
# Step-02
placeholder = ""
word_list = len(chosen_word)
for position in range(word_list):
    placeholder += "_"
#print(placeholder) for testing


# TODO-2 - Ask the user to guess a letter and answer to a variable called guess.Make guess lowercase
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)


    # TODO-3 - Check if the letter the user guessed (guess) is one of the letter in the chosen_word.Print "Right" if it is "Wrong" if its not.
    # Step#02
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
# Step_01   print(letter)
#    if letter == guess:
#        print("Right")
#    else:
#       print("Wrong")

# step-02

# Create an empty string called placeholder.

# for each letter in the chosen_word add into placeholder.
# so if the chosen_word was "apple" placeholder should be -----
# with 5 " " representing each letter to guess


# print out the hint.

if "_" not in display:
    game_over = True
    print(display)