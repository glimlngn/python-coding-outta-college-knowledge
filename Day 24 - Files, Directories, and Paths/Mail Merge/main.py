#TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend" with filenames "letter_for_[name]".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as file: 
    invited_names = file.read()
    name_list = invited_names.split('\n')

with open("./Input/Letters/starting_letter.txt", mode="r") as file: 
    starting_letter = file.read()

for name in name_list:
    ready_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name.lower()}.txt", mode="w") as file: 
        file.write(ready_letter)