rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = [rock, paper, scissors]
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper "
                    "or 2 for Scissors. "))
comp = random.randint(0, 2)

print(choices[you])
print("Computer chose: ")
print(choices[comp])

if you == comp:
    print("It's a draw!")
elif ((you + 2) % 3) == comp:
    print("You win!")
else:
    print("You lose!")
