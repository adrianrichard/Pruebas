from tkinter import *
from tkinter import messagebox, ttk
from sqlite3 import *
#from tkcalendar import *
from datetime import *

class agenda():
	def __init__(self,root):
		root.geometry("655x360")
		root.title("Agenda")
		pestañas=ttk.Notebook(root, width=655, height=360)
		pestañas.pack()
		home = Frame(pestañas)
		eventos = Frame(pestañas)
		historial = Frame(pestañas)
		pestañas.add(home, text="Compromisos")
		pestañas.add(eventos, text="Pendientes")
		pestañas.add(historial, text="Historial")
		pestañas.bind("<<NotebookTabChanged>>", self.llenar_tablas)
		##Ventana Inicio
		princ_frame=LabelFrame(home, text="Registrar compromisos", bg="white")
		princ_frame.pack(fill=BOTH, expand=YES)
		second_frame=LabelFrame(princ_frame, text="Seleccione la fecha", bg="white")
		second_frame.pack()
		fecha=datetime.now()
		dia=int(fecha.strftime("%d"))
		mes=int(fecha.strftime("%m"))
		anio=int(fecha.strftime("%Y"))
		self.lbl_hora=Label(princ_frame, text="Hora:", bg="white")
		self.lbl_hora.pack()
		self.label_hora=Frame(princ_frame)
		self.label_hora.pack()
		self.hora_combo=ttk.Combobox(self.label_hora, width=5, state="readonly")
		self.hora_combo.pack(side=LEFT)
		self.min_combo=ttk.Combobox(self.label_hora, width=5, state="readonly")
		self.min_combo.pack(side=LEFT)
		self.horario_combo=ttk.Combobox(self.label_hora, width=5, state="readonly")
		self.horario_combo.pack(side=LEFT)
		self.hora_combo["values"]=("01","02","03","04","05","06","07","08","09","10","11","12")
		self.min_combo["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
		self.horario_combo["values"]=("am","pm")
		self.lbl_lugar=Label(princ_frame, text="Lugar:", bg="white")
		self.lbl_lugar.pack()
		self.entry_lugar=Entry(princ_frame, width=50)
		self.entry_lugar.pack()
		self.lbl_detalle=Label(princ_frame, text="Detalles", bg="white")
		self.lbl_detalle.pack()
		self.entry_detalle=Entry(princ_frame, width=50)
		self.entry_detalle.pack()
		self.btn_guardar=Button(princ_frame, text="Guardar", command=self.guardar_compromiso)
		self.btn_guardar.pack(anchor="c", padx=10)

		#Ventana eventos
		princ_frame_eventos=LabelFrame(eventos, text="Lista de compromisos pendientes", bg="white")
		princ_frame_eventos.pack()
		second_frame_eventos=LabelFrame(princ_frame_eventos, text="Seleccione la fecha", bg="white")
		second_frame_eventos.pack()
		scroll=ttk.Scrollbar(princ_frame_eventos)
		'''self.calendario2 = DateEntry(second_frame_eventos,width=22, day=dia, month=mes, year=anio,
		                 selectbackground='gray80',
		                 selectforeground='black',
		                 normalbackground='white',
		                 normalforeground='black',
		                 background='gray90',
		                 foreground='black',
		                 bordercolor='gray90',
		                 othermonthforeground='gray50',
		                 othermonthbackground='white',
		                 othermonthweforeground='gray50',
		                 othermonthwebackground='white',
		                 weekendbackground='white',
		                 weekendforeground='black',
		                 headersbackground='white',
		                 headersforeground='gray70',
		                 dateformat=3)
		self.calendario2.pack(side=LEFT)'''
		boton_buscar=Button(second_frame_eventos, text="Buscar por fecha", command=self.llenar_lista_por_fecha)
		boton_buscar.pack(side=LEFT)
		boton_buscar_todas=Button(second_frame_eventos, text="Buscar todas las fechas", command=self.llenar_lista)
		boton_buscar_todas.pack(side=LEFT, padx=(250,0))
		scroll.pack(side=RIGHT, fill=Y)
		scroll2=ttk.Scrollbar(princ_frame_eventos, orient=HORIZONTAL)
		scroll2.pack(side=BOTTOM, fill=X)
		self.tabla= ttk.Treeview(princ_frame_eventos, yscrollcommand=scroll.set, xscrollcommand=scroll2.set)
		self.tabla["columns"]=("one","two", "three", "four")
		#self.tabla.heading('#0', text = 'ID', anchor = CENTER)
		#self.tabla.column("#0",stretch=YES,width=75)
		self.tabla.heading('#1', text = 'Fecha', anchor = CENTER)
		self.tabla.column("#1",stretch=YES,width=75)
		self.tabla.heading('#2', text = 'Hora', anchor = CENTER)
		self.tabla.column("#2",stretch=YES, width=75)
		self.tabla.heading('#3', text = 'Lugar', anchor = CENTER)
		self.tabla.column("#3",stretch=YES, width=200)
		self.tabla.heading('#4', text = 'Detalle', anchor = CENTER)
		self.tabla.column("#4",stretch=YES, width=200)
		self.tabla.pack(fill="both", expand="yes")
		scroll.config(command=self.tabla.yview)
		scroll2.config(command=self.tabla.xview)
		third_frame_eventos=Frame(eventos,height=10)
		third_frame_eventos.pack(fill="x", expand=YES)
		btn_cancelar=Button(third_frame_eventos, text="Cancelar", command=self.cancelar_compromiso)
		btn_cancelar.pack(side=RIGHT)
		btn_atendido=Button(third_frame_eventos, text="Marcar como atendido", command=self.atender)
		btn_atendido.pack(side=RIGHT)

		#Ventana historial
		princ_frame_historial=LabelFrame(historial, text="Historial de compromisos", bg="white")
		princ_frame_historial.pack()
		scroll_historial=ttk.Scrollbar(princ_frame_historial)
		scroll_historial.pack(side=RIGHT, fill=Y)
		scroll2_historial=ttk.Scrollbar(princ_frame_historial, orient=HORIZONTAL)
		scroll2_historial.pack(side=BOTTOM, fill=X)
		self.tabla_historial= ttk.Treeview(princ_frame_historial, yscrollcommand=scroll_historial.set, xscrollcommand=scroll2_historial.set)
		self.tabla_historial["columns"]=("one","two", "three", "four")
		self.tabla_historial.heading('#0', text = 'ID', anchor = CENTER)
		self.tabla_historial.column("#0",stretch=YES,width=75)
		self.tabla_historial.heading('#1', text = 'Fecha', anchor = CENTER)
		self.tabla_historial.column("#1",stretch=YES,width=75)
		self.tabla_historial.heading('#2', text = 'Hora', anchor = CENTER)
		self.tabla_historial.column("#2",stretch=YES, width=75)
		self.tabla_historial.heading('#3', text = 'Lugar', anchor = CENTER)
		self.tabla_historial.column("#3",stretch=YES, width=200)
		self.tabla_historial.heading('#4', text = 'Detalle', anchor = CENTER)
		self.tabla_historial.column("#4",stretch=YES, width=200)
		self.tabla_historial.pack(fill="both", expand="yes")
		scroll_historial.config(command=self.tabla_historial.yview)
		scroll2_historial.config(command=self.tabla_historial.xview)
		third_frame_historial=Frame(historial,height=10)
		third_frame_historial.pack(fill="x")
		btn_pendiente_historial=Button(third_frame_historial, text="Marcar como Pendiente", command=self.pendiente)
		btn_pendiente_historial.pack(side=RIGHT)

	#Funciones de la ventana inicio
	def coneccion_bd(self,sql, parametros=()):
		global cursor, coneccion
		coneccion=connect("agenda_bd.sqlite")
		cursor=coneccion.cursor()
		cursor.execute(sql, parametros)
		coneccion.commit()

	def guardar_compromiso(self):
		hora=self.hora_combo.get()+":"+self.min_combo.get()+" "+self.horario_combo.get()
		sql="INSERT INTO agenda VALUES(NULL,?,?,?,?,?)"
		parametros=(self.calendario1.get(), hora, self.entry_lugar.get(), self.entry_detalle.get(), "Pendiente")
		self.coneccion_bd(sql, parametros)
		messagebox.showinfo(message="Datos guardados correctamente", title="Todo correcto")
		self.hora_combo.set("")
		self.min_combo.set("")
		self.horario_combo.set("")
		self.entry_lugar.delete(0,END)
		self.entry_detalle.delete(0,END)

	#Funciones de la ventana eventos

	def llenar_lista(self):
		elementos_tabla= self.tabla.get_children()
		for elemento in elementos_tabla:
			self.tabla.delete(elemento)

		lista_compromisos=[]
		sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
		parametros=("Pendiente",)
		self.coneccion_bd(sql, parametros)
		compromisos=cursor.fetchall()
		cont=0
		for fila in compromisos:
            #original
            #self.tabla.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
			self.tabla.insert("", END, values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
			cont+=1

	def llenar_lista_por_fecha(self):
		elementos_tabla=self.tabla.get_children()
		for elemento in elementos_tabla:
			self.tabla.delete(elemento)

		lista_compromisos=[]
		sql="SELECT * From agenda WHERE fecha=? and estado=? ORDER BY id_compromiso DESC"
		parametros=(self.calendario2.get(), "Pendiente")
		self.coneccion_bd(sql, parametros)
		compromisos=cursor.fetchall()
		cont=0
		for fila in compromisos:
			self.tabla.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
			cont+=1

	def cancelar_compromiso(self):
		try:
			self.tabla.selection()[0]
			id_compromiso=self.tabla.item(self.tabla.selection())['text']
			sql = "DELETE FROM agenda WHERE id_compromiso = ?"
			parametros= (id_compromiso,)
			self.coneccion_bd(sql,parametros)
			messagebox.showinfo(message="Se canceló la cita", title="Transacción correcta")
			self.llenar_lista()
		except IndexError as e:
			messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al cancelar compromiso")

	def atender(self):
		try:
			self.tabla.selection()[0]
			id_compromiso=self.tabla.item(self.tabla.selection())['text']
			sql = "UPDATE agenda SET estado=? WHERE id_compromiso = ?"
			parametros= ("Atendido",id_compromiso,)
			self.coneccion_bd(sql,parametros)
			messagebox.showinfo(message="Se marcó el compromiso como atendido", title="Transacción correcta")
			self.llenar_lista()
		except IndexError as e:
			messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al cancelar compromiso")

	#Funciones ventana historial

	def llenar_historial(self):
		elementos_tabla= self.tabla_historial.get_children()
		for elemento in elementos_tabla:
			self.tabla_historial.delete(elemento)

		lista_compromisos=[]
		sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
		parametros=("Atendido",)
		self.coneccion_bd(sql, parametros)
		compromisos=cursor.fetchall()
		cont=0
		for fila in compromisos:
			self.tabla_historial.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
			cont+=1

	def aux_llenar_historial(self):
		elementos_tabla= self.tabla_historial.get_children()
		for elemento in elementos_tabla:
			self.tabla_historial.delete(elemento)

		lista_compromisos=[]
		sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
		parametros=("Atendido",)
		coneccion_bd(sql, parametros)
		compromisos=cursor.fetchall()
		cont=0
		for fila in compromisos:
			self.tabla_historial.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
			cont+=1

	def pendiente(self):
		try:
			self.tabla_historial.selection()[0]
			id_compromiso=self.tabla_historial.item(self.tabla_historial.selection())['text']
			sql = "UPDATE agenda SET estado=? WHERE id_compromiso = ?"
			parametros= ("Pendiente",id_compromiso,)
			self.coneccion_bd(sql,parametros)
			messagebox.showinfo(message="Se marcó el compromiso como pendiente", title="Transacción correcta")
			self.aux_llenar_historial()
		except IndexError as e:
			messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al marcar como pendiente el compromiso")

	#Función para llenar las tablas en cnjunto con el combobind
	def llenar_tablas(self,event):
		self.llenar_lista()
		self.llenar_historial()

app=Tk()
window=agenda(app)
app.mainloop()















# #Funciones de la ventana inicio
# def coneccion_bd(sql, parametros=()):
# 	global cursor, coneccion
# 	coneccion=connect("agenda_bd.sqlite")
# 	cursor=coneccion.cursor()
# 	cursor.execute(sql, parametros)
# 	coneccion.commit()

# def guardar_compromiso():
# 	hora=hora_combo.get()+":"+min_combo.get()+" "+horario_combo.get()
# 	sql="INSERT INTO agenda VALUES(NULL,?,?,?,?,?)"
# 	parametros=(calendario1.get(), hora, entry_lugar.get(), entry_detalle.get(), "Pendiente")
# 	coneccion_bd(sql, parametros)
# 	messagebox.showinfo(message="Datos guardados correctamente", title="Todo correcto")
# 	hora_combo.set("")
# 	min_combo.set("")
# 	horario_combo.set("")
# 	entry_lugar.delete(0,END)
# 	entry_detalle.delete(0,END)

# #Funciones de la ventana eventos

# def llenar_lista():
# 	elementos_tabla= tabla.get_children()
# 	for elemento in elementos_tabla:
# 		tabla.delete(elemento)

# 	lista_compromisos=[]
# 	sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
# 	parametros=("Pendiente",)
# 	coneccion_bd(sql, parametros)
# 	compromisos=cursor.fetchall()
# 	cont=0
# 	for fila in compromisos:
# 		tabla.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
# 		cont+=1

# def llenar_lista_por_fecha():
# 	elementos_tabla= tabla.get_children()
# 	for elemento in elementos_tabla:
# 		tabla.delete(elemento)

# 	lista_compromisos=[]
# 	sql="SELECT * From agenda WHERE fecha=? and estado=? ORDER BY id_compromiso DESC"
# 	parametros=(calendario2.get(), "Pendiente")
# 	coneccion_bd(sql, parametros)
# 	compromisos=cursor.fetchall()
# 	cont=0
# 	for fila in compromisos:
# 		tabla.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
# 		cont+=1

# def cancelar_compromiso():
# 	try:
# 		tabla.selection()[0]
# 		id_compromiso=tabla.item(tabla.selection())['text']
# 		sql = "DELETE FROM agenda WHERE id_compromiso = ?"
# 		parametros= (id_compromiso,)
# 		coneccion_bd(sql,parametros)
# 		messagebox.showinfo(message="Se canceló la cita", title="Transacción correcta")
# 		llenar_lista()
# 	except IndexError as e:
# 		messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al cancelar compromiso")

# def atender():
# 	try:
# 		tabla.selection()[0]
# 		id_compromiso=tabla.item(tabla.selection())['text']
# 		sql = "UPDATE agenda SET estado=? WHERE id_compromiso = ?"
# 		parametros= ("Atendido",id_compromiso,)
# 		coneccion_bd(sql,parametros)
# 		messagebox.showinfo(message="Se marcó el compromiso como atendido", title="Transacción correcta")
# 		llenar_lista()
# 	except IndexError as e:
# 		messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al cancelar compromiso")

# #Funciones ventana historial

# def llenar_historial():
# 	elementos_tabla= tabla_historial.get_children()
# 	for elemento in elementos_tabla:
# 		tabla_historial.delete(elemento)

# 	lista_compromisos=[]
# 	sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
# 	parametros=("Atendido",)
# 	coneccion_bd(sql, parametros)
# 	compromisos=cursor.fetchall()
# 	cont=0
# 	for fila in compromisos:
# 		tabla_historial.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
# 		cont+=1

# def aux_llenar_historial():
# 	elementos_tabla= tabla_historial.get_children()
# 	for elemento in elementos_tabla:
# 		tabla_historial.delete(elemento)

# 	lista_compromisos=[]
# 	sql="SELECT * From agenda WHERE estado=? ORDER BY id_compromiso DESC"
# 	parametros=("Atendido",)
# 	coneccion_bd(sql, parametros)
# 	compromisos=cursor.fetchall()
# 	cont=0
# 	for fila in compromisos:
# 		tabla_historial.insert("", END, text=compromisos[cont][0], values=(compromisos[cont][1],compromisos[cont][2],compromisos[cont][3],compromisos[cont][4]))
# 		cont+=1

# def pendiente():
# 	try:
# 		tabla_historial.selection()[0]
# 		id_compromiso=tabla_historial.item(tabla_historial.selection())['text']
# 		sql = "UPDATE agenda SET estado=? WHERE id_compromiso = ?"
# 		parametros= ("Pendiente",id_compromiso,)
# 		coneccion_bd(sql,parametros)
# 		messagebox.showinfo(message="Se marcó el compromiso como pendiente", title="Transacción correcta")
# 		aux_llenar_historial()
# 	except IndexError as e:
# 		messagebox.showwarning(message="No ha seleccionado ningún item", title="Error al marcar como pendiente el compromiso")

# #Función para llenar las tablas en cnjunto con el combobind
# def llenar_tablas(event):
# 	llenar_lista()
# 	llenar_historial()


# root=Tk()
# root.geometry("655x360")
# root.title("Agenda")
# pestañas=ttk.Notebook(root, width=655, height=360)
# pestañas.pack()
# home = Frame(pestañas)
# eventos = Frame(pestañas)
# historial = Frame(pestañas)
# pestañas.add(home, text="Compromisos")
# pestañas.add(eventos, text="Pendientes")
# pestañas.add(historial, text="Historial")
# pestañas.bind("<<NotebookTabChanged>>", llenar_tablas)
# ##Ventana Inicio
# princ_frame=LabelFrame(home, text="Registrar compromisos", bg="white")
# princ_frame.pack(fill=BOTH, expand=YES)
# second_frame=LabelFrame(princ_frame, text="Seleccione la fecha", bg="white")
# second_frame.pack()
# fecha=datetime.now()
# dia=int(fecha.strftime("%d"))
# mes=int(fecha.strftime("%m"))
# anio=int(fecha.strftime("%Y"))
# calendario1 = DateEntry(second_frame,width=22, day=dia, month=mes, year=anio,
#                  selectbackground='gray80',
#                  selectforeground='black',
#                  normalbackground='white',
#                  normalforeground='black',
#                  background='gray90',
#                  foreground='black',
#                  bordercolor='gray90',
#                  othermonthforeground='gray50',
#                  othermonthbackground='white',
#                  othermonthweforeground='gray50',
#                  othermonthwebackground='white',
#                  weekendbackground='white',
#                  weekendforeground='black',
#                  headersbackground='white',
#                  headersforeground='gray70',
#                  dateformat=3)
# calendario1.pack()
# lbl_hora=Label(princ_frame, text="Hora:", bg="white")
# lbl_hora.pack()
# label_hora=Frame(princ_frame)
# label_hora.pack()
# hora_combo=ttk.Combobox(label_hora, width=5, state="readonly")
# hora_combo.pack(side=LEFT)
# min_combo=ttk.Combobox(label_hora, width=5, state="readonly")
# min_combo.pack(side=LEFT)
# horario_combo=ttk.Combobox(label_hora, width=5, state="readonly")
# horario_combo.pack(side=LEFT)
# hora_combo["values"]=("01","02","03","04","05","06","07","08","09","10","11","12")
# min_combo["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
# horario_combo["values"]=("am","pm")
# lbl_lugar=Label(princ_frame, text="Lugar:", bg="white")
# lbl_lugar.pack()
# entry_lugar=Entry(princ_frame, width=50)
# entry_lugar.pack()
# lbl_detalle=Label(princ_frame, text="Detalles", bg="white")
# lbl_detalle.pack()
# entry_detalle=Entry(princ_frame, width=50)
# entry_detalle.pack()
# btn_guardar=Button(princ_frame, text="Guardar", command=self.guardar_compromiso,)
# btn_guardar.pack(anchor="e", padx=10)

# #Ventana eventos
# princ_frame_eventos=LabelFrame(eventos, text="Lista de compromisos pendientes", bg="white")
# princ_frame_eventos.pack()
# second_frame_eventos=LabelFrame(princ_frame_eventos, text="Seleccione la fecha", bg="white")
# second_frame_eventos.pack()
# scroll=ttk.Scrollbar(princ_frame_eventos)
# calendario2 = DateEntry(second_frame_eventos,width=22, day=dia, month=mes, year=anio,
#                  selectbackground='gray80',
#                  selectforeground='black',
#                  normalbackground='white',
#                  normalforeground='black',
#                  background='gray90',
#                  foreground='black',
#                  bordercolor='gray90',
#                  othermonthforeground='gray50',
#                  othermonthbackground='white',
#                  othermonthweforeground='gray50',
#                  othermonthwebackground='white',
#                  weekendbackground='white',
#                  weekendforeground='black',
#                  headersbackground='white',
#                  headersforeground='gray70',
#                  dateformat=3)
# calendario2.pack(side=LEFT)
# boton_buscar=Button(second_frame_eventos, text="Buscar por fecha", command=self.llenar_lista_por_fecha)
# boton_buscar.pack(side=LEFT)
# boton_buscar_todas=Button(second_frame_eventos, text="Buscar todas las fechas", command=self.llenar_lista)
# boton_buscar_todas.pack(side=LEFT, padx=(250,0))
# scroll.pack(side=RIGHT, fill=Y)
# scroll2=ttk.Scrollbar(princ_frame_eventos, orient=HORIZONTAL)
# scroll2.pack(side=BOTTOM, fill=X)
# tabla= ttk.Treeview(princ_frame_eventos, yscrollcommand=self.scroll.set, xscrollcommand=self.scroll2.set)
# tabla["columns"]=("one","two", "three", "four")
# tabla.heading('#0', text = 'ID', anchor = CENTER)
# tabla.column("#0",stretch=YES,width=75)
# tabla.heading('#1', text = 'Fecha', anchor = CENTER)
# tabla.column("#1",stretch=YES,width=75)
# tabla.heading('#2', text = 'Hora', anchor = CENTER)
# tabla.column("#2",stretch=YES, width=75)
# tabla.heading('#3', text = 'Lugar', anchor = CENTER)
# tabla.column("#3",stretch=YES, width=200)
# tabla.heading('#4', text = 'Detalle', anchor = CENTER)
# tabla.column("#4",stretch=YES, width=200)
# tabla.pack(fill="both", expand="yes")
# scroll.config(command=self.tabla.yview)
# scroll2.config(command=self.tabla.xview)
# third_frame_eventos=Frame(eventos,height=10)
# third_frame_eventos.pack(fill="x", expand=YES)
# btn_cancelar=Button(third_frame_eventos, text="Cancelar", command=self.cancelar_compromiso)
# btn_cancelar.pack(side=RIGHT)
# btn_atendido=Button(third_frame_eventos, text="Marcar como atendido", command=self.atender)
# btn_atendido.pack(side=RIGHT)

# #Ventana historial
# princ_frame_historial=LabelFrame(historial, text="Historial de compromisos", bg="white")
# princ_frame_historial.pack()
# scroll_historial=ttk.Scrollbar(princ_frame_historial)
# scroll_historial.pack(side=RIGHT, fill=Y)
# scroll2_historial=ttk.Scrollbar(princ_frame_historial, orient=HORIZONTAL)
# scroll2_historial.pack(side=BOTTOM, fill=X)
# tabla_historial= ttk.Treeview(princ_frame_historial, yscrollcommand=self.scroll_historial.set, xscrollcommand=self.scroll2_historial.set)
# tabla_historial["columns"]=("one","two", "three", "four")
# tabla_historial.heading('#0', text = 'ID', anchor = CENTER)
# tabla_historial.column("#0",stretch=YES,width=75)
# tabla_historial.heading('#1', text = 'Fecha', anchor = CENTER)
# tabla_historial.column("#1",stretch=YES,width=75)
# tabla_historial.heading('#2', text = 'Hora', anchor = CENTER)
# tabla_historial.column("#2",stretch=YES, width=75)
# tabla_historial.heading('#3', text = 'Lugar', anchor = CENTER)
# tabla_historial.column("#3",stretch=YES, width=200)
# tabla_historial.heading('#4', text = 'Detalle', anchor = CENTER)
# tabla_historial.column("#4",stretch=YES, width=200)
# tabla_historial.pack(fill="both", expand="yes")
# scroll_historial.config(command=self.tabla_historial.yview)
# scroll2_historial.config(command=self.tabla_historial.xview)
# third_frame_historial=Frame(historial,height=10)
# third_frame_historial.pack(fill="x")
# btn_pendiente_historial=Button(third_frame_historial, text="Marcar como Pendiente", command=self.pendiente)
# btn_pendiente_historial.pack(side=RIGHT)


# root.mainloop()