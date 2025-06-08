MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def show_report():
    """
    Prints report from global variable 'resources'
    """
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def check_resources(coff):
    """
    Checks if coffee machine has enough resources to make choice of coffee,
    cancels transaction if otherwise.

    Returns: boolean of whether resources are sufficient
    """
    coffee_ingredients = MENU[coff]["ingredients"]
    resources_enough = True

    for ing in coffee_ingredients:
        if resources[ing] < coffee_ingredients[ing]:
            print(f"Sorry, there is not enough {ing}.")
            resources_enough = False

    return resources_enough

def count_coins():
    """
    Counts how many coins the user has and calculates total money.

    Returns: Total user money
    """
    coin_multiplier = {
        "quarters": 0.01,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.25,
    }
    total = 0
    print("Please insert coins.")
    for coin in coin_multiplier:
        total += float(input(f"How many {coin}? "))*coin_multiplier[coin]
    total = round(total, 2)
    print(f"Your coins amount to ${total}.")
    return total

def make_coffee(coff, res, coff_cost):
    coff_ingredients = MENU[coff]["ingredients"]
    for ing in coff_ingredients:
        res[ing] -= coff_ingredients[ing]
    res["money"] = round(res["money"] + coff_cost, 2)
    return res

def main():
    try:
        global MENU
        global resources
        print("[Admin commands: report, refill, off]")
        print("Espresso\t\t$1.50\n"
              "Latte\t\t\t$2.50\n"
              "Cappuccino\t\t$3.00\n")
        coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

        while coffee != 'off':
            user_money = 0
            # print report
            if coffee == 'report':
                show_report()

            elif coffee == 'refill':
                resources["water"] = 300
                resources["milk"] = 200
                resources["coffee"] = 100
                print("Coffee machine refilled!")

            # Check if there's enough resources to make coffee.
            elif check_resources(coffee):
                # User inserts coins.
                user_money = count_coins()
                coffee_cost = MENU[coffee]["cost"]

                # Check if coins are enough, otherwise refund transaction.
                # Give change as needed.
                if user_money > coffee_cost:
                    change = round(user_money - coffee_cost, 2)
                    resources = make_coffee(coffee, resources, coffee_cost)
                    if user_money != 0:
                        print(f"Here is ${change} in change.")
                    print(f"Here is your {coffee} bby ☕ Enjoy! 😘")

                else:
                    print("Ya BROKE! Money refunded.")

            print()
            coffee = input("What would you like? (espresso/latte/cappuccino): ")

        print("Goodbye World! :)")
    except (ValueError, KeyError):
        print('\033[31m' + "Input invalid. Cancelling transaction." + '\033[0m')
        print()
        main()

main()