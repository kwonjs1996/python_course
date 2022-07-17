import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
# df = pandas.DataFrame(data)
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    # r_word = random.choice(to_learn["French"])
    # card_canvas.itemconfig(word_card, text=f"{r_word}")
    # global current_word = random.choice(to_learn)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(front_img, image=card_img)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(word_card, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(2000, flip_card)



def flip_card():
    card_canvas.itemconfig(front_img, image=card_back_img)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(word_card, text=f"{current_card['English']}", fill="white")


window = tkinter.Tk()
window.title("Flash")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(2000, flip_card)

card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_img = tkinter.PhotoImage(file="images/card_front.png")
right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

card_canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = card_canvas.create_image(400, 263, image=card_img)
card_canvas.grid(row=0, column=0, columnspan=2)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_card = card_canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))

right_button = tkinter.Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()