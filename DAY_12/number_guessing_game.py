from random import randint
#5 Const
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#3Function to check users guess against actual answer
def check_number(user_input , actual_answer , turns):
    """Checks answer against guess , return the number of turns remaining"""
    if user_input > actual_answer:
        print("Too High")
        return turns - 1
    elif user_input < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

#4 Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty (easy or hard:")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    #1Choose a random number between 1 to 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)

    #6
    turns = set_difficulty()
    guess = 0
    #8
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    #2let the user guess a number
        guess = int(input("Make a guess: "))
    #7
        turns = check_number(guess, answer , turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()


