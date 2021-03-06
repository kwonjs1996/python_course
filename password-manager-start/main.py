import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, "end")
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    site = site_input.get()
    user_email = email_input.get()
    password = password_input.get()
    new_data = {
        site: {
            "email": user_email,
            "password": password
        }
    }

    if site == "" and password == "":
        messagebox.showinfo(title="Website and Password empty", message="Please enter the Website and Password")

    elif site == "":
        messagebox.showinfo(title="Website empty", message="Please enter the Website!")
    elif password == "":
        messagebox.showinfo(title="Password empty", message="Please enter the Password!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {user_email} "
                                                           f"\nPassword: {password} \nIs it ok to save")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                site_input.delete(0, "end")
                password_input.delete(0, "end")
                site_input.focus()


def search_data():
    account = site_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="Please Add Account First")
    else:
        if account in data:
            messagebox.showinfo(title="Account Info", message=f"Website: {account}\nE-mail: "
                                                          f"{data[account]['email']}\nPassword: {data[account]['password']}")
        else:
            messagebox.showinfo(title="Account Not Found", message="No account that website,\nPlease check Website")
            site_input.delete(0,"end")


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

site_input = tkinter.Entry(width=21)
site_input.grid(row=1, column=1)
site_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "abc@email.com")

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate Password", command=password_generate)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=13, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()
