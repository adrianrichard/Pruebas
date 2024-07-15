import tkinter as tk
import random

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo / Lotería")

        self.numbers_drawn = set()

        self.label = tk.Label(self.root, text="Presiona Empezar para sortear números", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Empezar", command=self.start_draw)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_draw, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.create_number_grid()

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
        self.numbers_drawn.clear()  # Reiniciamos los números sorteados
        self.reset_number_grid()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.draw_number()

    def stop_draw(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def draw_number(self):
        if len(self.numbers_drawn) < 90:
            while True:
                number = random.randint(1, 90)
                if number not in self.numbers_drawn:
                    self.numbers_drawn.add(number)
                    self.result_label.config(text=f"Número sorteado: {number}")
                    self.update_number_grid(number)
                    break
            self.root.after(1000, self.draw_number)  # Llamada recursiva cada 1000ms (1 segundo)
        else:
            self.result_label.config(text="¡Todos los números han sido sorteados!")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)

    def reset_number_grid(self):
        for button in self.number_buttons:
            button.config(bg="SystemButtonFace")

    def update_number_grid(self, number):
        index = number - 1  # Convertir el número a índice (0-89)
        self.number_buttons[index].config(bg="green")  # Cambiar el color del botón al ser sorteado

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
