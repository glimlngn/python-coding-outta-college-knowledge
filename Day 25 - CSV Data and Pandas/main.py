import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

class Text(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def print_word(self, row):
        self.goto(row["x"].iloc[0], row["y"].iloc[0])
        self.write(row["state"].iloc[0], False, "center", ("Arial", 10, "bold"))
        self.goto(0, 0)

    def finish_game(self, score):
        self.write(f"Thanks for playing!\nScore: {score}/50", False, "center", ("Arial", 14, "bold"))

text = Text()

us_states = pd.read_csv("50_states.csv")

score = 0
correct_answers = []
game_is_on = True

while game_is_on:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?\nType '0' to finish playing").title()

    #check if the answer is one of the states
    is_state = us_states["state"].isin([answer]).any()

    if is_state and answer not in correct_answers:
        row = us_states[us_states["state"] == answer]
        correct_answers.append(answer)
        text.print_word(row)
        score += 1

    if answer == "0":
        text.finish_game(score)
        game_is_on = False

screen.exitonclick()