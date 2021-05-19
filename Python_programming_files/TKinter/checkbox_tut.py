from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("MAKING CHECKBOXES")
root.geometry("400x400")

def get_value():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar()

c = Checkbutton(root, text = "Check This box", variable = var, onvalue = "ON", offvalue= "OFF")
c.deselect()
c.pack()


myButton = Button(root,text = "press her to see value", command = get_value).pack()

root.mainloop()
