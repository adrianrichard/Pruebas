#!/usr/bin/python3
"""
===================================================================
[1.4] Simulate minimize/maximize association.
NOT USED by frigcal: supplemental example only.
Minimize/restore on main window is propagated to popup window.
See frigcal.py's onMonthHide/onMonthUnhide for full details.
PP4E here means Programming Python 4th Ed (source of some code).

[1.6] This doesn't work on Linux, as <Map>/<Unmap> don't fire!
Even if they did, need to withdraw(), not iconify(), on Linux.
===================================================================
"""
from tkinter import *

root1 = Tk()            # month window: main
root2 = Toplevel()      # image window: dependent

def tandemhide(E):
    root1.iconify()                           # PLUS--check E.widget==root1!
    if root2: root2.iconify()                 # PP4E: page 424, 667, etc.
    
def tandemunhide(E):
    if root2: root2.deiconify()
    root1.deiconify()

def eraser():
    global root2
    root2.destroy()
    root2 = None
    
root1.bind('<Unmap>', tandemhide)             # PP4E: page 447 (brief)
root1.bind('<Map>',   tandemunhide)

root2.protocol('WM_DELETE_WINDOW', eraser)    # PP4E: page 393, 423 etc.

Label(root1, text='Main Window',  font=('courier', 50, 'bold')).pack()
Label(root2, text='Popup Window', font=('courier', 25, 'bold')).pack()
mainloop()

 
