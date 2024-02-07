import tkinter as tk
from tkinter import ttk
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from controller import *
from db_connector import DBConnector
from clientes import Cliente
from cliente_repositorio import ClienteRepository

#db_connector = DBConnector()
#cliente_repository = ClienteRepository(db_connector)

control = Controller()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./images")
# G:\TECNICATURA EN DESARROLLO DE SOFTWARE\PROGRAMACIONFINAL\veterinariaPythonAndTkinter\view\images
# C:\Users\Usuario\Desktop\TPFinal\veterinariaPythonAndTkinter\view\images

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cerrar_cliente():
    window.destroy()

def agregar_cliente():
    nombre = entry_nombre.get()
    domicilio = entry_dni.get()
    dni = entry_especie.get()
    mascota = entry_domicilio.get()
    especie = entry_mascota.get()
    edad = entry_edad.get()
    telefono = entry_telefono.get()
    turno = entry_fecha.get()

    if nombre and domicilio and dni and mascota and especie and edad and telefono:
        label_mensaje.config(text="")

        # Crear un cliente con los valores ingresados
        cliente = Cliente(
            dni,
            nombre,
            domicilio,
            mascota,
            especie,
            edad,
            telefono,
            turno
        )

        print(cliente)

        # Guardar el cliente en la base de datos
        #cliente_repository.guardar_cliente(cliente)

        # Actualizar la tabla con los datos del cliente
        actualizar_tabla(cliente)

        # Limpiar los campos de entrada después de agregar un cliente
        entry_nombre.delete(0, "end")
        entry_domicilio.delete(0, "end")
        entry_dni.delete(0, "end")
        entry_mascota.delete(0, "end")
        entry_especie.delete(0, "end")
        entry_edad.delete(0, "end")
        entry_telefono.delete(0, "end")
        entry_fecha.delete(0, "end")
        label_mensaje.config(text="Cliente creado", bg="green")

    else:
        label_mensaje.config(text="Por favor, complete todos los campos.", bg="red")

def eliminar_cliente():
    selected_item = tabla_clientes.selection()
    if selected_item:
        label_mensaje.config(text="")
        dni = tabla_clientes.item(selected_item, "values")[2]
        #cliente_repository.eliminar_cliente(dni)
        tabla_clientes.delete(selected_item)
        label_mensaje.config(text="Cliente eliminado correctamente", bg="green")
    else:
        label_mensaje.config(text="Seleccione un cliente para eliminar.")
def editar_cliente():
    selected_item = tabla_clientes.selection()
    if selected_item:
        label_mensaje.config(text="")

        # Obtener los valores actuales de la fila seleccionada
        valores_actuales = tabla_clientes.item(selected_item)["values"]

    print(valores_actuales)
    # Mostrar los valores actuales en los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, valores_actuales[0])

    entry_domicilio.delete(0, tk.END)
    entry_domicilio.insert(0, valores_actuales[3])

    entry_dni.delete(0, tk.END)
    entry_dni.insert(0, valores_actuales[1])

    entry_mascota.delete(0, tk.END)
    entry_mascota.insert(0, valores_actuales[4])

    entry_especie.delete(0, tk.END)
    entry_especie.insert(0, valores_actuales[2])

    entry_edad.delete(0, tk.END)
    entry_edad.insert(0, valores_actuales[5])

    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, valores_actuales[6])

    entry_fecha.delete(0, tk.END)
    entry_fecha.insert(0, valores_actuales[7])
# Función para actualizar la tabla con los datos del cliente
# Modificar la función actualizar_tabla para aceptar un objeto Cliente
def actualizar_tabla(cliente):
    tabla_clientes.insert("", "end", values=(
        cliente.getNombre(),
        cliente.getDomicilio(),
        cliente.getDni(),
        cliente.getMascota(),
        cliente.getEspecie(),
        cliente.getEdad(),
        cliente.getTelefono(),
        cliente.getTurno()
    ))
# Crear una lista para almacenar los clientes
lista_clientes = []


def listar_clientes():
    # Borra la tabla actual
    for row in tabla_clientes.get_children():
        tabla_clientes.delete(row)

    # Usa el repositorio para obtener los clientes
    #clientes = cliente_repository.listar_clientes()

    # Agrega los clientes a la tabla
    for cliente in clientes:
        tabla_clientes.insert("", "end", values=(
            cliente.getDni(),
            cliente.getNombre(),
            cliente.getDomicilio(),
            cliente.getMascota(),
            cliente.getEspecie(),
            cliente.getEdad(),
            cliente.getTelefono(),
            cliente.getTurno()
        ))

