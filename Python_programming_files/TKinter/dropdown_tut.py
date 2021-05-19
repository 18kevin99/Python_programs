from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.title("DROPDOWN MENUES")
root.geometry("400x400")

def show():
    myLabel = Label(root, text = clicked.get()).pack()


options = [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
    ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root , clicked, *options)
drop.pack()

myButton = Button(root, text = "Show selection", command = show).pack()

root.mainloop()
