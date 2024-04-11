import tkinter as tk
import sqlite3
import io
from PIL import Image, ImageTk
imagenes = []
class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Visor de Imágenes")

        self.image_index = 0
        self.images = [
            "odontograma.png", "carta.jpg"
        ]
        self.load_images_from_db()
        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.load_image()

        prev_button = tk.Button(self.master, text="Anterior", command=self.prev_image)
        prev_button.pack(side=tk.LEFT)

        next_button = tk.Button(self.master, text="Siguiente", command=self.next_image)
        next_button.pack(side=tk.RIGHT)

    def load_image(self):
##        image_path = self.images[self.image_index]
##        image = Image.open(image_path)
##        photo = ImageTk.PhotoImage(image)
        photo=imagenes[0]
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.load_image()

    def prev_image(self):
        self.image_index = (self.image_index - 1) % len(self.images)
        self.load_image()

    def load_images_from_db(self):
        print("prueba")
        conn = sqlite3.connect('image_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT image_data FROM images")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            image_blob = row[0]
            print(image_blob)
            image = Image.open(io.BytesIO(image_blob))
            imagenes.append(image)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()