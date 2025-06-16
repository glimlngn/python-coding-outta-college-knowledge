from tkinter import * # type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        # Score
        sample_score = 0
        self.score_label = Label(text=f"Score: {sample_score}", fg="white", bg=THEME_COLOR, 
                            justify="center", font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column= 1)

        # Textbox
        sample_text = "Amazon acquired Twitch in August 2014 blah blah blah."
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text=sample_text, 
                            fill=THEME_COLOR, width=300, justify="center", font=("Arial", 16, "italic"))
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, command="")
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, command="")
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)