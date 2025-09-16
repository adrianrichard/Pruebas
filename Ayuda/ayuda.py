import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

def abrir_chm_fijo():
    """
    Abre un archivo CHM específico sin diálogos de búsqueda
    """
    # Ruta fija del archivo CHM - AJUSTA ESTA RUTA
    chm_path = r"AyudaMyM.chm"

    # Verificar si el archivo existe
    if not os.path.exists(chm_path):
        messagebox.showerror("Error",
                           f"No se encontró el archivo CHM en:\n{chm_path}\n\n"
                           "Por favor, verifique que el archivo existe en la ubicación especificada.")
        return False

    try:
        # Abrir el archivo CHM según el sistema operativo
        if sys.platform == "win32":
            # Windows - método nativo
            os.startfile(chm_path)
        elif sys.platform == "linux":
            # Linux - intentar con visores comunes
            try:
                subprocess.Popen(["xchm", chm_path])
            except:
                try:
                    subprocess.Popen(["kchmviewer", chm_path])
                except:
                    messagebox.showerror("Error",
                                       "No se encontró ningún visor de CHM instalado.\n"
                                       "Instale xchm o kchmviewer.")
                    return False
        elif sys.platform == "darwin":
            # macOS
            try:
                subprocess.Popen(["hh", chm_path])
            except:
                messagebox.showerror("Error",
                                   "No se pudo abrir el archivo CHM en macOS.\n"
                                   "Asegúrese de tener un visor de CHM instalado.")
                return False
        return True

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo CHM:\n{str(e)}")
        return False


# EJEMPLO DE USO CON INTERFAZ SIMPLE
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Abrir CHM Específico")
    root.geometry("400x150")

    # Botón para abrir
    btn_abrir = tk.Button(root, text="(?)", command=abrir_chm_fijo,
                         bg="lightblue", font=("Arial", 12), padx=20, pady=10)
    btn_abrir.pack(pady=20)

    root.mainloop()