print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

game_over = False

direction = input("Where do you want to go, left or right? (L or R) ")
if direction != 'L':
    game_over = True
    print("By going right [or by choosing the wrong input] You fell into a hole... Game Over!")

if game_over is False:
    swim = input("After going left, you come across a river with a school of salmon "
             "swimming by. Do you swim now or wait for the salmon to pass-by? (Swim or Wait) ")
    if swim != 'Wait':
        game_over = True
        print("After looking closely, you realize that they not salmon--they were piranhas!"
              "They didn't find you in good company. You got eaten... Game Over!")

if game_over is False:
    doors = input("You find three doors (Red, Yellow, Blue) one of which has the "
                      "treasure inside. Which door will you pick?\n ")
    if doors == 'Red':
        print("You got burned by fire... Game Over!")
    elif doors == 'Yellow':
        print("You found the treasure 🌟 You Win!")
    elif doors == 'Blue':
        print("You got eaten by beasts... Game Over!")
    else:
        print(f"You chose the '{doors}' door, which doesn't exist. "
              f"Pretentiously, you continue moving forward until you hit your head"
              f"on a brick wall... Game Over!")