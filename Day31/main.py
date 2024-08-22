"""Flash Cards App For Studying French Language"""

from tkinter import *

#Globals
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Images
# card_back = PhotoImage(file="/images/card_back.png")
# card_front = PhotoImage(file="/images/card_front.png")
# right_sign = PhotoImage(file="/images/right.png")
# wrong_sign = PhotoImage(file="/images/wrong.png")

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front )
canvas.grid(row=0, column=0, columnspan=2)




#Buttons
# card_back_button = Button(image=card_back, highlightthickness=0)
# card_front_button = Button(image=card_front, highlightthickness=0)
# right_sign_button = Button(image=right_sign, highlightthickness=0)
# wrong_sign_button = Button(image=wrong_sign, highlightthickness=0)






window.mainloop()
