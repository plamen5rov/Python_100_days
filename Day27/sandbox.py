from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(800, 600)

#Label

my_label = Label(text="I am a Label", font=("Courier New", 24, "bold"),)
my_label.pack()

#Buton

def button_clicked():
    my_label["text"]=input.get()
    
    
my_button = Button(text="Click me!", font=("Courier New", 11, "normal"), command=button_clicked)
my_button.pack()


#Entry

input = Entry(width=22)
input.pack()







window.mainloop()