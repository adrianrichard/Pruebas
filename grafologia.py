import tkinter as tk
from tkinter import ttk, messagebox

class HandwritingAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Escritura")
        self.root.geometry("600x700")

        # Variables para almacenar selecciones
        self.vars = {
            "size": tk.StringVar(),
            "slant": tk.StringVar(),
            "pressure": tk.StringVar(),
            "spacing": tk.StringVar(),
            "signature_legible": tk.StringVar(),
            "signature_size": tk.StringVar()
        }

        # Interfaz
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        ttk.Label(main_frame, text="Selecciona los aspectos a analizar",
                 font=("Arial", 14, "bold")).pack(pady=10)

        # --- Combobox para cada aspecto ---
        self.create_combobox(main_frame, "Tamaño de letra:", "size", [
            "Grande (extrovertido)",
            "Mediano (equilibrado)",
            "Pequeño (introvertido)",
            "Variable (inestable)"
        ])

        self.create_combobox(main_frame, "Inclinación:", "slant", [
            "Derecha (sociable)",
            "Izquierda (reservado)",
            "Vertical (racional)",
            "Irregular (impulsivo)"
        ])

        self.create_combobox(main_frame, "Presión del trazo:", "pressure", [
            "Fuerte (determinación)",
            "Moderada (equilibrio)",
            "Suave (sensibilidad)",
            "Irregular (estrés)"
        ])

        self.create_combobox(main_frame, "Espaciado entre palabras:", "spacing", [
            "Amplio (libertad)",
            "Estrecho (dependencia)",
            "Uniforme (disciplina)",
            "Irregular (confusión)"
        ])

        self.create_combobox(main_frame, "Legibilidad de la firma:", "signature_legible", [
            "Legible (transparencia)",
            "Ilegible (protección)",
            "Parcialmente legible"
        ])

        self.create_combobox(main_frame, "Tamaño de la firma vs texto:", "signature_size", [
            "Más grande (autoestima alta)",
            "Similar (equilibrio)",
            "Más pequeña (inseguridad)"
        ])

        # Botón de análisis
        ttk.Button(
            main_frame,
            text="Analizar Escritura",
            command=self.analyze_handwriting
        ).pack(pady=20)

        # Área de resultados
        self.result_text = tk.Text(main_frame, height=15, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH)

    def create_combobox(self, parent, label_text, var_key, options):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)

        ttk.Label(frame, text=label_text).pack(side=tk.LEFT, padx=5)

        combo = ttk.Combobox(
            frame,
            textvariable=self.vars[var_key],
            values=options,
            state="readonly",
            width=40
        )
        combo.pack(side=tk.RIGHT, expand=True)

    def analyze_handwriting(self):
        # Validar que todos los campos estén seleccionados
        for var_name, var in self.vars.items():
            if not var.get():
                messagebox.showerror("Error", f"¡Por favor, selecciona una opción para '{var_name}'!")
                return

        # Generar informe
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "=== RESULTADOS DEL ANÁLISIS ===\n\n")

        aspect_names = {
            "size": "Tamaño de letra",
            "slant": "Inclinación",
            "pressure": "Presión",
            "spacing": "Espaciado",
            "signature_legible": "Firma (legibilidad)",
            "signature_size": "Firma (tamaño relativo)"
        }

        for var_key, var in self.vars.items():
            self.result_text.insert(tk.END, f"• {aspect_names[var_key]}: {var.get()}\n")

        messagebox.showinfo("Éxito", "Análisis completado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HandwritingAnalyzerApp(root)
    root.mainloop()