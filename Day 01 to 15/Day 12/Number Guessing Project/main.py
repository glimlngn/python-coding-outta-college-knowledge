import random
from art import logo

NUMBER = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")
difficulty = input("Easy or Hard mode? (type 'easy' or 'hard') ").lower()
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("WTF that wasn't even in the choices! >:(")
    print("Bitch, ", end='')
    attempts = 1

def number_guess():
    global attempts
    attempts -= 1
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please input a number.")
        attempts += 1
        return 0

    if guess == NUMBER:
        return 1
    elif guess < NUMBER:
        print("Too low.")
        return 0
    elif guess > NUMBER:
        print("Too high.")
        return 0
    # 0 for "not equal", 1 for "equal"

game_won = 0
while attempts > 0 and game_won == 0:
    print(f"You have {attempts} attempt/s remaining to guess the number.")
    game_won = number_guess()

print()
if game_won == 1:
    print(f"You win!!! The number was {NUMBER}")
elif game_won == 0:
    print(f"You lose... The number was {NUMBER}.")
print("Rerun the code to play again.")