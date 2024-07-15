import tkinter as tk
import random
import pyttsx3

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo / Lotería")

        self.numbers_drawn = set()

        self.label = tk.Label(self.root, text="BINGO PARROQUIAL", font=("Helvetica", 14))
        self.label.grid(row=0, column=0, pady=5, columnspan=2)

        Frame_botones = tk.Frame(self.root)
        Frame_botones.grid(row=1, column=0, pady=5)

        self.start_button = tk.Button(Frame_botones, text="Empezar", command=self.start_draw)
        self.start_button.grid(row=0, column=0, pady=5)

        self.stop_button = tk.Button(Frame_botones, text="Detener", command=self.stop_draw, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=0, pady=5)

        self.clear_button = tk.Button(Frame_botones, text="Limpiar", command=self.clear_grid)
        self.clear_button.grid(row=2, column=0, pady=5)

        self.numero_sorteado_label = tk.Label(Frame_botones, text="Número sorteado", font=("Helvetica", 20))
        self.numero_sorteado_label.grid(row=3, column=0, pady=5)

        self.result_label = tk.Label(Frame_botones, text="", font=("Helvetica", 30))
        self.result_label.grid(row=4, column=0, pady=5)

        self.create_number_grid()

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 120)  # Velocidad de la voz

    def create_number_grid(self):
        self.number_buttons = []
        frame_numeros = tk.Frame(self.root)
        frame_numeros.grid(row=1, column=1, pady=5)

        for i in range(9):  # 9 filas
            for j in range(10):  # 10 columnas
                number = i * 10 + j + 1  # Calcular el número correspondiente
                button = tk.Button(frame_numeros, text=str(number), width=8, height=3, state=tk.DISABLED)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.number_buttons.append(button)

    def start_draw(self):
        self.numbers_drawn.clear()  # Reiniciamos los números sorteados
        self.reset_number_grid()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.DISABLED)

        self.draw_number()

    def stop_draw(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.NORMAL)
        self.root.after_cancel(self.draw_id)  # Detener el sorteo

    def draw_number(self):
        if len(self.numbers_drawn) < 90:
            while True:
                number = random.randint(1, 90)
                if number not in self.numbers_drawn:
                    self.numbers_drawn.add(number)
                    self.result_label.config(text=number)
                    self.update_number_grid(number)
                    self.speak_number(number)
                    break
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
        self.engine.say(str(number))
        self.engine.runAndWait()

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
