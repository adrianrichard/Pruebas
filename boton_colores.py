import tkinter as tk
window = tk.Tk()
btn = tk.Button(window, text='Button')
btn.pack(padx=10, pady=10)
rainbow_colors = ['red','purple','yellow','orange','blue',
                  'lightblue','green','black']
color_iterator = iter(rainbow_colors)
def ButtonUpdate():
    try:
        color = next(color_iterator)
        btn.config(bg=color)
    except StopIteration:
        return
    window.after(500, ButtonUpdate)
ButtonUpdate()
window.mainloop()