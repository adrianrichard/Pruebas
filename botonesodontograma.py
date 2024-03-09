import tkinter as tk



root = tk.Tk()
#root.configure(padx = 10, pady = 10)
buttons = []
colores=["red", "yellow", "blue","green"]
#tk.Button(root,height=6, width=6, justify="left").pack(padx=0, pady=0)
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


def button_click(event, index):
    canvas.itemconfig(buttons[index], fill="red")

def clicked():
    print("You clicked play!")
    #color="purple"

def crear_dientes():
    width = 60
    height = 60
    padding = 10
    num_buttons = 5
    dist_y =0
    #tk.Button(root,height=6, width=6, justify="left", command=clicked).pack(padx=0, pady=0)
    for i in range(num_buttons):
        dist_y +=10
        x1 = i * (width)
        y1 = 0
        x2 = x1 + width
        y2 = y1 + height

    ##    print(y2)
        #button_text = f"Button {i+1}"
        #button = canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")
    ##    canvas.create_rectangle(x1, y1, x2, y2,fill="red", tags="playbutton")
    
        btn = tk.Button(root, text='Welcome to Tkinter!', width=3, height=3, bd='0')
        btn.place(x=0, y=0)
        canvas.create_polygon(x1, y1, x1 + width/2, y2/2, x1, y2,fill=colores[0], outline = "black", tags="d1_i")
        #canvas.create_polygon(x1, y1, x1 + width/2, y2/2, x2, y1,fill=colores[1], outline = "black", tags="d1_s")
        #canvas.create_polygon(x2, y1, x1 + width/2, y2/2, x2, y2,fill=colores[2], outline = "black", tags="playbutton")
        #canvas.create_polygon(x1, y2, x1 + width/2, y2/2, x2, y2,fill=colores[3], outline = "black", tags="playbutton")
        #canvas.create_rectangle(x1 + width/3, y1 + height/3, x2 - width/3, y2 - height/3,fill="white")
        #canvas.tag_bind("d1_i","<Button-1>", clicked)
        #canvas.tag_bind("d1_s","<Button-1>", clicked)

##        buttons.append(button)
##        canvas.tag_bind(button, "<Button-1>", lambda event, index=i: button_click(event, index))

crear_dientes()
root.mainloop()
