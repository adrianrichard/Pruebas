from tkinter import *
from caldialog import *

class generalNotesDialog(CalDialog):
  def __init__(self, root):
    self.createDialog(root)

  def createDialog(self, root):
    self.dialog = self.createDialogWindow(root, "General Notes")

    frame = Frame(self.dialog)
    frame.pack()

    notes = self.loadGeneralNotes()

    self.textNotepad = Text(frame)
    self.textNotepad.delete('1.0', END)
    self.textNotepad.insert('1.0', notes)
    self.textNotepad.pack()

    okCancelFrame = Frame(frame)
    okCancelFrame.pack()

    buttonOK = Button(okCancelFrame, text="OK", command=self.okEvent)
    buttonOK.pack(side=LEFT, padx=10)

    buttonCancel = Button(okCancelFrame, text="Cancel", command=self.cancelEvent)
    buttonCancel.pack(side=LEFT, padx=10)

    self.execute(root, self.dialog, buttonOK)

  def okEvent(self):
    self.storeGeneralNotes()
    self.dialog.destroy()

  # Cancel Button was clicked
  def cancelEvent(self):
    self.dialog.destroy()

  def storeGeneralNotes(self):
    fp = open("gnotes.txt", "w")
    fp.write(self.textNotepad.get('1.0', END))
    fp.close()

  def loadGeneralNotes(self):
    try:
      fp = open("gnotes.txt", "r")
      stringToReturn = fp.read()
      fp.close()
      return stringToReturn
    except:
      return ""
