import tkinter

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flash")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_img = tkinter.PhotoImage(file="images/card_front.png")
right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

card_canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(400, 263, image=card_img)
card_canvas.grid(row=0, column=0, columnspan=2)
card_canvas.create_text(400, 150, text="Franch", font=("Ariel", 40, "italic"))
card_canvas.create_text(400, 300, text="word", font=("Ariel", 60, "bold"))

right_button = tkinter.Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)


window.mainloop()