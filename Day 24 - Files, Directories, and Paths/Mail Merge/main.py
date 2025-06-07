with open("./Input/Names/invited_names.txt", mode="r") as file: 
    invited_names = file.read()
    name_list = invited_names.split('\n')

with open("./Input/Letters/starting_letter.txt", mode="r") as file: 
    starting_letter = file.read()

for name in name_list:
    ready_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name.lower()}.txt", mode="w") as file: 
        file.write(ready_letter)