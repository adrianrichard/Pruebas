from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.filedialog as tk_file
import os
images_list=[]
images_vars=[]  
class ImageGalleryApp:
    def __init__(self, root):
        
        def display_image(index):
            image_display_lb.config(image=images_list[index][1])

        def load_images():

            dir_path = tk_file.askdirectory()
            images_files = os.listdir(dir_path)
          
            for r in range(0, len(images_files)):
                images_list.append([
                    ImageTk.PhotoImage(Image.open(dir_path + '/' + images_files[r]).resize((50, 50), Image.Resampling.LANCZOS)),
                    ImageTk.PhotoImage(Image.open(dir_path + '/'+ images_files[r]).resize((480,360), Image.Resampling.LANCZOS))
                    ])
                images_vars.append(f'imag_{r}')

            for n in range(len(images_vars)):
                globals()[images_vars[n]] = tk.Button(slider, image=images_list[n][0], bd=0, command= lambda n=n: display_image(n))
                globals()[images_vars[n]].grid(row=2, column=n)

        menu_btn = tk.Button(root, text= 'Abrir carpeta', bd=0, font=('Bold', 15), command=load_images)
        menu_btn.grid( row=0, column=1, padx=20, pady=20)        
        image_display_lb = tk.Label(root)
        image_display_lb.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        canvas = tk.Canvas(root, height=60, width=500)
        canvas.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        x_scroll_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
        x_scroll_bar.grid(column = 0, row = 3, sticky='ns')
        x_scroll_bar.config(command=canvas.xview)
        canvas.config(xscrollcommand=x_scroll_bar.set)
        canvas.bind('<Configure>', lambda e: canvas.bbox('all'))
        slider = tk.Frame(canvas)
        canvas.create_window((0, 0), window=slider, anchor=tk.NW)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
