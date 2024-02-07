from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from controller import *

# Se configura la ruta de acceso a las imágenes

#IMPORTANTE: Para cargar exitosamente las imágenes del proyecto, se deberá colocar la ruta absoluta del entorno local, como se muestra en la imágen a continuación.


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./images")
# G:\TECNICATURA EN DESARROLLO DE SOFTWARE\PROGRAMACIONFINAL\veterinariaPythonAndTkinter\view\images
# C:\Users\Usuario\Desktop\TPFinal\veterinariaPythonAndTkinter\view\images

#def relative_to_assets(path: str) -> Path:
#    return ASSETS_PATH / Path(path)


# Pantalla principal

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Fondo de pantalla

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage("image_1.png")
image_1 = canvas.create_image(
    500.0,
    300.0,
    image=image_image_1
)

# Titulo de la Aplicación con sus íconos

canvas.create_rectangle(
    80.0,
    29.0,
    919.0,
    170.0,
    fill="#862B8E",
    outline="")

canvas.create_text(
    310.0,
    74.0,
    anchor="nw",
    text="PETS PYTHON CODE",
    fill="#FFCD29",
    font=("Comic Sans MS", 38 * -1, "italic")
)

image_image_2 = PhotoImage("image_9.png")
image_2 = canvas.create_image(
    150.0,
    99.0,
    image=image_image_2
)

image_image_3 = PhotoImage("image_10.png")
image_3 = canvas.create_image(
    827.0,
    99.0,
    image=image_image_3
)


# Botones de interconexion con otras ventanas
control = Controller()

button_image_1 = PhotoImage("button_5.png")
button_1 = Button(
    background="black",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=control.abrirVentanaProductos,
    relief="flat"
)
button_1.place(
    x=510.0,
    y=300.0,
    width=240.0,
    height=80.0
)

button_image_3 = PhotoImage("button_6.png")
button_3 = Button(
    background="black",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=control.abrirVentanaClientes,
    relief="flat"
)
button_3.place(
    x=250.0,
    y=300.0,
    width=240.0,
    height=80.0
)
window.resizable(False, False)
window.mainloop()