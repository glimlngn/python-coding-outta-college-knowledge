import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ")

name_letters = [letter for letter in name]
name_letters_nato = [nato_dict[letter.upper()] for letter in name_letters]
print(name_letters)
print(name_letters_nato)