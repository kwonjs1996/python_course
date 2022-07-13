import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label


my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# Button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="Click")
new_button.grid(row=0, column=2)
# Entry

input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2, column=3)


window.mainloop()
