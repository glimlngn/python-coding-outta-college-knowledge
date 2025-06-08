import random
import art
from game_data import data

def clear_console():
    """Clears the console by printing a lotta line breaks."""
    print("\n" * 11)

def print_details(account):
    """Prints the details of the account: name, description, and country."""
    print(f"{account["name"]}, a {account["description"]} from {account["country"]}.")

def compare_followers(acc_a, acc_b):
    """
    Returns 'a' if followers of a > followers of b,
    returns 'b' if followers of a < followers of b
    """
    if acc_a["follower_count"] > acc_b["follower_count"]:
        return 'a'
    elif acc_a["follower_count"] < acc_b["follower_count"]:
        return 'b'
    else:
        return 'both'

def is_guess_correct(guess, correct_ans):
    """
    Returns 'False' if user guesses wrong to stop the game,
    returns 'True' and adds one (1) point to 'score' if user guesses correct
    """
    global score
    if guess == correct_ans or correct_ans == 'both':
        score += 1
        clear_console()
        print(art.logo)
        print('\033[32m' + f"You're right! Current score: {score}." + '\033[0m')
        if correct_ans == 'both':
            print("(Actually, they both have the same follower count...)")
        return True
    else:
        clear_console()
        print(art.logo)
        print('\033[31m' + "Sorry, that's wrong. " + '\033[0m' + f"Final score: {score}." + "\n" * 9)
        return False

print(art.logo + "\n")
score = 0

account_b = random.choice(data)
continue_game = True

while continue_game:
    account_a = account_b
    account_b = random.choice(data)
    print()
    print(f"Compare A: ", end='')
    print_details(account_a)
    print(art.vs)
    print(f"Against B: ", end='')
    print_details(account_b)

    correct_answer = compare_followers(account_a, account_b)
    # print(f"Psst, it's '{correct_answer.upper()}', A: {account_a["follower_count"]} and B: {account_b["follower_count"]}")
    print()
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print()
    continue_game = is_guess_correct(user_guess, correct_answer)
