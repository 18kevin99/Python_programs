from tkinter import *

def win():
    top = Toplevel()
    top.title("level1")
    lbl = Label(top, text = "does this print").pack()

root = Tk()
root.title("KEvin_eXp")
btn1 = Button(root, text= "experiment", command = win).pack()


top = Toplevel()
top.title("level1")
lbl = Label(top, text = "KEvin").pack()

root.mainloop()