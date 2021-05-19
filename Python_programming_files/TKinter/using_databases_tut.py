from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("using a database")
root.geometry("400x400")

#database
#create database

conn = sqlite3.connect("address_book.db")

#Create a cursor
c = conn.cursor()

#create table
c.execute(""" CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")

#commit changes
conn.commit()

#close connection
conn.close()


root.mainloop()
