from tkinter import * # type: ignore
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
CODEC = "cp1252"

with open("data/french_words.csv") as file:
    df = pd.read_csv(file)

for index, row in df.iterrows():
    # Fixes formatting of special characters    
    row[LANGUAGE] = row[LANGUAGE].upper().encode(CODEC).decode().lower()
    
# Converts df to list of dicts [{french_word1: english_word1}, {french_word2: english_word2}, ...]
words_dict = df.to_dict(orient='records')    

# ---------------------------- SHOW FLASHCARDS ------------------------------- #

def show_flashcard():
    wrong_button.config(command=show_flashcard)
    card = r.choice(words_dict)
    canvas.itemconfig(card_title, text=LANGUAGE)
    canvas.itemconfig(card_text, text=card[LANGUAGE])

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image and Texts
card_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text=f"{LANGUAGE}-to-English Flashcard App", font=("Arial", 32, "italic"))
card_text = canvas.create_text(400, 263, text="Ready?", font=("Arial", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=show_flashcard)
right_button.grid(row=1, column=1)

def not_ready_gag():
    canvas.itemconfig(card_text, text="Wdym?? U can do it!")

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=not_ready_gag)
wrong_button.grid(row=1, column=0)

window.mainloop()