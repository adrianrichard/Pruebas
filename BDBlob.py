# from tkinter import *
# import tkinter as tk
# from PIL import ImageTk, Image
# import tkinter.filedialog as tk_file
# import io
# import sqlite3
# root = tk.Tk()

# root.geometry('800x550')

# root.title('Tkinter Hub')

# def display_image(index):
#     image_display_lb.config(image=images_list[index][1])

# images_list=[]
# images_vars=[]

# def load_images(canvas):
#     try:
#         conn = sqlite3.connect('imagenes.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT imagen FROM imagenes")
#         rows = cursor.fetchall()
#         conn.close()
#         # for row in rows:
#         #     image_blob = row[0]
#         #     image = Image.open(io.BytesIO(image_blob))
#         #     images_list.append([
#         #         ImageTk.PhotoImage(image.resize((50, 50), Image.Resampling.LANCZOS)),
#         #         ImageTk.PhotoImage(image, Image.Resampling.LANCZOS)
#         #     ])
#         # images_vars.append(f'imag_{r}')

#         for n in range(len(images_vars)):
#             globals()[images_vars[n]] = tk.Button(slider, image=images_list[n][0], bd=0, command= lambda n=n: display_image(n))
#             globals()[images_vars[n]].pack(side=tk.LEFT)
#         n =len(images_list)+1
#         canvas.config(scrollregion=(0,0,n*50,500))
#     except:
#         print("error")

# image_display_lb = tk.Label(root)
# image_display_lb.pack(anchor=tk.CENTER)
# canvas = tk.Canvas(root, height=60, width=500, scrollregion=(0,0,500,500))
# canvas.pack(side=tk.BOTTOM, fill=tk.X)
# x_scroll_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
# x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
# print(len(images_list))
# canvas.config(xscrollcommand=x_scroll_bar.set)
# canvas.bind('<Configure>', lambda e: canvas.bbox('all'))
# slider = tk.Frame(canvas)
# canvas.create_window((0, 0), window=slider, anchor=tk.NW)
# #print(len(images_vars))
# #load_images(canvas)
# menu_btn = tk.Button(root, text= 'Open Folder', bd=0, font=('Bold', 15), command=load_images(canvas))
# menu_btn.pack( side=tk.TOP, anchor=tk.W, padx=20, pady=20)

# root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import io
import os
import matplotlib.pyplot as plt
imagen_blob=[]
def cargar_imagen_desde_db():
    # Conectar a la base de datos SQLite
    print(os.path.isfile("image_data.db"))
    try:
##        print("0")
        conexion = sqlite3.connect("image_database.db")
##        print("00")
        cursor = conexion.cursor()

        # Ejecutar la consulta para obtener la imagen almacenada como BLOB
        #cursor.execute("SELECT imagen FROM imagenes")
        bd = "SELECT Image FROM Image"
        cursor.execute(bd)
        #cursor.execute("SELECT * FROM agenda")
        #image = cursor.fetchall()
        imagen_blob = cursor.fetchall()
##        print(nombres)
        for row in imagen_blob:
            imagen .append(io. BytesIO(row))

        #imagen_blob.append(image()[0])
        conexion.close()
##        print(imagen_blob)

    except:
        print("error conexion")
    # Convertir el BLOB en un objeto de imagen utilizando PIL
    try:
        imagen_pil = Image.open(BytesIO(imagen_blob[0]))
    except:
        print("error carga")
##    im = plt.imread(io.BytesIO(imagen_blob))
##    plt.imshow(im)



    # Mostrar la imagen en una ventana Tkinter
    ventana = tk.Tk()
    ventana.title("Imagen desde SQLite")

    # Convertir la imagen de PIL a un formato compatible con Tkinter
    #imagen_tk = ImageTk.PhotoImage(imagen_blob)

    # Crear un widget de etiqueta para mostrar la imagen
    #etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    #etiqueta_imagen.pack()

    # Asegúrate de mantener la referencia a la imagen para que no se elimine de la memoria
   # etiqueta_imagen.imagen_tk = imagen_tk

    # Cerrar la conexión a la base de datos

    ventana.mainloop()

# Llamar a la función para cargar y mostrar la imagen desde la base de datos
cargar_imagen_desde_db()

##import tkinter as tk
##from PIL import Image, ImageTk
##import sqlite3
##
##class VisorImagenes:
##    def __init__(self, master):
##        self.master = master
##        self.master.title("Visor de Imágenes")
##        self.frame = tk.Frame(self.master)
##        self.frame.pack()
##
##        self.conexion = sqlite3.connect("image_data.db")
##        self.cursor = self.conexion.cursor()
##
##        self.cargar_imagenes()
##        self.indice_actual = 0
##
##        self.mostrar_imagen_actual()
##
##        # Botones de navegación
##        self.btn_anterior = tk.Button(self.frame, text="Anterior", command=self.imagen_anterior)
##        self.btn_anterior.pack(side=tk.LEFT)
##        self.btn_siguiente = tk.Button(self.frame, text="Siguiente", command=self.siguiente_imagen)
##        self.btn_siguiente.pack(side=tk.LEFT)
##
##    def cargar_imagenes(self):
##        self.cursor.execute("SELECT Image FROM Image")
##        self.imagenes_blob = self.cursor.fetchall()
##
##    def mostrar_imagen_actual(self):
##        imagen_blob = self.imagenes_blob[self.indice_actual][0]
##        imagen_pil = Image.frombytes('RGB', (300, 300), imagen_blob)  # Ajusta el tamaño según tu imagen
##        imagen_tk = ImageTk.PhotoImage(imagen_pil)
##        if hasattr(self, 'label_imagen'):
##            self.label_imagen.pack_forget()
##        self.label_imagen = tk.Label(self.master, image=imagen_tk)
##        self.label_imagen.pack()
##
##    def imagen_anterior(self):
##        if self.indice_actual > 0:
##            self.indice_actual -= 1
##            self.mostrar_imagen_actual()
##
##    def siguiente_imagen(self):
##        if self.indice_actual < len(self.imagenes_blob) - 1:
##            self.indice_actual += 1
##            self.mostrar_imagen_actual()
##
##def main():
##    root = tk.Tk()
##    visor = VisorImagenes(root)
##    root.mainloop()
##
##if __name__ == '__main__':
##    main()
