# -*- coding: iso-8859-1 -*-

from tkinter import *
#from Canvas import *
from tkinter.font import *
import os
import time
import calendar
import callib
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from PIL import ImageOps

import torah
import holidays
import preferences
import times
import locations
import notes
import zmanim
import customfonts
import customnames
from utils import *

def change_size(r):

  global yearCurrent
  global monthCurrent
  global cvwidth
  global cvheight

  cvwidth = r.width
  cvheight = r.height
  neu_zeichnen()
  root.update()

def neu_zeichnen():
  global yearCurrent
  global monthCurrent
  global dayCurrent
  global titlelinefont, subtitlelinefont, fontgregorian
  global fontjewish, fontholidays, fontshabbat, fontomer
  global fontweekdays, zmanimfont
  global dayrectangles
  global backImgOrg, backImgCanvas, backImgWidth, backImgHeight

  weekday, letzter_tag = calendar.monthrange(yearCurrent, monthCurrent);

  # Width of one cell
  breite = (int(cvwidth)-10) / 7
  # Clear the canvas
  cv.delete("all")

  if backImgWidth != cvwidth or backImgHeight != cvheight:
    backImgTemp = ImageOps.fit(backImgOrg, (cvwidth, cvheight))
    backImgCanvas = ImageTk.PhotoImage(backImgTemp)
    backImgWidth = cvwidth
    backImgHeight = cvheight
  cv.create_image(0, 0, image = backImgCanvas, anchor=NW)

  titelzeilenhoehe = titlelinefont.metrics("ascent") + titlelinefont.metrics("descent")
  untertitelzeilenhoehe = subtitlelinefont.metrics("ascent") + subtitlelinefont.metrics("descent")
  tagesnummernhoehe = fontgregorian.metrics("ascent") + fontgregorian.metrics("descent")

  titelzeile = customnames.getGregorianMonthName(monthCurrent) + " " + str(yearCurrent)

  # Calculating the jewish/gregorian start/end of the selected month
  julianisch = callib.gregorian_to_jd(yearCurrent, monthCurrent, 1)
  start_hebjahr, start_hebmonat, start_hebtag = callib.jd_to_hebrew(julianisch)
  julianisch = callib.gregorian_to_jd(yearCurrent, monthCurrent, letzter_tag)
  ende_hebjahr, ende_hebmonat, ende_hebtag = callib.jd_to_hebrew(julianisch)
  untertitelzeile = str(start_hebtag) + " " + customnames.getJewishMonthName(start_hebmonat, start_hebjahr) + " " + str(start_hebjahr) + " - " + str(ende_hebtag) + " " + customnames.getJewishMonthName(ende_hebmonat, ende_hebjahr) + " " + str(ende_hebjahr)

  cv.create_text(15, 5, anchor=NW, text=titelzeile, font=titlelinefont)
  cv.create_text(cvwidth - 15, 5, anchor=NE, justify=RIGHT, text=untertitelzeile, font=subtitlelinefont, fill="blue")

  # Weekdays
  weekdayname = customnames.getWeekdayName(0)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(1)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(2)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite*2+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(3)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite*3+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(4)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite*4+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(5)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite*5+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  weekdayname = customnames.getWeekdayName(6)
  textbreite = fontweekdays.measure(weekdayname)
  cv.create_text(5+breite*6+breite/2-textbreite/2, 5+titelzeilenhoehe, anchor=NW, text=weekdayname, font=fontweekdays)
  texthoehe = fontweekdays.metrics("ascent") + fontweekdays.metrics("descent")

  hoehe = (int(cvheight)-10-texthoehe-titelzeilenhoehe) / 6

  # Drawing rectangles
  tag = 1
  weekday = (weekday+1) % 7;

  aktuelle_spalte = weekday
  aktuelle_zeile = 0

  dayrectangles = []
  # Displaying day numbers
  for i in range(letzter_tag):
    if i+1 == dayCurrent:
      cv.create_rectangle(5+aktuelle_spalte*breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, 5+aktuelle_spalte*breite+breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe, fill='white')
    cv.create_rectangle(5+aktuelle_spalte*breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, 5+aktuelle_spalte*breite+breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe)
    # dayrectangles contains tuples of the form
    # (day number, left, top, right, bottom) - edge of the rectangle
    dayrectangles = dayrectangles + [(i+1, 5+aktuelle_spalte*breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, 5+aktuelle_spalte*breite+breite, 5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe)]
    for i in range(3):
      cv.create_line(5+aktuelle_spalte*breite, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe + i, \
		5+aktuelle_spalte*breite+breite-i, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe + i,
		fill="white")
      cv.create_line(5+aktuelle_spalte*breite+i, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, \
		5+aktuelle_spalte*breite+i, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe-i,
		fill="white")
      cv.create_line(5+aktuelle_spalte*breite+breite-i,\
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+i,\
		5+aktuelle_spalte*breite+breite-i,\
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe, \
		fill="darkgray")
      cv.create_line(5+aktuelle_spalte*breite+i, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe-i, \
		5+aktuelle_spalte*breite+breite, \
		5+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe+hoehe-i, \
		fill="darkgray")
    cv.create_text(7+aktuelle_spalte*breite, 7+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, anchor=NW, text=tag, font=fontgregorian)

    julianisch = callib.gregorian_to_jd(yearCurrent, monthCurrent, tag)
    hebjahr, hebmonat, hebtag = callib.jd_to_hebrew(julianisch)

    cv.create_text(2+aktuelle_spalte*breite+breite-3-fontjewish.measure(str(hebtag)), 7+titelzeilenhoehe+texthoehe+aktuelle_zeile*hoehe, anchor=NW, text=hebtag, fill="blue", font=fontjewish)

    holidaysToDisplay = ""

    # Calculating holidays and display them
    feiertag = holidays.berechne_feiertag(tag, monthCurrent, yearCurrent, calSettings.getDiaspora())
    if feiertag != None:
      for i in range(len(feiertag)):
        if holidaysToDisplay != "":
          holidaysToDisplay += "\n"
        holidaysToDisplay += feiertag[i]

    # Calculate torah readings and display them
    torahSections = torah.getTorahSections(hebmonat, hebtag, hebjahr, calSettings.getDiaspora)
    if torahSections != "":
      if holidaysToDisplay != "":
        holidaysToDisplay += "\n"
      holidaysToDisplay += torahSections



    cv.create_text(7+aktuelle_spalte*breite+breite/2,
                   7+titelzeilenhoehe+texthoehe+
                       aktuelle_zeile*hoehe+tagesnummernhoehe+20
                   ,
                   text=holidaysToDisplay, font=fontholidays,
                   width=breite-7, anchor=tkinter.CENTER,
                   justify=tkinter.CENTER, fill="blue")

    currentLocationName = calSettings.getCurrentLocationName()
    currentLocation = locations.getLocationData(currentLocationName)
    if holidays.getWeekdayOfHebrewDate(hebtag, hebmonat, hebjahr) == 5:
      shabbat = times.GetSunset(monthCurrent, tag, yearCurrent, currentLocation)
      if isDST(tag, monthCurrent, yearCurrent, calSettings):
        shabbat[0] += 1
      times.SubtractMinutes(shabbat, calSettings.getMinBeforeSunset())
      shabbatString = times.FormatTime(calSettings, shabbat)

      cv.create_text(7+aktuelle_spalte*breite+breite/2-fontshabbat.measure(shabbatString)/2,
                     7+titelzeilenhoehe+texthoehe+
                         aktuelle_zeile*hoehe
                     ,
                     text=shabbatString, font=fontshabbat,
                     width=breite-7, anchor=tkinter.NW, fill="red")
    elif holidays.getWeekdayOfHebrewDate(hebtag, hebmonat,  hebjahr) == 6:
      if(calSettings.getHavdalahMethod() == 0):
        havdalah = times.GetSunset(monthCurrent, tag, yearCurrent, currentLocation)
        if isDST(tag, monthCurrent, yearCurrent, calSettings):
          havdalah[0] += 1
        times.AddMinutes(havdalah, calSettings.getMinAfterSunset())
      else:
        havdalah = times.GetSunsetDegreesBelowHorizon(monthCurrent, tag, yearCurrent, \
						calSettings.getDegBelowHorizon(), \
						currentLocation)
        if isDST(tag, monthCurrent, yearCurrent, calSettings):
          havdalah[0] += 1
        times.AddMinutes(havdalah, calSettings.getPlusMinutes())
      shabbatString = times.FormatTime(calSettings, havdalah)

      cv.create_text(7+aktuelle_spalte*breite+breite/2-fontshabbat.measure(shabbatString)/2,
                     7+titelzeilenhoehe+texthoehe+
                         aktuelle_zeile*hoehe
                     ,
                     text=shabbatString, font=fontshabbat,
                     width=breite-7, anchor=tkinter.NW, fill="red")

    startOmerJulian = int(callib.hebrew_to_jd(hebjahr, 1, 16))
    endOmerJulian = int(callib.hebrew_to_jd(hebjahr, 3, 5))
    omerString = ""
    omerCount = int((julianisch-startOmerJulian)+1)
    if omerCount > 0 and omerCount <= 49:
      omerString = customnames.getOmerCount(omerCount)

    cv.create_text(7+aktuelle_spalte*breite+breite/2,
			7+titelzeilenhoehe+texthoehe+
			aktuelle_zeile*hoehe+tagesnummernhoehe*4,
			text=omerString, font=fontomer, width=breite-5,
			anchor=tkinter.CENTER, justify=tkinter.CENTER, fill="VioletRed")

    aktuelle_spalte = aktuelle_spalte+1
    if aktuelle_spalte % 7 == 0:
      aktuelle_zeile = aktuelle_zeile+1
      aktuelle_spalte = 0
    tag = tag + 1

  zmanimLeft = 5+2*breite
  zmanimTop = 5+titelzeilenhoehe+texthoehe+5*hoehe
  zmanimRight = 5+6*breite+breite
  zmanimBottom = 5+titelzeilenhoehe+texthoehe+5*hoehe+hoehe
  zmanimWidth = zmanimRight-zmanimLeft
  zmanimHeight = zmanimBottom-zmanimTop
  cv.create_rectangle(zmanimLeft, zmanimTop, zmanimRight, zmanimBottom)

  listZmanimForToday = zmanim.getZmanimForDay(calSettings, dayCurrent, \
					monthCurrent, yearCurrent)
  zmanTextHeight = zmanimfont.metrics("ascent") + zmanimfont.metrics("descent")
  zmanTimeWidth = zmanimfont.measure("XX:XXPM")
  zmanMaxNameWidth = 0
  for currentZmanim in listZmanimForToday:
    if zmanimfont.measure(currentZmanim[0]) > zmanMaxNameWidth:
      zmanMaxNameWidth = zmanimfont.measure(currentZmanim[0])
  x = 5+zmanimLeft
  y = 5+zmanimTop
  for currentZmanim in listZmanimForToday:
    zmanName = currentZmanim[0]
    zmanTime = currentZmanim[1]
    cv.create_text(x, y, anchor=tkinter.NW, \
		font=zmanimfont, \
		text=zmanName, fill="blue")
    cv.create_text(x + zmanMaxNameWidth+5, y, anchor=tkinter.NW, \
		font=zmanimfont, \
		text=zmanTime, fill="blue")
    y += zmanTextHeight
    if y + zmanTextHeight > zmanimBottom:
      x += zmanMaxNameWidth+5 + zmanTimeWidth + 10
      y = 5+zmanimTop


