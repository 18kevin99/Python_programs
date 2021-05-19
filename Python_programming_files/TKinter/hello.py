from tkinter import *
"""
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
"""

root = Tk()
root.title('Kev_tut')

app = Frame(root)
app.pack(padx = 10, pady = 10)
myLabel = Label(app, text = "Hello World!")
myLabel.pack()

root.mainloop()
