from tkinter import *
import sqlite3
import pyttsx3

# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

# window
class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
        # heading
        self.heading = Label(master, text="Bookings", font=('arial 60 bold'), fg='black', bg='pink')
        self.heading.place(x=370, y=0)

        # button to change bookings
        self.change = Button(master, text="Next Booking", width=30, height=2, bg='steelblue', command=self.func)
        self.change.place(x=500, y=700)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 150 bold'))
        self.n.place(x=500, y=300)

        self.pname = Label(master, text="", font=('arial 50 bold'))
        self.pname.place(x=500, y=200)
    # function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Booking number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
