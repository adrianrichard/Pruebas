from tkinter.font import *
import os

def create_fonts():
  # Set the fonts

  addsize = 0

  if os.name == "nt":
    addsize = 0
  elif os.name == "posix":
    addsize = 10

  titlelinefont = Font(family="Helvetica", size=18+addsize)
  subtitlelinefont = Font(family="Helvetica", size=18+addsize)
  fontgregorian = Font(family="Helvetica", size=10+addsize)
  fontjewish = Font(family="Helvetica", size=9+addsize)
  fontholidays = Font(family="Helvetica", size=9+addsize)
  fontshabbat = Font(family="Helvetica", size=9+addsize)
  fontomer = Font(family="Helvetica", size=9+addsize)
  fontweekdays = Font(family="Helvetica", size=9+addsize)
  zmanimfont = Font(family="Helvetica", size=9+addsize)

  return (titlelinefont, subtitlelinefont, fontgregorian, \
         fontjewish, fontholidays, fontshabbat, fontomer, \
         fontweekdays, zmanimfont)
