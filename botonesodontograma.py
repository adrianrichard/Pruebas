import tkinter as tk
from tkinter import Frame, Label
import sqlite3
from PIL import ImageGrab

root = tk.Tk()
#root.configure(padx = 10, pady = 10)
buttons = []
try:
    miConexion=sqlite3.connect("../Proyecto-Final/bd/DBpaciente.sqlite3")
    miCursor=miConexion.cursor()
    sql = "SELECT Apellido, Nombre, DNI, Telefono, ObraSocial FROM Paciente ORDER BY Apellido"
    apellido='LOPEZ'
    miCursor.execute(sql)    
    pacientes = miCursor.fetchall()
    miConexion.commit()
    #print(pacientes)
except:
    print("error")
colores=["red", "yellow", "blue","white"]
def capture_screenshot():
    # Capturar la pantalla y guardarla como una imagen
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png", "PNG")
#tk.Button(root,height=6, width=6, justify="left").pack(padx=0, pady=0)
ancho = 900
Label(root, text='Dientes', font='Arial 20').grid(column=0, row=0)
nombre=pacientes[0][1]
apellido=pacientes[0][0]
obra_social=pacientes[0][4]
dni=pacientes[0][2]
frame_datos_paciente=Frame(root)
frame_datos_paciente.grid(column=0, row=1)
Label(frame_datos_paciente, text='Nombre Completo: '+apellido+', '+nombre, font='Arial 15').grid(column=0, row=0)
Label(frame_datos_paciente, text='Obra Social: '+obra_social,  font='Arial 15').grid(column=1, row=0)
Label(frame_datos_paciente, text='D.N.I.: '+str(dni),  font='Arial 15').grid(column=2, row=0)
frame_dientes = Frame(root)
frame_dientes.grid(column=0, row=2)
canvas = tk.Canvas(frame_dientes, width=ancho, height=600)
canvas.pack()

#def button_click(event, index):
    #canvas.itemconfig(buttons[index], fill="red")

def clicked():
    print("You clicked play!")
    #color="purple"

def crear_dientes():
    width = 42
    height = 42
    padding = 10
    num_buttons = 8
    x1=0
    for i in range(num_buttons):
        x1 = x1 + padding
        y1 = padding
        x2 = x1 + width
        y2 = y1 + height

        if (i%2):            
            d12=canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5,y1+5,x2-5,y2-5, width=5, outline="blue")

        elif (i%3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    canvas.create_line(0, y2+padding, ancho, y2+padding, width=3)

    x1=x1+10
    canvas.create_line(x1, 10, x1, 270, width=3)
    for i in range(num_buttons):
        x1 = x1 + padding
        y1 = padding
        x2 = x1 + width
        y2 = y1 + height

        if (i==5):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i%3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5, y1+5, x2-5, y2-5, fill="red", width=5)
            canvas.create_line(x1+5, y2-5, x2-5, y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    y1=y2+20
    x1=0
    for i in range(num_buttons):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    x1=x1+10

    for i in range(num_buttons):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5,y1+5,x2-5,y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    x1=155
    y1=y2 + 50 
    for i in range(num_buttons-3):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    x1=x2+11
    y1= 165
    for i in range(num_buttons-3):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    x1=155
    y1=y2 + 10 
    for i in range(num_buttons-3):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2
    x1=x2+11
    y1= y2-height
    for i in range(num_buttons-3):
        x1 = x1 + padding       
        x2 = x1 + width
        y2 = y1 + height                
        if (i==1):            
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_oval(x1+5, y1+5, x2-5, y2-5, width=5, outline="blue")

        elif (i==3):                    
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill="white", outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill="white", outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
            canvas.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
            canvas.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
        else:
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2,fill=colores[0], outline = "black")
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1,fill=colores[1], outline = "black")
            canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2,fill=colores[2], outline = "black")
            canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2,fill=colores[3], outline = "black")
            canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
        x1=x2    
crear_dientes()
capture_screenshot()
root.mainloop()
