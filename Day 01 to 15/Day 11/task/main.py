import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def addCard(cards_player):
    """
    Adds a card to a player's deck. Returns updated deck and sum
    :param cards_player:
    :return updated cards of player:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    sum = 0
    new_card = random.choice(cards)
    cards_player.append(new_card)
    for i in cards_player:
        sum += i
    return cards_player

def sumCards(cards_player):
    """
    Adds up the cards in the player's deck
    :param cards_player:
    :return updated sum of cards:
    """
    sum = 0
    for i in cards_player:
        sum += i
    return sum

def aceChange(cards_player):
    """
    Changes the ace card from an '11' to a '1'
    :param cards_player:
    :return cards with updated ace:
    """
    cards_player[cards_player.index(11)] = 1
    return cards_player

cards_mine = []
cards_mine_sum = 0
cards_cpu = []
cards_cpu_sum = 0

play_again = input("Do you want to play a game of Blackjack (y/n)? ").lower()

while play_again == 'y':
    print(logo)
    cards_mine = addCard(cards_mine)
    cards_mine = addCard(cards_mine)
    cards_mine_sum = sumCards(cards_mine)

    print(f"    Your cards: {cards_mine}, current score: {cards_mine_sum}")

    cards_cpu = addCard(cards_cpu)
    cards_cpu = addCard(cards_cpu)
    cards_cpu_sum = sumCards(cards_cpu)

    print(f"    Computers first card: {cards_cpu[0]}")

    if cards_cpu_sum == 21:
        print(f"    Computer's hand: {cards_cpu}, score: {cards_cpu_sum}")
        print("CPU got Blackjack! You lose... 🚶‍")
    elif cards_mine_sum == 21:
        print("You got Blackjack! You win!! 🤩‍")
    else:
        get_another_card = 'y'
        while get_another_card == 'y' and cards_mine_sum < 21:
            get_another_card = input("Will you get another card (y/n)? ").lower()

            if get_another_card == 'y':
                cards_mine = addCard(cards_mine)
                cards_mine_sum = sumCards(cards_mine)

                if 11 in cards_mine and cards_mine_sum > 21:
                    cards_mine = aceChange(cards_mine)
                    cards_mine_sum = sumCards(cards_mine)
                print(f"    Your cards: {cards_mine}, current score: {cards_mine_sum}")
                print(f"    Computers first card: {cards_cpu[0]}")

        print(f"\n    ***\n    Your final hand: {cards_mine}, final score: {cards_mine_sum}")

        if cards_mine_sum > 21:
            cards_cpu_sum = sumCards(cards_cpu)
            print(f"    Computer's final hand: {cards_cpu}, final score: {cards_cpu_sum}\n    ***\n")
            print("You went over. You lose! 😤")
        elif cards_mine_sum == 21:
            print("You got Blackjack! You win!! 🤩‍")
        else:
            while cards_cpu_sum < 17:
                cards_cpu = addCard(cards_cpu)
                cards_cpu_sum = sumCards(cards_cpu)
            print(f"    Computer's final hand: {cards_cpu}, final score: {cards_cpu_sum}\n    ***\n")
            if cards_cpu_sum > 21:
                print("Opponent went over. You win! 😃")
            elif cards_cpu_sum == 21:
                print("CPU got Blackjack! You lose... 🚶‍")

            elif cards_mine_sum > cards_cpu_sum:
                print("You win! 😃")
            elif cards_mine_sum < cards_cpu_sum:
                print("You lose 😞")
            else:
                print("Draw 😑")

    play_again = input("Do you want to play again (y/n)? ").lower()
    if play_again == 'y':
        cards_mine = []
        cards_mine_sum = 0
        cards_cpu = []
        cards_cpu_sum = 0
        print("\n" * 30)

print("aw ok")