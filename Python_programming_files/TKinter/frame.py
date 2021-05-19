from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to code:")

frame = LabelFrame(root, text ="This is my frame", padx= 5, pady=5, bg = "red", fg = "blue")
frame.pack(padx=10, pady= 10)
button = Button(frame, text ="Don't click here", bg="blue", fg = "red")
button.grid(row= 0, column= 0)
button2 = Button(frame, text = "or here", bg="blue", fg = "red")
button2.grid(row= 1, column= 1)



root.mainloop()
