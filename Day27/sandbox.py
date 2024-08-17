import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(800, 600)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Courier New", 24, "bold"),)
my_label.pack()










window.mainloop()