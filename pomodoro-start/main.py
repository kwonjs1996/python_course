import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
rep = 0
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    rep = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep % 2 == 1:
        title_label.config(text="Work", foreground=GREEN)
        count_down(work_sec)
    elif rep % 2 == 0:
        title_label.config(text="Short Break", foreground=PINK)
        count_down(short_break_sec)
        if rep % 8 == 0:
            title_label.config(text="Long Break", foreground=RED)
            count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.trunc(count / 60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    if 10 > int(sec) > 0:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
        marks = ""
        work_session = math.floor(rep / 2)
        for _ in range(work_session):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"))
title_label.config(bg=YELLOW, foreground=GREEN)
title_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tkinter.Label(text="")
check_label.config(bg=YELLOW, foreground=GREEN)
check_label.grid(row=3, column=1)




window.mainloop()

