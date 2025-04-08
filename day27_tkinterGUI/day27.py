import tkinter

window = tkinter.Tk()
window.title("tkinter program")
window.minsize(width=500, height=300)

# Creating labels

my_label = tkinter.Label(text="a label", font=("Arial", 24, "bold"))

#place the label in the center of the screen
my_label.pack()

# place the label at the top
#my_label.pack(side="top")








window.mainloop()