def mouseclick(event):
  global dayrectangles
  global dayCurrent

  for dayrectangle in dayrectangles:
    day, left, top, right, bottom = dayrectangle
    if event.x >= left and event.x <= right and event.y >= top and event.y <= bottom:
      dayCurrent = day
  neu_zeichnen()

def about():
  tkinter.messagebox.showinfo("About",
                        "der tog far Python\n" +
                        "Version 1.0\n\n" +
                        "Copyright (c) by David and Ulrich Greve (2005)\n\n" +
			"Website: http://www.tichnut.de/jewish/")

def quitmenu(a=None):
  root.destroy()

# Code for going to previous month
def prevmonth():
  global yearCurrent
  global monthCurrent
  global dayCurrent

  if monthCurrent == 1:
    yearCurrent = yearCurrent - 1
    monthCurrent = 12
  else:
    monthCurrent = monthCurrent - 1
  lastday = getLastDayOfGregorianMonth(monthCurrent, yearCurrent)
  if dayCurrent > lastday:
    dayCurrent = lastday
  neu_zeichnen()

# Code for going to next month
def nextmonth():
  global yearCurrent
  global monthCurrent
  global dayCurrent

  if monthCurrent == 12:
    yearCurrent = yearCurrent + 1
    monthCurrent = 1
  else:
    monthCurrent = monthCurrent + 1
  lastday = getLastDayOfGregorianMonth(monthCurrent, yearCurrent)
  if dayCurrent > lastday:
    dayCurrent = lastday
  neu_zeichnen()

