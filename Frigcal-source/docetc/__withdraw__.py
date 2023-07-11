#!/usr/bin/python3
"""
============================================================================
[1.6] Supplemental example only (NOT USED by frigcal).
Demo the difference between iconify()/withdraw() on Linux and Windows.
On Linux, scripts must use withdraw() to get windows back with deiconify().
On Windows, either works, but withdraw() window doesn't appear in taskbar.
Linux also doesn't trigger <Unmap>/<Map> or <Configure> on minimize/restore.
============================================================================
"""
from tkinter import *
import time, sys

root = Tk()
Label(root, text='root', font='times 20 bold', height=5, width=15).pack()

dialog1 = Toplevel(root)
Label(dialog1, text='popup-iconify', font='times 20 bold', height=5, width=15).pack()

dialog2 = Toplevel(root)
Label(dialog2, text='popup-withdraw', font='times 20 bold', height=5, width=15).pack()

root.after(2000, lambda: (dialog1.iconify(),      # <=doesn't restore on Linux
                          dialog2.withdraw(),     # <=not in taskbar on Windows
                          print('minimized')))    # both calls remove the popups

root.after(7000, lambda: (dialog1.deiconify(),    # dialog1 doesn't return on Linux
                          dialog2.deiconify(),    # both return on Windows 
                          print('maximized')))    # only dialog2 reappers on Linux

root.mainloop()

