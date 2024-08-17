from tkinter import *

window = Tk()
window.title("Miles t0 Km Converter")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

def calculate():
    miles = int(entry.get())
    km = round(miles *  1.609)
    result_label.config(text=km)

entry = Entry(width=10)
entry.grid(column=1, row=3)

miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=3)

equal_label = Label(text="is equal to ", font=("Arial", 14, "bold"))
equal_label.grid(column=3, row=3)

result_label = Label(text="0", font=("Arial", 14, "bold"))
result_label.grid(column=4, row=3)

km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=5, row=3)

button = Button(text="Calculate", font=("Arial", 14, "bold"), command=calculate)
button.grid(column=3, row=5)








window.mainloop()