def year():
  global yearCurrent

  eingabeJahr = int(entryYear.get())
  if eingabeJahr > 1583:
    if eingabeJahr < 3000:
      yearCurrent = eingabeJahr
      entryYear.configure(text=str(yearCurrent))
      neu_zeichnen()
    else:
      return 0
  else:
    return 0

def changeyear(event):
  year()

def initYear():
  global yearCurrent
  entryYear.configure(text=str(yearCurrent))

def init():
  global yearCurrent
  yearCurrent=int(time.strftime("%Y"))

def prevmonthevent(event):
  prevmonth()

def nextmonthevent(event):
  nextmonth()

def prefmenu():
  preferences.preferencesDialog(calSettings, root)
  neu_zeichnen()

def shabbatMenu():
  preferences.shabbatDialog(calSettings, root)
  neu_zeichnen()

def storeSettingsOnQuit(event):
  calSettings.storeSettings()

def generalNotesMenu():
  genNotes = notes.generalNotesDialog(root)

def dstMenu():
  dstDialog = preferences.daylightSavingTimesdialog(calSettings, root)
  neu_zeichnen()

def zmaimMenu():
  zmaDialog = preferences.zmanimDialog(calSettings, root)
  neu_zeichnen()

global yearCurrent
global backImgOrg, backImgWidth, backImgHeight

