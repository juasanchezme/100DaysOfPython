from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)


# card back
canvas = Canvas(width=900, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="./day31/images/card_back.png")  
canvas.create_image(450, 313, image=logo_img)
canvas.grid(column=1, row=1, padx=(50,50),pady=(0,50))

# card front
card_front = PhotoImage(file="day31/images/card_front.png")
canvas.create_image(450, 313, image=card_front)
canvas.grid(column=1, row=1, padx=(50,50),pady=(0,50))




window.mainloop()