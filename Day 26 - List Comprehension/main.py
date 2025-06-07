import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

name = input("Enter a word: ")

name_letters = [letter for letter in name]
name_letters_nato = [nato_dict[letter.upper()] for letter in name_letters]
print(name_letters)
print(name_letters_nato)