init()
root = Tk()
root.title("der tog far Python")

backImgOrg = Image.open("wallpaper.bmp")
backImgWidth = 0
backImgHeight = 0

calSettings = preferences.settings()
calSettings.loadSettings()

posx = 0
posy = 0
# Get Size of Screen
screenwidth, screenheight = root.wm_maxsize()
screenwidth  -= 5
screenheight -= 30
if os.name == "nt":
  screenheight -= 70
root.geometry("%dx%d+%d+%d" % (screenwidth, screenheight, posx, posy))

# Main Menu

menubar = Menu(root)

calendarmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

calendarMenu = menubar.add_cascade(label="Calendar", menu=calendarmenu)
calendarmenu.add_command(label="Preferences...", command=prefmenu)
calendarmenu.add_command(label="  Candle Lighting/Havdalah...", command=shabbatMenu)
calendarmenu.add_command(label="  DST Settings...", command=dstMenu)
calendarmenu.add_command(label="  Zmanim...", command=zmaimMenu)
calendarmenu.add_separator()
calendarmenu.add_command(label="General Notes", command=generalNotesMenu)
calendarmenu.add_separator()
calendarmenu.add_command(label="Quit", command=quitmenu, accelerator='Alt-Q')
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.config(menu=menubar)

# Caption Frame

caption = Frame(root)

dayCurrent = int(time.strftime("%d"))
monthCurrent = int(time.strftime("%m"))
yearCurrent = int(time.strftime("%Y"))

imgBackward = PhotoImage(file="backward.pnm")
buttonPrevMonth = Button(caption, command=prevmonth, bg = "gray", image=imgBackward)
buttonPrevMonth.pack(side=LEFT, padx=100)

entryYearVariable = StringVar()
entryYearVariable.set(str(time.strftime("%Y")))
entryYear = Entry(caption, textvariable=entryYearVariable, width="5")
entryYear.bind('<KeyPress-Return>', changeyear)
initYear()
entryYear.pack(side=LEFT, expand=0, padx=3)

imgSelect = PhotoImage(file="select.pnm")
buttonGo = Button(caption, command=year, bg = "gray", image=imgSelect)
buttonGo.pack(side=LEFT, expand=0, padx=3)

imgForward = PhotoImage(file="forward.pnm")
buttonNextMonth = Button(caption, command=nextmonth, bg = "gray", image=imgForward)
buttonNextMonth.pack(side=LEFT, padx=100)

caption.pack(fill=X)

titlelinefont, subtitlelinefont, fontgregorian, \
  fontjewish, fontholidays, fontshabbat, fontomer, \
  fontweekdays, zmanimfont = customfonts.create_fonts()

cv = Canvas(root)
cv.pack(fill=BOTH, expand=1)

# Shortcuts
cv.bind("<Configure>", change_size)
cv.bind('<Button-1>', mouseclick)
root.bind('<Destroy>', storeSettingsOnQuit)
root.bind('<Alt-q>', quitmenu)
root.bind('<Alt-Q>', quitmenu)

root.bind('<Right>', nextmonthevent)
root.bind('<Left>', prevmonthevent)

root.mainloop()
