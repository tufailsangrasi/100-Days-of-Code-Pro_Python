from random import randint

# Easy and difficult level turns
EASY_LEVEL_TURNS = 10
DIFFICULT_LEVEL_TURNS = 5


# Function to check user input
def check_number(user_input , actual_answer , turns):
  """Checks answer against guess , return the number of turns remaining"""
  if user_input > actual_answer:
    print("Too High")
    return turns - 1
  elif user_input < actual_answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"Congrats you guess the actual number ${actual_answer}")

# Setting the level of difficulty
def set_difficulty():
  level = input("Choose a difficulty (easy & hard)")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return DIFFICULT_LEVEL_TURNS
  
def game():  
    # Choose a random number between 1 to 100
    print("Welcome to Number guessing game!")
    print("Guess a number from 1 to 100")
    answer = randint(1,100)

# Let the user guess a number
    user_guess = int(input("Make a guess: "))
  
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    turns = check_number(user_guess , answer , turns)
    if turns == 0:
      print("You have run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
