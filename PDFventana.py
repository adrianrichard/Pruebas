import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

colores=["red", "yellow", "blue","white"]

def crear_pdf(datos_personales, prestaciones):
    nombre_pdf = "informe.pdf"
    c = canvas.Canvas(nombre_pdf, pagesize=letter)
    
    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Informe Médico")

    # Datos personales
    c.setFont("Helvetica", 12)
    y_personal = 700
    for etiqueta, valor in datos_personales.items():
        c.drawString(50, y_personal, f"{etiqueta}: {valor}")
        y_personal -= 20
    
    # Tabla de prestaciones
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_personal - 20, "Tabla de Prestaciones:")
    
    # Encabezados de la tabla
    y_tabla = y_personal - 40
    encabezados = ["Fecha", "Prestación", "Código", "Odontólogo"]
    x_start = 50
    for encabezado in encabezados:
        c.drawString(x_start, y_tabla, encabezado)
        x_start += 130
    
    # Datos de las prestaciones
    y_tabla -= 20
    for prestacion in prestaciones:
        x_start = 50
        for dato in prestacion:
            c.drawString(x_start, y_tabla, dato)
            x_start += 130
        y_tabla -= 20
    
    # Cuadrícula con Canvas    
    c.drawImage('LOGO1.png', 500, 700, width=100, height=80)
    c.drawPath
    # width = 42
    # height = 42
    # padding = 10
    # num_buttons = 8
    # x1=0
    # for i in range(num_buttons):
    #     x1 = x1 + padding
    #     y1 = y_cuadricula
    #     x2 = x1 + width
    #     y2 = y1 + height

    #     if (i%2):            
    #         c.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
    #         c.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
    #         c.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
    #         c.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
    #         c.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
    #         c.create_oval(x1+5,y1+5,x2-5,y2-5, width=5, outline="blue")

    #     elif (i%3):                    
    #         c.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill="white", outline = "black")
    #         c.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill="white", outline = "black")
    #         c.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
    #         c.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill="white", outline = "black")
    #         c.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
    #         c.create_line(x1+5,y1+5,x2-5,y2-5, fill="red", width=5)
    #         c.create_line(x1+5,y2-5,x2-5,y1+5, fill="red", width=5)
    #     # else:
        #     canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x1, y2, fill=colores[0], outline = "black")
        #     canvas.create_polygon(x1, y1, x1 + width/2, y1 + height/2, x2, y1, fill=colores[1], outline = "black")
        #     canvas.create_polygon(x2, y1, x1 + width/2, y1 + height/2, x2, y2, fill=colores[2], outline = "black")
        #     canvas.create_polygon(x1, y2, x1 + width/2, y1 + height/2, x2, y2, fill=colores[3], outline = "black")
        #     canvas.create_rectangle(x1 + width/3.0, y1 + height/3.0, x2 - width/3.0, y2 - height/3.0, fill="white")
    # c.drawString(50, y_cuadricula, "Cuadrícula con Canvas:")
    
    # # Dibujar cuadrícula
    # c.setStrokeColorRGB(0, 0, 0.5)  # color de línea: azul oscuro
    # c.setLineWidth(1)
    # x_start = 50
    # y_start = y_cuadricula - 50
    
    # for i in range(4):
    #     for j in range(10):
    #         c.rect(x_start + j * 50, y_start - i * 50, 50, 50)
    
    c.save()
    messagebox.showinfo("PDF Creado", f"Se ha creado el PDF: {nombre_pdf}")

def main():
    # Crear ventana
    root = tk.Tk()
    root.title("Generador de PDF de Informe Médico")
        
    # Datos de ejemplo
    datos_personales = {
        "Nombre completo": "Juan Pérez",
        "DNI": "12345678",
        "Dirección": "Calle Falsa 123",
        "Obra social": "ObraSocial SA",
        "Teléfono": "1122334455"
    }
    
    prestaciones = [
        ["2024-06-01", "Limpieza", "001", "Dr. Martínez"],
        ["2024-06-15", "Extracción", "002", "Dr. Gómez"]
    ]
    
    # Botón para generar el PDF
    btn_generar_pdf = tk.Button(root, text="Generar PDF", command=lambda: crear_pdf(datos_personales, prestaciones))
    btn_generar_pdf.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()