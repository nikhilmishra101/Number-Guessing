import random
from replit import clear
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess_number,user_number,attempts):
  if guess_number > user_number:
    print("Too Low")
    attempts -= 1
  elif guess_number < user_number:
    print("Too High")
    attempts -= 1
  else:
    print(f"Yeah you got it right,The Number is {guess_number},YOU WON.")
  return attempts
def set_difficulty():
  level = input("Choose a difficulty.Type 'easy' or 'hard': ")
  if level.lower() == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")

  computer_guess = random.randint(1,101)
  print(computer_guess)
  turns = set_difficulty()
  user_guess = 0
  while user_guess != computer_guess:
    print(f"You have {turns} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    turns = check_answer(computer_guess,user_guess,turns)
    if turns == 0:
      print("You ran out of lives,You lose")
      return
    elif user_guess != computer_guess:
      print("Guess Again.")

game()

play_again = input("You want to play again.Type 'y' for yes and 'n' for no")

if play_again.lower() == "y":
  clear()
  game()