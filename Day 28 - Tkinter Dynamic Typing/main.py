from tkinter import * # type: ignore

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = int(count/60)
    count_sec = (count%60)
    global timer, reps

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_label.config(text="✔" * int(reps/2))

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start_button.config(command="")
    global reps
    reps += 1
    # long break every 8th rep
    if reps % 8 == 0:
        title_label.config(text="Break!", fg=RED)
        min = LONG_BREAK_MIN
    # short break every even rep (except 8th)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        min = SHORT_BREAK_MIN
    # work every odd rep
    else:
        title_label.config(text="Work", fg=GREEN)
        min = WORK_MIN
    count_down(60 * min)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="25:00")
    start_button.config(command=start_timer)
    check_label.config(text="")
    reps = 0

# ---------------------------- TODO: TIMER PAUSE (Extra) ------------------------------- # 



# ---------------------------- TODO: Windows Notification (Extra) ------------------------------- # 



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# Tomato and Timer
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="25:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Buttons
# calls start_timer() when pressed
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

# calls reset_timer() when pressed
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

#Labels
check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16))
check_label.grid(row=3, column=1)

window.mainloop()