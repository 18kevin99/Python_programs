from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("FILE DIALOG BOX")

def open_image():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/", title= "Select File"
                                , filetypes=(("python_progs","*.py"),("PNG","*.png"),("All FIles","*.*")))
    my_label = Label(root, text = root.filename).pack()
    try:
        my_img = ImageTk.PhotoImage(Image.open(root.filename))
        img_label = Label(root, image= my_img).pack()
    except:
        print("please select a valid image file for this demo")
    
my_btn = Button(root, text= "Press to display png img", command = open_image).pack()
root.mainloop()
