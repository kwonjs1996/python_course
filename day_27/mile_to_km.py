import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

def convert():
    mile = user_input.get()
    km = round(float(mile) * 1.609, 2)
    label_result.config(text=km)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)
label_is_equal = tkinter.Label(text="is equal to")
label_is_equal.grid(column=0, row=1)
label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)
label_result = tkinter.Label(text="")
label_result.grid(column=1, row=1)
button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
user_input = tkinter.Entry(width=15)
user_input.grid(row=0, column=1)




window.mainloop()
