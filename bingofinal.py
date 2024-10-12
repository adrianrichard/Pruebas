import tkinter as tk
import random
import pyttsx3
import time
from tkinter import messagebox

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo")
        self.root.configure(bg="SkyBlue")
        self.root.resizable(False, False)

        self.numbers_drawn = []  # Cambiado a lista para mantener el orden de los números sorteados
        self.ultimos_numeros = []

        self.label = tk.Label(self.root, text="BINGO PARROQUIAL", font=("Helvetica", 20, 'bold'), width=40, borderwidth=2, relief="sunken", background='orange')
        self.label.grid(row=0, column=0, pady=5, columnspan=2)
        self.start_button = tk.Button(self.root, height=1, text="Acerca de", font=("Helvetica", 10, 'bold'), background='lightgreen',command=self.version)
        self.start_button.grid(row=0, column=1, pady=5, sticky=tk.E)

        Frame_botones = tk.Frame(self.root, borderwidth=4, relief="ridge")
        Frame_botones.grid(row=1, column=0)
        
        self.numero_sorteado_label = tk.Label(Frame_botones, text="Número sorteado", font=("Helvetica", 20, 'bold'), width=20, borderwidth=2, relief="sunken", background='orange')
        self.numero_sorteado_label.grid(row=0, column=0, padx=(10, 10))

        self.result_label = tk.Label(Frame_botones, text="", font=("Helvetica", 230))
        self.result_label.grid(row=1, column=0)        
        
        self.label_ultimos = tk.Label(Frame_botones, text="", font=('Helvetica', 25), background='lightgreen', height=1, width=18)
        self.label_ultimos.grid(row=2, column=0)

        self.start_button = tk.Button(Frame_botones, width=15, height=1, text="COMENZAR", font=("Helvetica", 15, 'bold'), bg="SkyBlue", command=self.start_draw)
        self.start_button.grid(row=3, column=0)

        self.stop_button = tk.Button(Frame_botones, width=15, height=1, text="PAUSAR", font=("Helvetica", 15, 'bold'), bg="SkyBlue", command=self.stop_draw, state=tk.DISABLED)
        self.stop_button.grid(row=4, column=0)

        self.clear_button = tk.Button(Frame_botones, width=15, height=1, text="REINICIAR", font=("Helvetica", 15, 'bold'), bg="SkyBlue", command=self.clear_grid)
        self.clear_button.grid(row=5, column=0)

        self.create_number_grid()

        self.engine = pyttsx3.init()
        self.voices =self.engine.getProperty('voices')      
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 150)  # Velocidad de la voz
        #self.engine.setProperty('volume', 10) 

        # Diccionario para números especiales del 10 al 19
        self.special_numbers = {
            10: "diez",
            11: "once",
            12: "doce",
            13: "trece",
            14: "catorce",
            15: "quince",
            16: "dieciséis",
            17: "diecisiete",
            18: "dieciocho",
            19: "diecinueve"
        }
    def version(self):
        messagebox.showinfo("Acerca de", "Creado por Adrián Richard \n Versión 2.0 - 2024")
        
    def create_number_grid(self):
        self.number_buttons = []
        frame_numeros = tk.Frame(self.root, background='SkyBlue')
        frame_numeros.grid(row=1, column=1, pady=5)

        for i in range(9):  # 9 filas
            for j in range(10):  # 10 columnas
                number = i * 10 + j + 1  # Calcular el número correspondiente
                button = tk.Button(frame_numeros, text=str(number), width=2, state=tk.DISABLED, font=("Helvetica", 20, 'bold'))
                button.grid(row=i, column=j, padx=3, pady=3)
                self.number_buttons.append(button)

    def start_draw(self):
        self.start_button.config(state=tk.DISABLED, text='CONTINUAR')
        self.stop_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.draw_number()

    def stop_draw(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.NORMAL)
        # No cancelamos el sorteo, solo dejamos de actualizar la interfaz y la voz
        self.root.after_cancel(self.draw_id)

    def draw_number(self):
        if len(self.numbers_drawn) < 90:
            number = random.randint(1, 90)            
            
            while number in self.numbers_drawn:
                number = random.randint(1, 90)
            
            # Mantener solo los últimos 5 números
            if len(self.ultimos_numeros) == 5:
                self.ultimos_numeros.pop(0)
            self.ultimos_numeros.append(number)
            self.label_ultimos.config(text=" - ".join(map(str, self.ultimos_numeros)))
            
            self.numbers_drawn.append(number)
            self.result_label.config(text=number)
            self.root.update()
            self.update_number_grid(number)
            time.sleep(1)
            self.speak_number(number)

            self.draw_id = self.root.after(2000, self.draw_number)  # Llamada recursiva cada 2000ms (2 segundo)
        else:
            messagebox.showinfo("FIN", "¡Todos los números han sido sorteados!")
            #self.result_label.config(text="¡Todos los números han sido sorteados!", font=("Helvetica", 15, 'bold'))
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.clear_button.config(state=tk.NORMAL)

    def reset_number_grid(self):
        for button in self.number_buttons:
            button.config(bg="SystemButtonFace", disabledforeground="gray")

    def update_number_grid(self, number):
        index = number - 1  # Convertir el número a índice (0-89)
        self.number_buttons[index].config(bg="black", disabledforeground="white")  # Cambiar el color del botón al ser sorteado

    def speak_number(self, number):
        if number in self.special_numbers:
            full_number = self.special_numbers[number]
            digits = [int(digit) for digit in str(number)]
            words = [self.digit_to_word[digit] for digit in digits]
            self.engine.say(full_number)
            self.engine.say(" ".join(words))
        else:
            self.engine.say(str(number))
            digits = [int(digit) for digit in str(number)]
            words = [self.digit_to_word[digit] for digit in digits]
            self.engine.say(" ".join(words))

        self.engine.runAndWait()

    @property
    def digit_to_word(self):
        return {
            0: "cero",
            1: "uno",
            2: "dos",
            3: "tres",
            4: "cuatro",
            5: "cinco",
            6: "seis",
            7: "siete",
            8: "ocho",
            9: "nueve"
        }

    def clear_grid(self):
        respuesta = messagebox.askokcancel("REINICIAR", "¿Quiere reiniciar el sorteo?")
        if respuesta:
            self.numbers_drawn.clear()
            self.reset_number_grid()
            self.result_label.config(text="🙂")
            self.ultimos_numeros.clear()
            self.start_button.config(state=tk.NORMAL, text='COMENZAR')
            self.stop_button.config(state=tk.DISABLED, disabledforeground="gray90")
            self.clear_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()