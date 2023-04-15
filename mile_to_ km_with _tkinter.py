from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label

my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=0)

second_label = Label(text="is equal to", font=("Arial", 24, "bold"))
second_label.grid(column=0, row=1)

third_label = Label(text="Km", font=("Arial", 24, "bold"))
third_label.grid(column=2, row=1)

km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(column=1, row=1)

#Button

miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)

# convert to km from miles

def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_label.config(text=km)



button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()
