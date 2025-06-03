from tkinter import * # type: ignore
from win10toast import ToastNotifier

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
pause_switch = True    # changes the button between 'Pause' and 'Resume'

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer, reps, time_left 
    count_min = int(count/60)
    count_sec = (count%60)
    time_left = count

    # formatting time
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(10, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:    # adds check everytime 'Work' is finished
            check_label.config(text=check_label.cget("text") + "✔")
        if reps % 16 == 0:    # newline after every 2 long breaks
            check_label.config(text=check_label.cget("text") + "\n")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    pause_button.config(command=pause_timer)
    start_button.config(command="")
    global reps
    reps += 1
    # long break every 8th rep
    if reps % 8 == 0:
        title_label.config(text="Breaaak", fg=RED)
        notify("Long Break Time! (20 minutes)")
        min = LONG_BREAK_MIN
    # short break every even rep (except 8th)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        notify("Break Time! (5 minutes)")
        min = SHORT_BREAK_MIN
    # work every odd rep
    else:
        title_label.config(text="Work", fg=GREEN)
        notify("Work Time! (25 minutes)")
        min = WORK_MIN
    count_down(60 * min)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer, reps, pause_switch
    pause_switch = True
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    pause_label.grid_forget()
    title_label.grid(row=0, column=1)
    canvas.itemconfig(timer_text, text="25:00")
    start_button.config(command=start_timer)
    pause_button.config(command="")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER PAUSE (Extra) ------------------------------- # 

def pause_timer():
    global timer, pause_switch
    if pause_switch == True:
        window.after_cancel(timer)   # Cancels timer
        pause_button.config(text="Resume")    # Change title to 'Pause'
        title_label.grid_forget()
        pause_label.grid(row=0, column=1)
    else: 
        timer = window.after(1, count_down, time_left-1)    # Resumes timer
        pause_button.config(text="Pause")    # Revert to last shown title
        pause_label.grid_forget()
        title_label.grid(row=0, column=1)

    pause_switch = not pause_switch

# ---------------------------- Windows Notification (Extra) ------------------------------- # 

notif = ToastNotifier()
def notify(message):
    notif.show_toast("Pomodoro Timer", message, threaded=True)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=0, height=550)

# Labels
title_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

pause_label = Label(text="Paused", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=RED)
pause_label.grid(row=0, column=1)
pause_label.grid_forget()

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16))
check_label.grid(row=4, column=1)

# Tomato Image and Timer
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="25:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start", command=start_timer, width=6)
start_button.grid(row=3, column=0)

pause_button = Button(text="Pause", width=6)
pause_button.grid(row=2, column=2)

reset_button = Button(text="Reset", command=reset_timer, width=6)
reset_button.grid(row=3, column=2)


window.mainloop()