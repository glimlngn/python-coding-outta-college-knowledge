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
        self.score_label = Label(text=f"Score: {sample_score}/{self.quiz.question_count}", fg="white", bg=THEME_COLOR, 
                            justify="center", font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column= 1)

        # Textbox
        sample_text = "Good Luck!"
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text=sample_text, 
                            fill=THEME_COLOR, width=300, justify="center", font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, command=lambda:self.get_next_question("True"))
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, command=lambda:self.get_next_question("False"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        self.window.mainloop()

    def get_next_question(self, *answer):
        if answer != ():
            user_answer = answer[0]
            is_answer_correct = self.quiz.check_answer(user_answer)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

            if is_answer_correct:
                self.canvas.config(bg="green")
                self.canvas.itemconfig(self.question_text, fill="white")
            else:
                self.canvas.config(bg="red")
                self.canvas.itemconfig(self.question_text, fill="white")
            self.window.after(1500, lambda: [self.canvas.config(bg="white"), \
                                             self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)])
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_count}")
        
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.window.after(1500, lambda: [self.true_button.config(state="active"), 
                                             self.false_button.config(state="active"), 
                                             self.canvas.itemconfig(self.question_text, text=q_text)])
        else:
            finished_quiz_text = f"You've completed the quiz!\nYour final score is: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, 
                                   text=finished_quiz_text)
            print("\n", finished_quiz_text)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")