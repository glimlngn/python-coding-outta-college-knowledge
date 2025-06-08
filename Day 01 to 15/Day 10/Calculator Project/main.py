def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# from art import logo
# print(logo)

replay = 'n'
result = 0
while True:
    if replay == 'n':
        first_number = float(input("Input the first number: "))
    elif replay == 'y':
        first_number = result

    operator = input("Input the operator (+, -, *, /): ")
    second_number = float(input("Input the second number: "))
    result = operations[operator](first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")
    replay = input(f"Type 'y' to continue calculating with {result}, "
                   f"or type 'n' to start a new calculation: ").lower()

    if replay == 'n':
        print("\n" * 30)
    #     print(logo)