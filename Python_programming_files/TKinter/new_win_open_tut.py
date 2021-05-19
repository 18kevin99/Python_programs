from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to open new windows")

def win_open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("images/img_0.png"))
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = "Close Window", command = top.destroy).pack()

btn = Button(root, text= "Open Second window", command = win_open).pack()


root.mainloop()
