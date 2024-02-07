import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta

class EditableTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self.rows = rows
        self.columns = columns
        self.current_week_start = self.get_start_of_current_week()

        self.cells = [[None for _ in range(columns)] for _ in range(rows)]
        self.selected_cell = None

        self.create_header()
        self.create_table()

    def get_start_of_current_week(self):
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        return start_of_week

    def create_header(self):
        header_labels = ["Horario"] + [f"{(self.current_week_start + timedelta(days=i)).strftime('%Y-%m-%d')}" for i in range(5)]  # De lunes a viernes
        day_labels = ["Día"] + [f"{(self.current_week_start + timedelta(days=i)).strftime('%A')}" for i in range(5)]  # Día de la semana

        for col, (header, day) in enumerate(zip(header_labels, day_labels)):
            header_label = tk.Label(self, text=f"{header}\n{day}", width=15, height=2, bg="lightgray", relief="ridge")
            header_label.grid(row=0, column=col, sticky="nsew")
            self.grid_columnconfigure(col, weight=1)

        # Botones para avanzar y retroceder de semana
        prev_week_button = tk.Button(self, text="<<", command=self.go_to_previous_week)
        prev_week_button.grid(row=0, column=len(header_labels), sticky="nsew")

        next_week_button = tk.Button(self, text=">>", command=self.go_to_next_week)
        next_week_button.grid(row=0, column=len(header_labels) + 1, sticky="nsew")

    def create_table(self):
        self.conn = sqlite3.connect('table_data.db')
        self.create_table_in_database()

        horarios = [f"{i}:00 AM" for i in range(9, 13)] + [f"{i}:00 PM" for i in range(1, 21)]
        for row, horario in enumerate(horarios, start=1):
            tk.Label(self, text=horario, width=15, height=2, bg="lightgray", relief="ridge").grid(row=row, column=0, sticky="nsew")

            for col in range(1, 6):  # 5 columns for Monday to Friday
                cell_entry = tk.Entry(self, width=15)
                cell_entry.grid(row=row, column=col, sticky="nsew")
                cell_entry.bind("<Button-1>", lambda event, r=row, c=col: self.on_cell_click(event, r, c))
##                self.cells[row - 1][col - 1] = cell_entry

                self.grid_rowconfigure(row, weight=1)

    def create_table_in_database(self):
        query = '''
        CREATE TABLE IF NOT EXISTS table_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            horario TEXT,
            fecha TEXT,
            contenido TEXT
        );
        '''
        with self.conn:
            self.conn.execute(query)

    def on_cell_click(self, event, row, col):
        if self.selected_cell:
            # Restablecer el color de la celda previamente seleccionada
            self.cells[self.selected_cell[0]][self.selected_cell[1]].config(bg="white")

        # Cambiar el color de la celda seleccionada
        self.cells[row - 1][col - 1].config(bg="lightblue")
        self.selected_cell = (row - 1, col - 1)

    def go_to_previous_week(self):
        self.current_week_start -= timedelta(days=7)
        self.update_table()

    def go_to_next_week(self):
        self.current_week_start += timedelta(days=7)
        self.update_table()

    def update_table(self):
        header_labels = ["Horario"] + [f"{(self.current_week_start + timedelta(days=i)).strftime('%Y-%m-%d')}" for i in range(5)]  # De lunes a viernes
        day_labels = ["Día"] + [f"{(self.current_week_start + timedelta(days=i)).strftime('%A')}" for i in range(5)]  # Día de la semana

        for col, (header, day) in enumerate(zip(header_labels, day_labels)):
            self.children["!label" + str(col)].config(text=f"{header}\n{day}")

        for row in range(1, self.rows + 1):
            for col in range(1, 6):  # 5 columns for Monday to Friday
                self.cells[row - 1][col - 1].delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Editable Table with Weekdays, Times, and Dates")

    table = EditableTable(root, rows=16, columns=5)  # 16 rows for times, 1 row for header
    table.pack(expand=True, fill="both")

##    save_button = ttk.Button(root, text="Guardar en la Base de Datos", command=table.save_to_database)
##    save_button.pack()

    root.mainloop()
