import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = tkinter.Label(text="Wdbsite: ")
web_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)

site_input = tkinter.Entry(width=35)
site_input.grid(row=1, column=1, columnspan=2)

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add",width=36)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()