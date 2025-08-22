# Hangman game
import random

word_list = ["python", "javascript", "java"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_list = len(chosen_word)
for position in range(word_list):
    placeholder += "_"

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    print(display)
    
    if "_" not in display:
        game_over = True
        print("Winner!")