def actualizar_cliente():
    selected_item = tabla_clientes.selection()
    if selected_item:
        label_mensaje.config(text="")

        # Obtener el DNI del cliente seleccionado
        dni = tabla_clientes.item(selected_item, "values")[2]

        # Obtener los datos actualizados de los campos de entrada
        nombre = entry_nombre.get()
        domicilio = entry_domicilio.get()
        mascota = entry_mascota.get()
        especie = entry_especie.get()
        edad = entry_edad.get()
        telefono = entry_telefono.get()
        turno = entry_fecha.get()

        # Crear un objeto Cliente con los datos actualizados
        cliente_actualizado = Cliente(
            dni,
            nombre,
            domicilio,
            mascota,
            especie,
            edad,
            telefono,
            turno
        )

        # Llamar al método de actualización en el repositorio
        #cliente_repository.actualizar_cliente(cliente_actualizado)

        # Actualizar la tabla con los datos del cliente actualizado
        actualizar_tabla(cliente_actualizado)

        label_mensaje.config(text="Cliente actualizado exitosamente", bg="green")
    else:
        label_mensaje.config(text="Seleccione un cliente para actualizar.", bg="red")


window = Tk()
window.title('TURNOS CLIENTES - Rango/Galvez - Prof. Bozalongo')
window.geometry("1000x600")
window.configure(bg = "#5D12FC")


