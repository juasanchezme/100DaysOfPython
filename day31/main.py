from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=40, pady=10, bg=BACKGROUND_COLOR)



# card 
canvas = Canvas(width=800, height=500)
card_front = PhotoImage(file="day31/images/card_front.png")
card_back = PhotoImage(file="day31/images/card_back.png")
canvas_image = canvas.create_image(400, 250, image=card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
cross_image = PhotoImage(file="day31/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="day31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=1)


# Adding text to the canvas

data = pd.read_csv("day31/data/french_words.csv")

def select_random_word():
    random_row = data.iloc[random.randint(0, len(data)-1)]
    palabra_frances = random_row["French"]
    palabra_ingles = random_row["English"]
    return palabra_frances, palabra_ingles

# Inicializar con una palabra
current_fr, current_en = select_random_word()
text_fr = canvas.create_text(400, 150, text=current_fr, font=("Arial", 40, "italic"), fill="black")
text_en = canvas.create_text(400, 250, text=current_en, font=("Arial", 60, "bold"), fill="black")

def next_card():
    fr, en = select_random_word()
    canvas.itemconfig(text_fr, text=fr)
    canvas.itemconfig(text_en, text=en)

unknown_button.config(command=next_card)
known_button.config(command=next_card)

window.mainloop()