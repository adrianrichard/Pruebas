import tkinter as tk
import random
import pyttsx3

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo / Lotería")

        self.numbers_drawn = []  # Cambiado a lista para mantener el orden de los números sorteados

        self.label = tk.Label(self.root, text="Presiona Empezar para sortear números", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Empezar", command=self.start_draw)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_draw, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.clear_button = tk.Button(self.root, text="Limpiar", command=self.clear_grid)
        self.clear_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.create_number_grid()

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Velocidad de la voz

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

    def create_number_grid(self):
        self.number_buttons = []
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        for i in range(9):  # 9 filas
            for j in range(10):  # 10 columnas
                number = i * 10 + j + 1  # Calcular el número correspondiente
                button = tk.Button(frame, text=str(number), width=4, height=2, state=tk.DISABLED)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.number_buttons.append(button)

    def start_draw(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.DISABLED)

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

            self.numbers_drawn.append(number)
            self.result_label.config(text=f"Número sorteado: {number}")
            self.update_number_grid(number)
            self.speak_number(number)

            self.draw_id = self.root.after(1000, self.draw_number)  # Llamada recursiva cada 1000ms (1 segundo)
        else:
            self.result_label.config(text="¡Todos los números han sido sorteados!")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.clear_button.config(state=tk.NORMAL)

    def reset_number_grid(self):
        for button in self.number_buttons:
            button.config(bg="SystemButtonFace")

    def update_number_grid(self, number):
        index = number - 1  # Convertir el número a índice (0-89)
        self.number_buttons[index].config(bg="green")  # Cambiar el color del botón al ser sorteado

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
        self.numbers_drawn.clear()
        self.reset_number_grid()
        self.result_label.config(text="Presiona Empezar para sortear números")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
