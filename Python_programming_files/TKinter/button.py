from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your Name")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me" , padx = 50, pady= 50, command = myClick, fg="red", bg="blue")#use HEX color codes or names 
myButton.pack()

root.mainloop()
