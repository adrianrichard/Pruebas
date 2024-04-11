import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import *

import io
record=[]
imagenes = []
conn = sqlite3.connect('imagenes.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS imagenes
                      (id INTEGER PRIMARY KEY,
                       nombre TEXT,
                       imagen BLOB)''')
def convert_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image
def cargar_imagenes():
    conn = sqlite3.connect('imagenes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT imagen FROM imagenes")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        image_blob = row[0]
        image = Image.open(io.BytesIO(image_blob))
        imagenes.append(image)
    
def guardar_imagen():
    imagen_path = 'carta.jpg'
    with open(imagen_path, 'rb') as f:
        imagen_binaria = f.read()
    nombre = 'carta'
    print (nombre)
    cursor.execute('''INSERT INTO imagenes (nombre, imagen)
                          VALUES (?, ?)''', (nombre, imagen_binaria))
    print("YYYY")
    conn.commit()

def display_Table(root):
    my_tree = ttk.Treeview(root, yscrollcommand= vertical_scrollbar.set)
    my_tree.pack()
    vertical_scrollbar = ttk.Scrollbar(root)
    vertical_scrollbar.pack(side=RIGHT, fill=Y)
    vertical_scrollbar.config(command= my_tree.yview)

    style = ttk.Style(root)
    style.theme_use("winnative")
    style.configure(".", font=("Helvetica", 11))
    style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))
    style.configure("Treeview", rowheight=50) # set row height

    my_tree['columns'] = ("id",)
    my_tree.column("#0", width=100, stretch='NO') # set width
    my_tree.column("id", width=100, anchor='w')

    my_tree.heading("#0", anchor='w', text='Image')
    my_tree.heading("id", anchor='w', text="Id")

    count = 0

    my_tree.imglist = []
    for record in cursor_variable:
        img = Image.open(io.BytesIO(record[1]))
        img.thumbnail((50,50)) # resize the image to desired size
        img = ImageTk.PhotoImage(img)
        my_tree.insert(parent="", index="end", iid=count,
                       image=img, values=(record[0],)) # use "image" option for the image
        my_tree.imglist.append(img) # save the image reference
        count += 1

root = Tk()

id = Entry(root, width=10, font=("Helvetica", 20), bd=3)
id.pack()

browse_button = Button(root,text ='Browse',command = lambda:open_file())
browse_button.pack()

display_button = Button(root,text ='display',command =lambda:display_file(root))
display_button.pack()

display_table_button = Button(root,text ='display Table',command =lambda:display_Table(root))
display_table_button.pack()

root.mainloop()
