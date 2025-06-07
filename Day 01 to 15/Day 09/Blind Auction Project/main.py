from art import logo

print(logo)
any_other_bidders = True
bids = {}
while any_other_bidders:
    name = input("What is your name? ")
    price = int(input("What is your bid? PHP "))
    bids[name] = price
    decision = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if decision == 'no':
        any_other_bidders = False
    print("\n" * 20)
max_price = 0
max_name = ""
for name in bids:
    if bids[name] > max_price:
        max_price = bids[name]
        max_name = name

print(bids)
print(f"The winner is {max_name} with a bid of PHP {bids[max_name]}")