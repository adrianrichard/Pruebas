import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def capture_window(window):
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    return screenshot

def save_as_pdf(window, filename):
    screenshot = capture_window(window)
    screenshot.save("screenshot.png", "PNG")

    c = canvas.Canvas(filename, pagesize=letter)
    img = ImageReader("screenshot.png")
    w=img.width
    c.drawImage(img, 100, 100, width=w, height=img.height)
    c.save()

# Ejemplo de ventana Tkinter
def create_window():
    window = tk.Tk()
    window.title("Ejemplo de ventana Tkinter")
    label = ttk.Label(window, text="Hola, esta es una ventana de ejemplo.")
    label.pack(padx=20, pady=40)
    return window

if __name__ == "__main__":
    ventana = create_window()
    save_as_pdf(ventana, "ventana.pdf")
    ventana.mainloop()
