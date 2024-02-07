import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3

class ImageGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        self.conn = sqlite3.connect('image_gallery.db')
        self.create_table_in_database()

        self.images = []
        self.current_image_index = 0

        self.create_widgets()

    def create_table_in_database(self):
        query = '''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT
        );
        '''
        with self.conn:
            self.conn.execute(query)

    def create_widgets(self):
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        prev_button = tk.Button(self.root, text="Previous", command=self.show_previous_image)
        prev_button.pack(side=tk.LEFT, padx=10)

        next_button = tk.Button(self.root, text="Next", command=self.show_next_image)
        next_button.pack(side=tk.RIGHT, padx=10)

        add_button = tk.Button(self.root, text="Add Image", command=self.add_image)
        add_button.pack(side=tk.BOTTOM, pady=10)

        self.load_images_from_database()

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            with self.conn:
                self.conn.execute("INSERT INTO images (file_path) VALUES (?)", (file_path,))
            self.load_images_from_database()

    def load_images_from_database(self):
        with self.conn:
            result = self.conn.execute("SELECT file_path FROM images")
            self.images = [row[0] for row in result.fetchall()]

        self.show_current_image()

    def show_current_image(self):
        if self.images:
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            tk_image = ImageTk.PhotoImage(image)

            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image

    def show_previous_image(self):Nuevo
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_current_image()

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGalleryApp(root)
    root.mainloop()
