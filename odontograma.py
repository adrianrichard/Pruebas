
#print('Hola mundo!!!')
from tkinter import *

ventana=Tk()
c=Canvas(ventana, width=500, height=500)
ventana.geometry("500x500")

for coord_x in range(0, 100, 10):
    for coord_y in range(0, 100, 10):
        print(coord_x, coord_y)
        c.delete()
        c.place(x=coord_x ,y=coord_y)
        c.create_rectangle(0,0,10,10,fill="blue", tags="playbutton")
        #c.create_polygon(0,50,25,25,50,50,fill="yellow")
        c.delete()
        
'''c.place(x=0,y=0)
c.create_rectangle(0,0,50,50,fill=color, tags="playbutton")
c.create_polygon(0,50,25,25,50,50,fill="yellow")
c.create_polygon(50,0,25,25,50,50,fill="red")
c.create_polygon(0,0,25,25,0,50,fill="green")
#c.create_polygon(0,0,50,50,25,50,fill="blue")
c.create_line(0,0,50,50)
c.create_line(50,0,0,50)
c.create_rectangle(15,15,35,35,fill="white")
'''



ventana.mainloop()
'''
from tkinter import *

ventana=Tk()

c=Canvas(ventana, width=500, height=500)
ventana.geometry("500x500")
color="gray"
c.place(x=0,y=0)
c.create_rectangle(0,0,50,50,fill=color, tags="playbutton")
c.create_polygon(0,50,25,25,50,50,fill="yellow")
c.create_polygon(50,0,25,25,50,50,fill="red")
c.create_polygon(0,0,25,25,0,50,fill="green")
#c.create_polygon(0,0,50,50,25,50,fill="blue")
c.create_line(0,0,50,50)
c.create_line(50,0,0,50)
c.create_rectangle(15,15,35,35,fill="white")

def clicked(*args):
    print("You clicked play!")
    color="purple"



c.tag_bind("playbutton","<Button-1>",clicked)

c.pack()

c1=Canvas(ventana, width=500, height=500)
c1.place(x=50,y=0)
c1.create_rectangle(0,0,50,50,fill="white")
c1.create_polygon(0,50,25,25,50,50,fill="yellow")
c1.create_polygon(50,0,25,25,50,50,fill="red")
c1.create_polygon(0,0,25,25,0,50,fill="green")
#c.create_polygon(0,0,50,50,25,50,fill="blue")
c1.create_line(0,0,50,50)
c1.create_line(50,0,0,50)
c1.create_rectangle(15,15,35,35,fill="white")
c1.create_rectangle(15,15,35,35,fill="red")
c2=Canvas(ventana, width=500, height=500)
c2.place(x=0,y=50)
c2.create_rectangle(0,0,50,50,fill="white")
c2.create_polygon(0,50,25,25,50,50,fill="yellow")
c2.create_polygon(50,0,25,25,50,50,fill="white")
c2.create_polygon(0,0,25,25,0,50,fill="green")
#c.create_polygon(0,0,50,50,25,50,fill="blue")
c2.create_line(0,0,50,50)
c2.create_line(50,0,0,50)
c2.create_rectangle(15,15,35,35,fill="white")
c2.create_rectangle(15,15,35,35,fill="red")
ventana.geometry("500x500")

ventana.mainloop()'''
'''
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
root = tk.Tk()
cal = DateEntry(root, width=12, year=2019, month=6, day=22,
background='darkblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)
root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

root = tk.Tk()
# change ttk theme to 'clam' to fix issue with downarrow button
style = ttk.Style(root)
style.theme_use('clam')

class MyDateEntry(DateEntry):
    def __init__(self, master=None, **kw):
        DateEntry.__init__(self, master=None, **kw)
        # add black border around drop-down calendar
        self._top_cal.configure(bg='black', bd=1)
        # add label displaying today's date below
        tk.Label(self._top_cal, bg='gray90', anchor='w',
                 text='Today: %s' % date.today().strftime('%x')).pack(fill='x')

# create the entry and configure the calendar colors
de = MyDateEntry(root, year=2016, month=9, day=6,
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
                 headersforeground='gray70')
de.pack()
root.mainloop()

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

root.mainloop()
'''