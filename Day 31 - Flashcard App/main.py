from tkinter import * # type: ignore
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"    # TODO: Add more languages to learn i.e. Filipino
CODEC = "cp1252"

# ---------------------------- INITIALIZE DATA ------------------------------- #

with open(f"data/{LANGUAGE.lower()}_words.csv", "r") as file:
    df = pd.read_csv(file)

for index, row in df.iterrows():
    # Fixes formatting of special characters    
    row[LANGUAGE] = row[LANGUAGE].upper().encode(CODEC).decode().lower()

try:
    with open(f"data/{LANGUAGE.lower()}_words_to_learn.csv", "r") as file:
        df_to_learn = pd.read_csv(file)
except FileNotFoundError:
    print(f"'{LANGUAGE.lower()}_words_to_learn.csv' not found. Creating file...")
    df.to_csv(f"data/{LANGUAGE.lower()}_words_to_learn.csv", index=False)
    with open(f"data/{LANGUAGE.lower()}_words_to_learn.csv", "r") as file:
        df_to_learn = pd.read_csv(file)

for index, row in df_to_learn.iterrows():
    # Fixes formatting of special characters [again]    
    row[LANGUAGE] = row[LANGUAGE].upper().encode(CODEC).decode().lower()

# Converts df to list of dicts [{french_word1: english_word1}, {french_word2: english_word2}, ...]
words_dict = df_to_learn.to_dict(orient='records')    # Working data are from the 'words to learn' file

current_card = {}

# ---------------------------- TRACK PROGRESS ------------------------------- #

def remove_card():    # TODO: Keep track of number of known words in GUI
    global current_card
    words_dict.remove(current_card)
    print(current_card)
    current_card_series = pd.DataFrame.from_dict(current_card, orient="index").transpose().iloc[0]
    print(df_to_learn)
    df_to_learn.drop(df_to_learn.index[df_to_learn[LANGUAGE] == current_card_series[LANGUAGE]], inplace=True)
    df_to_learn.reset_index(drop=True, inplace=True)
    df_to_learn.to_csv(f"data/{LANGUAGE.lower()}_words_to_learn.csv", index=False)

# ---------------------------- RESET PROGRESS ------------------------------- #
# TODO: Add feature to reset progress


# ---------------------------- NEXT FLASHCARD ------------------------------- #

def next_card(knows_word):
    global current_card    # Weird, i should be able to also put 'global timer' here

    if knows_word:
        remove_card()

    current_card = r.choice(words_dict)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text=LANGUAGE, fill='black')
    canvas.itemconfig(card_text, text=current_card[LANGUAGE], fill='black')

    def count_down(count):    # TODO: Add countdown timer to GUI
        global timer
        window.after_cancel(timer)
        if count > 0:
            print(count)
            timer = window.after(1000, count_down, count-1)
        else: 
            print("FLIP!")
            flip_card()

    count_down(5)    # X seconds countdown before flipping the card

# ---------------------------- FLIP FLASHCARD ------------------------------- #

def flip_card():
    global current_card
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_text, text=current_card["English"], fill='white')

# ---------------------------- GUI SETUP ------------------------------- #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(0, func=lambda *args: None)    # Initialize timer

# Image and Texts
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text=f"{LANGUAGE}-to-English Flashcard App", font=("Arial", 32, "italic"))
card_text = canvas.create_text(400, 263, text="Ready?", font=("Arial", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
def is_ready(is_ready):
    if is_ready:
        right_button.config(command=lambda: next_card(knows_word=True))
        wrong_button.config(command=lambda: next_card(knows_word=False))
        next_card(knows_word=False)
    else:
        canvas.itemconfig(card_text, text="Wdym?? U can do it!")
    
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=lambda: is_ready(is_ready=True))
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=lambda: is_ready(is_ready=False))
wrong_button.grid(row=1, column=0)

window.mainloop()