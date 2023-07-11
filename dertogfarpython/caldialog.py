from tkinter import *

class CalDialog:
  def createDialogWindow(self, root, caption):
    dialog = Toplevel(root)
    dialog.title(caption)
    return dialog

  def execute(self, root, dialog, focusWidget):
    focusWidget.focus_set()
    dialog.grab_set()
    root.wait_window(dialog)
    root.grab_set()
