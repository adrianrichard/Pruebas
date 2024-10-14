# Importar la librería graphviz
from graphviz import Digraph

# Crear el diagrama de entidad-relación normalizado
dot = Digraph(comment='Diagrama Entidad-Relación Normalizado')

# Entidades normalizadas
dot.node('Paciente', 'Paciente\n(DNI, Nombre, Domicilio)')
dot.node('Odontologo', 'Odontólogo\n(Matrícula, Nombre)')
dot.node('Turno', 'Turno\n(Fecha, Hora, Paciente, Odontólogo)')
dot.node('Odontograma', 'Odontograma\n(ID_Odontograma, Fecha, Paciente, Odontólogo)')
dot.node('Diente', 'Diente\n(Número, Paciente, id_odontograma, Caras, Corona, Extracción)')
dot.node('Prestacion', 'Prestación\n(ID_Prestacion, Fecha, Tipo_Prestacion, Paciente, Odontólogo)')

# Relaciones
dot.edge('Paciente', 'Turno', label='1..N')  # Paciente a Turno (uno a muchos)
dot.edge('Odontologo', 'Turno', label='1..N')  # Odontólogo a Turno (uno a muchos)
dot.edge('Paciente', 'Odontograma', label='1..N')  # Paciente a Odontograma (uno a muchos)
dot.edge('Odontologo', 'Odontograma', label='1..N')  # Odontólogo a Odontograma (uno a muchos)
dot.edge('Paciente', 'Diente', label='1..N')  # Paciente a Diente (uno a muchos)
dot.edge('Odontograma', 'Diente', label='1..N')  # Odontograma a Diente (uno a muchos)
dot.edge('Paciente', 'Prestacion', label='1..N')  # Paciente a Prestación (uno a muchos)
dot.edge('Odontologo', 'Prestacion', label='1..N')  # Odontólogo a Prestación (uno a muchos)

# Renderizar y guardar el diagrama en formato PNG
# Eliminar la opción cleanup=True para debugging
output_path = dot.render('diagrama_er_paciente_normalizado', format='png')

# Muestra la ruta donde se guarda el archivo
print(f"Diagrama guardado en: {output_path}")
