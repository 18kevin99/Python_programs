from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("images_viewer")

def back_button(num):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image= img_lst[num - 1])
    button_next = Button(root, text=">>", command=lambda: next_button(num + 1))
    button_back = Button(root, text="<<", command=lambda: back_button(num - 1))

    if num == 0:
        button_back = Button(root, text="<<", state= DISABLED)
    my_label.grid(row = 0, column= 0, columnspan = 3)
    button_back.grid(row= 1, column = 0)
    button_next.grid(row= 1, column = 2)

    status = Label(root, text = "Image "+ str(num) +" of "+ str(len(img_lst)),bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)
    

def next_button(num):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image= img_lst[num - 1])
    button_next = Button(root, text=">>", command=lambda: next_button(num + 1))
    button_back = Button(root, text="<<", command=lambda: back_button(num - 1))

    if num == len(img_lst):
        button_next = Button(root, text=">>", state= DISABLED)
    my_label.grid(row = 0, column= 0, columnspan = 3)
    button_back.grid(row= 1, column = 0)
    button_next.grid(row= 1, column = 2)

    status = Label(root, text = "Image "+ str(num) +" of "+ str(len(img_lst)),bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)


    
my_img0 = ImageTk.PhotoImage(Image.open("images/img_0.png"))
my_img1 = ImageTk.PhotoImage(Image.open("images/img_1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img_2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img_3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img_4.png"))

img_lst = [my_img0,my_img1,my_img2,my_img3,my_img4]

status = Label(root, text = "Image 1 of "+ str(len(img_lst)),bd = 1, relief = SUNKEN, anchor = E)

my_label = Label(image = my_img0)
my_label.grid(row = 0, column= 0, columnspan = 3)

button_back = Button(root, text="<<", state = DISABLED, command= back_button)
button_exit = Button(root, text="QUIT", command= root.quit)
button_next = Button(root, text=">>", command=lambda: next_button(2))

button_back.grid(row= 1, column = 0)
button_exit.grid(row= 1, column = 1)
button_next.grid(row= 1, column = 2)

status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)
root.mainloop()