canvas = Canvas(
    window,
    bg = "#5D12FC",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
label_mensaje = tk.Label(window, text="", fg="white", bg="red")
label_mensaje.pack()

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage("image_1.png")
image_1 = canvas.create_image(
    500.0,
    300.0,
    image=image_image_1
)

entry_telefono_imagen = PhotoImage("entry_1.png")
entry_bg_7 = canvas.create_image(
    730.5,
    533.5,
    image=entry_telefono_imagen
)
entry_telefono = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_telefono.place(
    x=663.0,
    y=522.0,
    width=135.0,
    height=21.0
)


image_telephone = PhotoImage("tel_icon.png")
tel_icon = canvas.create_image(
    665.0,
    498.0,
    image=image_telephone
)




entry_turno_imagen = PhotoImage("trash.png")
entry_bg_7 = canvas.create_image(
    663.0,
    443.0,
    image=entry_turno_imagen
)
entry_fecha = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_fecha.place(
    x=663.0,
    y=443.0,
    width=135.0,
    height=21.0
)


image_telephone = PhotoImage("trash.png")
tel_icon = canvas.create_image(
    663.0,
    443.0,
    image=image_telephone
)


boton_eliminar_imagen = PhotoImage("boton_eliminar.png")
boton_eliminar = Button(
    image=boton_eliminar_imagen,
    borderwidth=0,
    highlightthickness=0,
    command=eliminar_cliente,
    relief="flat"
)
boton_eliminar.place(
    x=822.0,
    y=364.0,
    width=167.0,
    height=50.0
)

boton_volver_imagen = PhotoImage("boton_volver.png")
boton_volver = Button(
    image=boton_volver_imagen,
    borderwidth=0,
    highlightthickness=0,
    command=cerrar_cliente,
    relief="flat"
)
boton_volver.place(
    x=19.0,
    y=19.0,
    width=121.0,
    height=50.0
)

boton_agregar_imagen = PhotoImage("boton_agregar.png")
boton_agregar = Button(
    image=boton_agregar_imagen,
    borderwidth=0,
    highlightthickness=0,
    command=agregar_cliente,  # Vincular la función al botón,
    relief="flat"
)
boton_agregar.place(
    x=822.0,
    y=518.0,
    width=167.0,
    height=50.00000762939453
)

boton_editar_imagen = PhotoImage("boton_editar.png")
boton_editar = Button(
    image=boton_editar_imagen,
    borderwidth=0,
    highlightthickness=0,
    command=editar_cliente,
    relief="flat"
)
boton_editar.place(
    x=822.0,
    y=441.0,
    width=167.0,
    height=50.0
)

canvas.create_text(
    420.0,
    24.0,
    anchor="nw",
    text="TURNOS CLIENTES",
    fill="#FFFFFF",
    font=("Roboto Black", 22 * -1)
)

canvas.create_rectangle(
    52.0,
    362.0,
    210.0,
    391.38999938964844,
    fill="#6937D5",
    outline="")

canvas.create_rectangle(
    73.0,
    478.0,
    113.0,
    518.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    73.0,
    400.0,
    113.0,
    440.0,
    fill="#872B8F",
    outline="")

canvas.create_rectangle(
    480.0,
    474.0,
    520.0,
    514.0,
    fill="#872B8F",
    outline="")

canvas.create_rectangle(
    480.0,
    474.0,
    520.0,
    514.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    277.0,
    478.0,
    317.0,
    518.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    277.0,
    478.0,
    317.0,
    518.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    73.0,
    478.0,
    113.0,
    518.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    79.0,
    474.0,
    815.0,
    515.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    79.0,
    399.0,
    638.0,
    440.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    51.0,
    399.0,
    815.0,
    570.0,
    fill="#872B8F",
    outline="")

entry_nombre_image = PhotoImage("entry_1.png")
entry_bg_1 = canvas.create_image(
    155.5,
    454.5,
    image=entry_nombre_image
)
entry_nombre = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_nombre.place(
    x=88.0,
    y=443.0,
    width=135.0,
    height=21.0
)

entry_domicilio_image = PhotoImage("entry_1.png")
entry_bg_2 = canvas.create_image(
    155.5,
    533.5,
    image=entry_domicilio_image
)
entry_domicilio = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_domicilio.place(
    x=88.0,
    y=522.0,
    width=135.0,
    height=21.0
)

entry_dni_image = PhotoImage("entry_1.png")
entry_bg_3 = canvas.create_image(
    358.5,
    454.5,
    image=entry_dni_image
)
entry_dni = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_dni.place(
    x=291.0,
    y=443.0,
    width=135.0,
    height=21.0
)

entry_mascota_image = PhotoImage("entry_1.png")
entry_bg_4 = canvas.create_image(
    358.5,
    533.5,
    image=entry_mascota_image
)
entry_mascota = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_mascota.place(
    x=291.0,
    y=522.0,
    width=135.0,
    height=21.0
)

entry_especie_imagen = PhotoImage("entry_1.png")
entry_bg_5 = canvas.create_image(
    561.5,
    454.5,
    image=entry_especie_imagen
)
entry_especie = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_especie.place(
    x=494.0,
    y=443.0,
    width=135.0,
    height=21.0
)

canvas.create_text(
    317.0,
    416.0,
    anchor="nw",
    text="DOMICILIO",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    113.0,
    496.0,
    anchor="nw",
    text="MASCOTA",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_rectangle(
    73.0,
    400.0,
    113.0,
    440.0,
    fill="#872B8F",
    outline="")

canvas.create_text(
    113.0,
    416.0,
    anchor="nw",
    text="NOMBRE",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    317.0,
    496.0,
    anchor="nw",
    text="ESPECIE",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    520.0,
    416.0,
    anchor="nw",
    text="DNI",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

entry_edad_imagen = PhotoImage("entry_1.png")
entry_bg_6 = canvas.create_image(
    561.5,
    533.5,
    image=entry_edad_imagen
)
entry_edad = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_edad.place(
    x=494.0,
    y=522.0,
    width=135.0,
    height=21.0
)

entry_telefono_imagen = PhotoImage("trash.png")
entry_bg_7 = canvas.create_image(
    730.5,
    533.5,
    image=entry_telefono_imagen
)
entry_telefono = Entry(
    bd=0,
    bg="#C7BFBF",
    fg="#000716",
    highlightthickness=0
)
entry_telefono.place(
    x=663.0,
    y=522.0,
    width=135.0,
    height=21.0
)

canvas.create_text(
    515.0,
    496.0,
    anchor="nw",
    text="EDAD",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    695.0,
    496.0,
    anchor="nw",
    text="TELEFONO",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    695.0,
    416.0,
    anchor="nw",
    text="FECHA-HORA",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 11 * -1)
)

canvas.create_text(
    52.0,
    362.0,
    anchor="nw",
    text="Asignar o editar",
    fill="#FFFFFF",
    font=("Roboto Black", 22 * -1)
)

user_imagen = PhotoImage("icon_user.png")
icon_user = canvas.create_image(
    93.0,
    420.0,
    image=user_imagen
)

clock_imagen = PhotoImage("clock_icon.png")
clock_icon = canvas.create_image(
    500.0,
    498.0,
    image=clock_imagen
)

world_imagen = PhotoImage("world_icon.png")
world_icon = canvas.create_image(
    297.0,
    498.0,
    image=world_imagen
)

pet_imagen = PhotoImage("pet_icon.png")
pet_icon = canvas.create_image(
    93.0,
    498.0,
    image=pet_imagen
)

canvas.create_rectangle(
    645.0,
    478.0,
    685.0,
    518.0,
    fill="#872B8F",
    outline="")

canvas.create_rectangle(
    645.0,
    478.0,
    685.0,
    518.0,
    fill="#872B8F",
    outline="")

image_telephone = PhotoImage("tel_icon.png")
tel_icon = canvas.create_image(
    665.0,
    498.0,
    image=image_telephone
)

imageTurno = PhotoImage("cal2.png")
tel_icon = canvas.create_image(
    665.0,
    420,
    image=imageTurno
)


canvas.create_rectangle(
    277.0,
    400.0,
    317.0,
    440.0,
    fill="#872B8F",
    outline="")

canvas.create_rectangle(
    277.0,
    400.0,
    317.0,
    440.0,
    fill="#872B8F",
    outline="")

home_imagen = PhotoImage("home_icon.png")
home_icon = canvas.create_image(
    297.0,
    420.0,
    image=home_imagen
)

canvas.create_rectangle(480.0,400.0,520.0,440.0,fill="#872B8F",outline="")

canvas.create_rectangle(
    480.0,
    400.0,
    520.0,
    440.0,
    fill="#872B8F",
    outline="")

dni_imagen = PhotoImage("dni_icon.png")
dni_icon = canvas.create_image(
    500.0,
    420.0,
    image=dni_imagen
)
# Aca adentro quiero generar la tabla que necesito
canvas.create_rectangle(
    146.0,
    84.0,
    894.0,
    334.0,
    fill="#CF2A2A",
    outline="")


# Crear una instancia de ttk.Style
style = ttk.Style()


# Definir un estilo personalizado para la tabla (encabezado)
style.configure("Tabla.Heading",
                background="#CF2A2A",  # Cambia el color de fondo del encabezado aquí
                foreground="white",    # Cambia el color del texto del encabezado aquí
                font=("Helvetica", 12))  # Cambia la fuente y el tamaño del encabezado aquí


# Definir un estilo personalizado para la tabla
style.configure("Tabla.Treeview",
                background="#872B8F",  # Cambia el color de fondo aquí
                foreground="white",    # Cambia el color del texto aquí
                font=("Roboto", 10))  # Cambia la fuente y el tamaño aquí

# Crear el Treeview para mostrar la tabla de clientes y aplicar el estilo
tabla_clientes = ttk.Treeview(
    window,
    columns=("Nombre", "Domicilio", "DNI", "Mascota", "Especie", "Edad", "Telefono","Turno"),
    show="headings",
    style="Tabla.Treeview"  # Aplicar el estilo personalizado aquí
)

# Configurar las columnas
tabla_clientes.heading("Nombre", text="Nombre")
tabla_clientes.heading("Domicilio", text="Domicilio")
tabla_clientes.heading("DNI", text="DNI")
tabla_clientes.heading("Mascota", text="Mascota")
tabla_clientes.heading("Especie", text="Especie")
tabla_clientes.heading("Edad", text="Edad")
tabla_clientes.heading("Telefono", text="Teléfono")
tabla_clientes.heading("Turno", text="Turno")

# Ajustar el ancho de las columnas (puedes ajustarlo según tu diseño)
tabla_clientes.column("Nombre", width=120)
tabla_clientes.column("Domicilio", width=100)
tabla_clientes.column("DNI", width=100)
tabla_clientes.column("Mascota", width=100)
tabla_clientes.column("Especie", width=100)
tabla_clientes.column("Edad", width=60)
tabla_clientes.column("Telefono", width=100)
tabla_clientes.column("Turno", width=125)

# Colocar el Treeview en la posición deseada
tabla_clientes.place(x=146.0, y=84.0, width=800.0, height=250.0)
# Modificar el bucle principal para cargar los clientes desde el repositorio
##for cliente in cliente_repository.listar_clientes():
##    actualizar_tabla(cliente)


window.resizable(False, False)
window.mainloop()
