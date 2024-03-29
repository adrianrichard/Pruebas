import tkinter as tk

root = tk.Tk()
#root.configure(padx = 10, pady = 10)
buttons = []
colores=["red", "yellow", "blue","white"]
#tk.Button(root,height=6, width=6, justify="left").pack(padx=0, pady=0)
ancho = 900
canvas = tk.Canvas(root, width=ancho, height=600)
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
            canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
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
root.mainloop()
