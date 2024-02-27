import tkinter as tk
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Visor de Imágenes")

        self.image_index = 0
        self.images = [
            "6.png", "carta.jpg"
        ]

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.load_image()

        prev_button = tk.Button(self.master, text="Anterior", command=self.prev_image)
        prev_button.pack(side=tk.LEFT)

        next_button = tk.Button(self.master, text="Siguiente", command=self.next_image)
        next_button.pack(side=tk.RIGHT)

    def load_image(self):
        image_path = self.images[self.image_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.load_image()

    def prev_image(self):
        self.image_index = (self.image_index - 1) % len(self.images)
        self.load_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()