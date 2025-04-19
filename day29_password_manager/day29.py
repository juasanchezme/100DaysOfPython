from tkinter import *
from tkinter import messagebox

RED2 = "#E83F25"
RED = "#A62C2C"
ORANGE = "#EA7300"
CREAM = "#D3CA79"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass 


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_correct = messagebox.askokcancel(title=website, message=f"You entered: \n website: {website}\n email: {email} \n password: {password} \n Is it correct?")
    
    if is_correct:
        with open("day29_password_manager/data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

# 🎨 
PRIMARY_BG = "#1F2937"    # Fondo oscuro
PRIMARY_TEXT = "#FFFFFF"  # Texto principal (blanco)
INPUT_BG = "#E5E7EB"      # Campos de entrada (gris claro)
INPUT_FG = "#000000"      # Texto en campos
ACCENT_COLOR = "#3B82F6"  # Botones o acciones (azul)
ALERT_COLOR = "#EF4444"   # Para botón "Add"
FONT_NAME = "Courier"



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=PRIMARY_BG)

# Título
title_label = Label(
    text="Password Manager", 
    fg=ACCENT_COLOR, 
    bg=PRIMARY_BG, 
    font=(FONT_NAME, 32, "bold")
)
title_label.grid(column=1, row=0, pady=(0, 20))

# Logo
canvas = Canvas(width=200, height=200, bg=PRIMARY_BG, highlightthickness=0)
logo_img = PhotoImage(file="day29_password_manager/logo_candado.png")  # Ajusta la ruta si es necesario
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1, pady=(0, 20))

# Labels
Label(text="Website:", fg=PRIMARY_TEXT, bg=PRIMARY_BG, font=(FONT_NAME, 14)).grid(column=0, row=2)
Label(text="Email/Username:", fg=PRIMARY_TEXT, bg=PRIMARY_BG, font=(FONT_NAME, 14)).grid(column=0, row=3)
Label(text="Password:", fg=PRIMARY_TEXT, bg=PRIMARY_BG, font=(FONT_NAME, 14)).grid(column=0, row=4)

# Entries
website_entry = Entry(width=20, bg=INPUT_BG, fg=INPUT_FG, font=(FONT_NAME, 12))
website_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky="ew")
website_entry.focus()

email_entry = Entry(width=20, bg=INPUT_BG, fg=INPUT_FG, font=(FONT_NAME, 12))
email_entry.insert(0, "")
email_entry.grid(column=1, row=3, columnspan=2, pady=5,sticky="ew")

password_entry = Entry(width=20, bg=INPUT_BG, fg=INPUT_FG, font=(FONT_NAME, 12))
password_entry.grid(column=1, row=4, pady=5,sticky="ew")

# Botón generar contraseña
password_button = Button(
    text="Generate", 
    command=generate_password,
    bg=ACCENT_COLOR, 
    fg=PRIMARY_TEXT, 
    font=(FONT_NAME, 10), 
    width=20
)
password_button.grid(column=2, row=4, padx=5)

# Botón agregar
add_button = Button(
    text="Add", 
    command=save,
    bg=ALERT_COLOR, 
    fg=PRIMARY_TEXT, 
    font=(FONT_NAME, 12, "bold"),
    width=20
)
add_button.grid(column=1, row=5, columnspan=2, pady=20, sticky="ew")

window.mainloop()
