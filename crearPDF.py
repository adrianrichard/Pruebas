from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle

# Crear el documento PDF
pdf_filename = "documento.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Obtener los estilos de muestra
styles = getSampleStyleSheet()

# Contenido del PDF
content = []

# Añadir el logo
logo_path = "LOGO1.png"  # Reemplaza con la ruta a tu logo
logo = Image(logo_path, width=2*inch, height=1*inch)
content.append(logo)

# Título
title = Paragraph("Reporte de Estadísticas del Negocio", styles['Title'])
content.append(title)

# Estadísticas
data = [
    ['Categoría', 'Valor'],
    ['Ventas Totales', '$100,000'],
    ['Clientes Nuevos', '150'],
    ['Proyectos Completados', '25'],
]

table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

content.append(table)

# Construir el documento PDF
document.build(content)

print(f"PDF generado: {pdf_filename}")
