from tkinter import *
RED2 = "#E83F25"
RED = "#A62C2C"
ORANGE = "#EA7300"
CREAM = "#D3CA79"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20,bg=CREAM)

title_label = Label(text="Password Manager", fg=RED, bg=CREAM, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200, bg=CREAM, highlightthickness=0)
tomato_img = PhotoImage(file="day29_password_manager/logo.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

window.mainloop()