from tkinter import *
from caldialog import *
import tkinter.font
import Pmw
import locations

import locations

class settings:
  def __init__(self):
    pass

  def storeSettings(self):
    iniFileName = "settings.ini"
    fp = open(iniFileName, "w")
    fp.write("diaspora->" + str(self.diaspora) + "\n")
    fp.write("timeformat->" + str(self.timeformat) + "\n")
    fp.write("currentLocationName->" + self.currentLocationName + "\n")
    fp.write("minBeforeSunset->" + str(self.minBeforeSunset) + "\n")
    fp.write("havdalahMethod->" + str(self.havdalahMethod) + "\n")
    fp.write("minAfterSunset->" + str(self.minAfterSunset) + "\n")
    fp.write("degBelowHorizon->" + str(self.degBelowHorizon) + "\n")
    fp.write("plusMinutes->" + str(self.plusMinutes) + "\n")
    fp.write("dstMethod->" + str(self.dstMethod) + "\n")
    fp.write("startTimeCommon->" + str(self.startTimeCommon) + "\n")
    fp.write("startWeekdayCommon->" + str(self.startWeekdayCommon) + "\n")
    fp.write("startMonthCommon->" + str(self.startMonthCommon) + "\n")
    fp.write("endTimeCommon->" + str(self.endTimeCommon) + "\n")
    fp.write("endWeekdayCommon->" + str(self.endWeekdayCommon) + "\n")
    fp.write("endMonthCommon->" + str(self.endMonthCommon) + "\n")
    fp.write("startTimeIsraeli->" + str(self.startTimeIsraeli) + "\n")
    fp.write("startWeekdayIsraeli->" + str(self.startWeekdayIsraeli) + "\n")
    fp.write("startDayIsraeli->" + str(self.startDayIsraeli) + "\n")
    fp.write("startMonthIsraeli->" + str(self.startMonthIsraeli) + "\n")
    fp.write("endWeekdayIsraeli->" + str(self.endWeekdayIsraeli) + "\n")
    fp.write("alotHashachar->" + str(self.alotHashachar) + "\n")
    fp.write("earliestTallit->" + str(self.earliestTallit) + "\n")
    fp.write("kriatShema->" + str(self.kriatShema) + "\n")
    fp.write("tefila->" + str(self.tefila) + "\n")
    fp.write("chatzot->" + str(self.chatzot) + "\n")
    fp.write("minchaGedola->" + str(self.minchaGedola) + "\n")
    fp.write("minchaKtana->" + str(self.minchaKtana) + "\n")
    fp.write("plagHaMincha->" + str(self.plagHaMincha) + "\n")
    fp.write("tzaitHakochavim->" + str(self.tzaitHakochavim))
    fp.close()

  def loadSettings(self):
    ini = {}
    try:
      iniFileName = "settings.ini"
      fp = open(iniFileName)
      lines = fp.readlines()
      for line in lines:
        values = line.split("->")
        if len(values) == 2:
          parameter = values[0].strip()
          value = values[1].strip()
          ini[parameter] = value
      fp.close()
    except:
      ini = {}
      ini["diaspora"] = "1"
      ini["timeformat"] = "12"
      ini["currentLocationName"] = "Pforzheim"
      ini["minBeforeSunset"] = 18
      ini["havdalahMethod"] = 0
      ini["minAfterSunset"] = 60
      ini["degBelowHorizon"] = 6.5
      ini["plusMinutes"] = 30
      ini["dstMethod"] = 0 # Common
      ini["startTimeCommon"] = 1
      ini["startWeekdayCommon"] = 1
      ini["startMonthCommon"] = 1
      ini["endTimeCommon"] = 1
      ini["endWeekdayCommon"] = 0
      ini["endMonthCommon"] = 1
      ini["startTimeIsraeli"] = 1
      ini["startWeekdayIsraeli"] = 1
      ini["startDayIsraeli"] = 1
      ini["startMonthIsraeli"] = 1
      ini["endWeekdayIsraeli"] = 0
      ini["alotHashachar"] = "16Deg"
      ini["earliestTallit"] = "11Deg"
      ini["kriatShema"] = "GRO"
      ini["tefila"] = "GRO"
      ini["chatzot"] = "GRO"
      ini["minchaGedolah"] = "GRO"
      ini["minchaKtana"] = "GRO"
      ini["plagHaMincha"] = "GRO"
      ini["tzaitHakochavim"] = "8.5deg"

    self.diaspora = int(ini["diaspora"])
    self.timeformat = int(ini["timeformat"])
    self.currentLocationName = ini["currentLocationName"]
    self.minBeforeSunset = int(ini["minBeforeSunset"])
    self.havdalahMethod = int(ini["havdalahMethod"])
    self.minAfterSunset = int(ini["minAfterSunset"])
    self.degBelowHorizon = float(ini["degBelowHorizon"])
    self.plusMinutes = int(ini["plusMinutes"])
    self.dstMethod = int(ini["dstMethod"])
    self.startTimeCommon = int(ini["startTimeCommon"])
    self.startWeekdayCommon = int(ini["startWeekdayCommon"])
    self.startMonthCommon = int(ini["startMonthCommon"])
    self.endTimeCommon = int(ini["endTimeCommon"])
    self.endWeekdayCommon = int(ini["endWeekdayCommon"])
    self.endMonthCommon = int(ini["endMonthCommon"])
    self.startTimeIsraeli = int(ini["startTimeIsraeli"])
    self.startWeekdayIsraeli = int(ini["startWeekdayIsraeli"])
    self.startDayIsraeli = int(ini["startDayIsraeli"])
    self.startMonthIsraeli = int(ini["startMonthIsraeli"])
    self.endWeekdayIsraeli = int(ini["endWeekdayIsraeli"])
    self.alotHashachar = ini["alotHashachar"]
    self.earliestTallit = ini["earliestTallit"]
    self.kriatShema = ini["kriatShema"]
    self.tefila = ini["tefila"]
    self.chatzot = ini["chatzot"]
    self.minchaGedola = ini["minchaGedola"]
    self.minchaKtana = ini["minchaKtana"]
    self.plagHaMincha = ini["plagHaMincha"]
    self.tzaitHakochavim = ini["tzaitHakochavim"]

  # Diaspora/Israel
  def getDiaspora(self):
    if(self.diaspora == 0):
      return False
    else:
      return True

  def setDiaspora(self, diasporaVal):
    if diasporaVal == True:
      self.diaspora = 1
    else:
      self.diaspora = 0

  # Time format
  def getTimeFormat(self):
    return self.timeformat

  def setTimeFormat(self, timeformat):
    self.timeformat = timeformat

  # Current location name
  def getCurrentLocationName(self):
    return self.currentLocationName

  def setCurrentLocationName(self, locationName):
    self.currentLocationName = locationName

  # Minutes before sunset

  def setMinBeforeSunset(self, min):
    self.minBeforeSunset = min

  def getMinBeforeSunset(self):
    return self.minBeforeSunset

  # Havdalah method

  def getHavdalahMethod(self):
    return self.havdalahMethod

  def setHavdalahMethod(self, flag):
    self.havdalahMethod = flag

  # Minutes after sunset

  def getMinAfterSunset(self):
    return self.minAfterSunset

  def setMinAfterSunset(self, min):
    self.minAfterSunset = min

  # Degrees below horizon ...

  def getDegBelowHorizon(self):
    return self.degBelowHorizon

  def setDegBelowHorizon(self, deg):
    self.degBelowHorizon = deg

  # ... + ? minutes

  def getPlusMinutes(self):
    return self.plusMinutes

  def setPlusMinutes(self, min):
    self.plusMinutes = min

  # Daylight savings time settings

  def getDSTMethod(self):
    return self.dstMethod

  def setDSTMethod(self, method):
    self.dstMethod = method

  # First, 2nd, ...

  def getStartTimeCommon(self):
    return self.startTimeCommon

  def setStartTimeCommon(self, time):
    self.startTimeCommon = time

  # Start weekday for common method

  def getStartWeekdayCommon(self):
    return self.startWeekdayCommon

  def setStartWeekdayCommon(self, weekday):
    self.startWeekdayCommon = weekday

  # Start month for common method

  def getStartMonthCommon(self):
    return self.startMonthCommon

  def setStartMonthCommon(self, month):
    self.startMonthCommon = month

  # First, 2nd, ...

  def getEndTimeCommon(self):
    return self.endTimeCommon

  def setEndTimeCommon(self, time):
    self.endTimeCommon = time

  # End weekday for common method

  def getEndWeekdayCommon(self):
    return self.endWeekdayCommon

  def setEndWeekdayCommon(self, weekday):
    self.endWeekdayCommon = weekday

  # End month for common method

  def getEndMonthCommon(self):
    return self.endMonthCommon

  def setEndMonthCommon(self, month):
    self.endMonthCommon = month

# ---------- Israeli method ----------

  # First, 2nd, ...

  def getStartTimeIsraeli(self):
    return self.startTimeIsraeli

  def setStartTimeIsraeli(self, time):
    self.startTimeIsraeli = time

  # Start Weekday

  def getStartWeekdayIsraeli(self):
    return self.startWeekdayIsraeli

  def setStartWeekdayIsraeli(self, weekday):
    self.startWeekdayIsraeli = weekday

  # Start Day

  def getStartDayIsraeli(self):
    return self.startDayIsraeli

  def setStartDayIsraeli(self, day):
    self.startDayIsraeli = day

  # Start Month

  def getStartMonthIsraeli(self):
    return self.startMonthIsraeli

  def setStartMonthIsraeli(self, day):
    self.startMonthIsraeli = day

  # End Weekday

  def getEndWeekdayIsraeli(self):
    return self.endWeekdayIsraeli

  def setEndWeekdayIsraeli(self, day):
    self.endWeekdayIsraeli = day

  # -------- ZMANIM ---------

  # Alot Hashachar

  def getAlotHashachar(self):
    return self.alotHashachar

  def setAlotHashachar(self, flag):
    self.alotHashachar = flag

  # Earliest Tallit

  def getEarliestTallit(self):
    return self.earliestTallit

  def setEarliestTallit(self, flag):
    self.earliestTallit = flag

  # Kriat Shema

  def getKriatShema(self):
    return self.kriatShema

  def setKriatShema(self, flag):
    self.kriatShema = flag

  # Tefila

  def getTefila(self):
    return self.tefila

  def setTefila(self, flag):
    self.tefila = flag

  # Chatzot

  def getChatzot(self):
    return self.chatzot

  def setChatzot(self, flag):
    self.chatzot = flag

  # Mincha Gedola

  def getMinchaGedola(self):
    return self.minchaGedola

  def setMinchaGedola(self, flag):
    self.minchaGedola = flag

  # Mincha K'tana

  def getMinchaKtana(self):
    return self.minchaKtana

  def setMinchaKtana(self, flag):
    self.minchaKtana = flag

  # Plag Ha Mincha

  def getPlagHaMincha(self):
    return self.plagHaMincha

  def setPlagHaMincha(self, flag):
    self.plagHaMincha = flag

  # Tzait Hakochavim

  def getTzaitHakochavim(self):
    return self.tzaitHakochavim

  def setTzaitHakochavim(self, flag):
    self.tzaitHakochavim = flag

# --------- DIALOGS -----------

class preferencesDialog(CalDialog):
  def __init__(self, calSettings, root):
    self.calSettings = calSettings
    self.createDialog(root)

  def getIndexFromString(self, array, str):
    for i in range(len(array)):
      if array[i] == str:
        return i

  def createDialog(self, root):
    self.dialog = self.createDialogWindow(root, "Preferences")

    frame = Frame(self.dialog)
    frame.pack()

    # Diaspora - Israel

    frameDiasporaIsrael = Frame(frame)
    frameDiasporaIsrael.pack()

    self.diasporaIsraelSel = IntVar()
    if not self.calSettings.getDiaspora():
      self.diasporaIsraelSel.set(0)
    else:
      self.diasporaIsraelSel.set(1)

    diaspora = Radiobutton(frameDiasporaIsrael, text="Diaspora", variable=self.diasporaIsraelSel, value=1)
    diaspora.pack(side=LEFT, padx=10)

    israel = Radiobutton(frameDiasporaIsrael, text="Israel", variable=self.diasporaIsraelSel, value=0)
    israel.pack(side=LEFT, padx=10)

    frameSpace0 = Frame(frame)
    frameSpace0.pack()
    labelSpace0 = Label(frameSpace0, text="")
    labelSpace0.pack()

    frameTimeFormat = Frame(frame)
    frameTimeFormat.pack()

    self.timeFormatSel = IntVar()
    self.timeFormatSel.set(self.calSettings.getTimeFormat())

    timeformat12 = Radiobutton(frameTimeFormat, text="12 hour (AM/PM)", variable=self.timeFormatSel, value=12)
    timeformat12.pack(side=LEFT, padx=10)

    timeformat24 = Radiobutton(frameTimeFormat, text="24 hour", variable=self.timeFormatSel, value=24)
    timeformat24.pack(side=LEFT, padx=10)

    frameSpace1 = Frame(frame)
    frameSpace1.pack()
    labelSpace1 = Label(frameSpace1, text="")
    labelSpace1.pack()

    # Location list
    frameLocationList = Frame(frame)
    vscroll = Scrollbar(frameLocationList)
    vscroll.pack(side=RIGHT, fill=Y)
    self.listLocations = Listbox(frameLocationList, yscrollcommand=vscroll.set)
    for town in locations.getLocationList():
      self.listLocations.insert(END, town)
    self.listLocations.pack(side=LEFT, fill=BOTH)
    self.listLocations.selection_clear(0, END)
    indexToSelect = self.getIndexFromString(locations.getLocationList(), self.calSettings.getCurrentLocationName())
    self.listLocations.selection_set(first=indexToSelect)
    self.listLocations.see(indexToSelect)
    vscroll.config(command=self.listLocations.yview)
    frameLocationList.pack()

    # OK or cancel?

    frameButtons = Frame(frame)
    frameButtons.pack()

    buttonOK = Button(frameButtons, text="OK", command=self.okEvent)
    buttonOK.pack(side=LEFT, padx=10)

    buttonCancel = Button(frameButtons, text="Cancel", command=self.cancelEvent)
    buttonCancel.pack(side=LEFT, padx=10)

    frameSpace2 = Frame(frame)
    frameSpace2.pack()
    labelSpace2 = Label(frameSpace2, text="")
    labelSpace2.pack()

    self.execute(root, self.dialog, buttonOK)

  # OK Button was clicked
  def okEvent(self):
    self.calSettings.setDiaspora(self.diasporaIsraelSel.get())
    self.calSettings.setTimeFormat(self.timeFormatSel.get())
    self.calSettings.setCurrentLocationName(self.listLocations.get(self.listLocations.curselection()))
    self.dialog.destroy()

  # Cancel Button was clicked
  def cancelEvent(self):
    self.dialog.destroy()

# Preferences for Candle Lighting/Havdalah
class shabbatDialog(CalDialog):
  def __init__(self, calSettings, root):
    self.calSettings = calSettings
    self.createDialog(root)
  def createDialog(self, root):
    self.dialog = self.createDialogWindow(root, "Candle Lighting/Havdalah")

    frame = Frame(self.dialog)
    frame.pack()

    labelCandleLighting = Label(frame, text="Candle lighting:")
    labelCandleLighting.pack()

    # Frame for Candle Lighting

    frameCandleLightingSettings = Frame(frame)
    frameCandleLightingSettings.pack()

    self.entryMinutesBeforeSunset = Entry(frameCandleLightingSettings, width=3, text=self.calSettings.getMinBeforeSunset())
    self.entryMinutesBeforeSunset.delete(0, END)
    self.entryMinutesBeforeSunset.insert(0, self.calSettings.getMinBeforeSunset())
    self.entryMinutesBeforeSunset.pack(side=LEFT, fill=Y)

    stringMin = " minutes before sunset"
    labelMinutesBeforeSunset = Label(frameCandleLightingSettings, text=stringMin)
    labelMinutesBeforeSunset.pack(side=LEFT, fill=BOTH)

    labelHavdalah = Label(frame, text="Havdalah:")
    labelHavdalah.pack()

    # Frame for Havdalah

    frameHavdalah = Frame(frame)
    frameHavdalah.pack()

    self.varOptionMinDeg = IntVar()
    if self.calSettings.getHavdalahMethod() == 0:
      self.varOptionMinDeg.set(0)
    else:
      self.varOptionMinDeg.set(1)

    frameHavdalahMinAfterSunset = Frame(frameHavdalah)
    frameHavdalahMinAfterSunset.pack()

    radioMinAfterSunset = Radiobutton(frameHavdalahMinAfterSunset, \
		variable=self.varOptionMinDeg, value=0)
    radioMinAfterSunset.grid(row=0)

    self.entryMinAfterSunset = Entry(frameHavdalahMinAfterSunset, width=3)
    self.entryMinAfterSunset.delete(0, END)
    self.entryMinAfterSunset.insert(0, self.calSettings.getMinAfterSunset())
    self.entryMinAfterSunset.grid(row=0, column=1)

    labelMinAfterSunset = Label(frameHavdalahMinAfterSunset, text="minutes after sunset")
    labelMinAfterSunset.grid(row=0, column=2)

    frameDegBelowHorizon = Frame(frameHavdalah)
    frameDegBelowHorizon.pack()

    radioDegBelowHorizon = Radiobutton(frameDegBelowHorizon, \
		variable=self.varOptionMinDeg, value=1)
    radioDegBelowHorizon.grid(row=0)

    self.entryDegBelowHorizon = Entry(frameDegBelowHorizon, width=5)
    self.entryDegBelowHorizon.delete(0, END)
    self.entryDegBelowHorizon.insert(0, self.calSettings.getDegBelowHorizon())
    self.entryDegBelowHorizon.grid(row=0, column=1)

    labelDegBelowHorizon = Label(frameDegBelowHorizon, text="degrees below horizon + ")
    labelDegBelowHorizon.grid(row=0, column=2)

    self.entryPlusMinutes = Entry(frameDegBelowHorizon, width=3)
    self.entryPlusMinutes.delete(0, END)
    self.entryPlusMinutes.insert(0, self.calSettings.getPlusMinutes())
    self.entryPlusMinutes.grid(row=0, column=3)

    labelPlusMinutes = Label(frameDegBelowHorizon, text="minutes")
    labelPlusMinutes.grid(row=0, column=4)

    okCancelFrame = Frame(frame)
    okCancelFrame.pack()

    buttonOK = Button(okCancelFrame, text="OK", command=self.okEvent)
    buttonOK.pack(side=LEFT, padx=10)

    buttonCancel = Button(okCancelFrame, text="Cancel", command=self.cancelEvent)
    buttonCancel.pack(side=LEFT, padx=10)

    self.execute(root, self.dialog, buttonOK)

  # OK Button was clicked
  def okEvent(self):
    self.calSettings.setMinBeforeSunset(int(self.entryMinutesBeforeSunset.get()))
    self.calSettings.setHavdalahMethod(self.varOptionMinDeg.get())
    self.calSettings.setMinAfterSunset(int(self.entryMinAfterSunset.get()))
    self.calSettings.setDegBelowHorizon(float(self.entryDegBelowHorizon.get()))
    self.calSettings.setPlusMinutes(int(self.entryPlusMinutes.get()))
    self.dialog.destroy()

 # Cancel Button was clicked
  def cancelEvent(self):
    self.dialog.destroy()

class daylightSavingTimesdialog(CalDialog):
  def __init__(self, calSettings, root):
    self.calSettings = calSettings
    self.createDialog(root)

  def getIndexFromString(self, array, str):
    for i in range(len(array)):
      if array[i] == str:
        return i

  def helperGetEntryWidth(self, stringlist):
    width = 0
    for item in stringlist:
      if len(item) > width:
        width = len(item)
    return width + 2

  def selectBeforeAfter(self):
    self.entryAfterBeforeIsraeli.config(state=NORMAL)
    self.entryAfterBeforeIsraeli.delete(0, END)

    index = self.getIndexFromString(self.listComboIsraeli1, self.comboIsraeli1.get())
    if index == 0:
      self.entryAfterBeforeIsraeli.insert(0, "after")
    elif index == 1:
      self.entryAfterBeforeIsraeli.insert(0, "before")
    self.entryAfterBeforeIsraeli.config(state=DISABLED)

  def eventSelected(self, a):
    self.selectBeforeAfter()

  def createDialog(self, root):
    self.dialog = self.createDialogWindow(root, "DST Settings")

    frame = Frame(self.dialog)
    frame.pack()

    frameMethods = Frame(frame)
    frameMethods.pack()

    self.varCommonIsraeli = IntVar()
    if self.calSettings.getDSTMethod() == 0:
      self.varCommonIsraeli.set(0)
    elif self.calSettings.getDSTMethod() == 1:
      self.varCommonIsraeli.set(1)
    else:
      self.varCommonIsraeli.set(2)

    # Common method

    radioCommon = Radiobutton(frameMethods, text="Common method", \
		variable=self.varCommonIsraeli, value=0)
    radioCommon.pack()

    frameCommon = Frame(frameMethods)
    frameCommon.pack()

    labelStart = Label(frameCommon, text="Start: ")
    labelStart.grid(row=0)

    labelStartFont = tkinter.font.Font()
    labelStartFont.name = labelStart["font"]
    itemHeight = labelStartFont.metrics("linespace") + \
                 labelStartFont.metrics("linespace")/3

    self.listComboCommon1 = ("1st", "2nd", "3rd", "4th", "Last")
    self.comboCommon1 = Pmw.ComboBox(frameCommon,
                                     entry_width=self.helperGetEntryWidth(self.listComboCommon1),
                                     listheight=itemHeight*len(self.listComboCommon1),
                                     scrolledlist_items=self.listComboCommon1)
    self.comboCommon1.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartTimeCommon()
    self.comboCommon1.selectitem(self.listComboCommon1[index])
    self.comboCommon1.grid(row=0, column=1)

    self.listWeekdays = ("Sunday", "Monday", "Tuesday", \
				"Wednesday", "Thursday", "Friday", "Saturday")
    self.comboStartWeekdayCommon = Pmw.ComboBox(frameCommon, \
		entry_width=self.helperGetEntryWidth(self.listWeekdays), \
		listheight = itemHeight*len(self.listWeekdays), \
		scrolledlist_items=self.listWeekdays)
    self.comboStartWeekdayCommon.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartWeekdayCommon()
    self.comboStartWeekdayCommon.selectitem(self.listWeekdays[index])
    self.comboStartWeekdayCommon.grid(row=0, column=2)

    labelIn = Label(frameCommon, text="in")
    labelIn.grid(row=0, column=3)

    self.months = ("January", "February", "March", "April", "May", "June", \
		"July", "August", "September", "October", "November", \
		"December")
    self.comboMonths = Pmw.ComboBox(frameCommon,
		entry_width=self.helperGetEntryWidth(self.months), \
		listheight = itemHeight*len(self.months), \
		scrolledlist_items=self.months)
    self.comboMonths.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartMonthCommon()
    self.comboMonths.selectitem(self.months[index])
    self.comboMonths.grid(row=0, column=4)

    # ---------------------- End Method ------------------------

    labelEnd = Label(frameCommon, text="End: ")
    labelEnd.grid(row=1)

    self.comboCommon2 = Pmw.ComboBox(frameCommon, \
		entry_width=self.helperGetEntryWidth(self.listComboCommon1), \
		listheight = itemHeight*len(self.listComboCommon1), \
		scrolledlist_items=self.listComboCommon1)
    self.comboCommon2.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getEndTimeCommon()
    self.comboCommon2.selectitem(self.listComboCommon1[index])
    self.comboCommon2.grid(row=1, column=1)

    self.comboEndWeekday = Pmw.ComboBox(frameCommon, \
		entry_width=self.helperGetEntryWidth(self.listWeekdays), \
		listheight = itemHeight*len(self.listWeekdays), \
		scrolledlist_items=self.listWeekdays)
    self.comboEndWeekday.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getEndWeekdayCommon()
    self.comboEndWeekday.selectitem(self.listWeekdays[index])
    self.comboEndWeekday.grid(row=1, column=2)

    labelIn = Label(frameCommon, text="in")
    labelIn.grid(row=1, column=3)

    self.comboMonthsEnd = Pmw.ComboBox(frameCommon, \
		entry_width=self.helperGetEntryWidth(self.months), \
		listheight = itemHeight*len(self.months), \
		scrolledlist_items=self.months)
    self.comboMonthsEnd.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getEndMonthCommon()
    self.comboMonthsEnd.selectitem(self.months[index])
    self.comboMonthsEnd.grid(row=1, column=4)

    # Israeli method

    radioIsraeli = Radiobutton(frameMethods, text="Israeli method", \
		variable=self.varCommonIsraeli, value=1)
    radioIsraeli.pack()

    frameIsraeli = Frame(frameMethods)
    frameIsraeli.pack()

    labelStart = Label(frameIsraeli, text="Start: ")
    labelStart.grid(row=0)

    self.listComboIsraeli1 = ("First", "Last")
    self.comboIsraeli1 = Pmw.ComboBox(frameIsraeli, \
		entry_width=self.helperGetEntryWidth(self.listComboIsraeli1), \
		listheight = itemHeight*len(self.listComboIsraeli1), \
		scrolledlist_items=self.listComboIsraeli1, \
		selectioncommand=self.eventSelected)
    self.comboIsraeli1.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartTimeIsraeli()
    self.comboIsraeli1.selectitem(self.listComboIsraeli1[index])
    self.comboIsraeli1.grid(row=0, column=1)

    self.comboStartWeekdayIsraeli = Pmw.ComboBox(frameIsraeli, \
		entry_width=self.helperGetEntryWidth(self.listWeekdays), \
		listheight = itemHeight*len(self.listWeekdays), \
		scrolledlist_items=self.listWeekdays)
    self.comboStartWeekdayIsraeli.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartWeekdayIsraeli()
    self.comboStartWeekdayIsraeli.selectitem(self.listWeekdays[index])
    self.comboStartWeekdayIsraeli.grid(row=0, column=2)

    self.entryAfterBeforeIsraeli = Entry(frameIsraeli)
    self.entryAfterBeforeIsraeli.insert(0, "after")
    self.entryAfterBeforeIsraeli.config(state=DISABLED, width=7)
    self.entryAfterBeforeIsraeli.grid(row=0, column=3)

    self.days = []
    for i in range(1, 32):
      self.days.append(str(i))
    self.comboDaysIsraeli = Pmw.ComboBox(frameIsraeli, \
		entry_width=self.helperGetEntryWidth(self.days), \
		listheight = itemHeight*len(self.days), \
		scrolledlist_items=self.days)
    self.comboDaysIsraeli.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartDayIsraeli()
    self.comboDaysIsraeli.selectitem(self.days[index])
    self.comboDaysIsraeli.grid(row=0, column=4)

    self.months = ("January", "February", "March", "April", "May", "June", \
		"July", "August", "September", "October", "November", \
		"December")
    self.comboMonthsIsraeli = Pmw.ComboBox(frameIsraeli, \
		entry_width=self.helperGetEntryWidth(self.listWeekdays), \
		listheight = itemHeight*len(self.months), \
		scrolledlist_items=self.months)
    self.comboMonthsIsraeli.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getStartMonthIsraeli()
    self.comboMonthsIsraeli.selectitem(self.months[index])
    self.comboMonthsIsraeli.grid(row=0, column=5)

    # ------------------------- End method -----------------------------

    labelEnd = Label(frameIsraeli, text="End: ")
    labelEnd.grid(row=1)

    labelLast = Label(frameIsraeli, text="Last")
    labelLast.grid(row=1, column=1)

    self.comboEndWeekdayIsraeli = Pmw.ComboBox(frameIsraeli, \
		entry_width=self.helperGetEntryWidth(self.listWeekdays), \
		listheight = itemHeight*len(self.listWeekdays), \
		scrolledlist_items=self.listWeekdays)
    self.comboEndWeekdayIsraeli.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    index = self.calSettings.getEndWeekdayIsraeli()
    self.comboEndWeekdayIsraeli.selectitem(self.listWeekdays[index])
    self.comboEndWeekdayIsraeli.grid(row=1, column=2)

    labelBeforeYomKippur = Label(frameIsraeli, text="before Yom Kippur")
    labelBeforeYomKippur.grid(row=1, column=3)

    radioCommon = Radiobutton(frameMethods, text="No DST", \
		variable=self.varCommonIsraeli, value=2)
    radioCommon.pack()

    okCancelFrame = Frame(frame)
    okCancelFrame.pack()

    buttonOK = Button(okCancelFrame, text="OK", command=self.okEvent)
    buttonOK.pack(side=LEFT, padx=10)

    buttonCancel = Button(okCancelFrame, text="Cancel", command=self.cancelEvent)
    buttonCancel.pack(side=LEFT, padx=10)

    self.selectBeforeAfter()

    self.execute(root, self.dialog, buttonOK)

  # OK Button was clicked
  def okEvent(self):
    if self.varCommonIsraeli.get() == 0:
      self.calSettings.setDSTMethod(0)
    elif self.varCommonIsraeli.get() == 1:
      self.calSettings.setDSTMethod(1)
    else:
      self.calSettings.setDSTMethod(2)

    index = self.getIndexFromString(self.listComboCommon1, self.comboCommon1.get())
    self.calSettings.setStartTimeCommon(index)

    index = self.getIndexFromString(self.listWeekdays, self.comboStartWeekdayCommon.get())
    self.calSettings.setStartWeekdayCommon(index)

    index = self.getIndexFromString(self.months, self.comboMonths.get())
    self.calSettings.setStartMonthCommon(index)

    index = self.getIndexFromString(self.listComboCommon1, self.comboCommon2.get())
    self.calSettings.setEndTimeCommon(index)

    index = self.getIndexFromString(self.listWeekdays, self.comboEndWeekday.get())
    self.calSettings.setEndWeekdayCommon(index)

    index = self.getIndexFromString(self.months, self.comboMonthsEnd.get())
    self.calSettings.setEndMonthCommon(index)

    index = self.getIndexFromString(self.listComboIsraeli1, self.comboIsraeli1.get())
    self.calSettings.setStartTimeIsraeli(index)

    index = self.getIndexFromString(self.listWeekdays, self.comboStartWeekdayIsraeli.get())
    self.calSettings.setStartWeekdayIsraeli(index)

    index = self.getIndexFromString(self.days, self.comboDaysIsraeli.get())
    self.calSettings.setStartDayIsraeli(index)

    index = self.getIndexFromString(self.months, self.comboMonthsIsraeli.get())
    self.calSettings.setStartMonthIsraeli(index)

    index = self.getIndexFromString(self.listWeekdays, self.comboEndWeekdayIsraeli.get())
    self.calSettings.setEndWeekdayIsraeli(index)

    self.dialog.destroy()

  # Cancel Button was clicked
  def cancelEvent(self):
    self.dialog.destroy()

# ---------------------------- ZMANIM ------------------------------------

class zmanimDialog(CalDialog):
  def __init__(self, calSettings, root):
    self.calSettings = calSettings
    self.createDialog(root)

  def getIndexFromString(self, array, str):
    for i in range(len(array)):
      if array[i] == str:
        return i

  def helperGetEntryWidth(self, stringlist):
    width = 0
    for item in stringlist:
      if len(item) > width:
        width = len(item)
    return width + 2

  def createDialog(self, root):
    self.dialog = self.createDialogWindow(root, "Zmanim")

    frame = Frame(self.dialog)
    frame.pack()

    labelStart = Label(frame, text="")
    labelStartFont = tkinter.font.Font()
    labelStartFont.name = labelStart["font"]
    itemHeight = labelStartFont.metrics("linespace") + \
                 labelStartFont.metrics("linespace")/3

    frameZmanim = Frame(frame)
    frameZmanim.pack()

    # Alot Hashachar

    labelAlotHashachar = Label(frameZmanim, text="Alot Hashachar: ")
    labelAlotHashachar.grid(row=0)

    self.listAlotHashachar = ("16.1 degrees below horizon",
				"72 minutes before sunrise",
				"90 minutes before sunrise")
    self.listAlotHashacharIDs = ("16Deg", "72min", "90min")

    self.comboAlotHashachar = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listAlotHashachar), \
		listheight = itemHeight*len(self.listAlotHashachar), \
		scrolledlist_items=self.listAlotHashachar)
    self.comboAlotHashachar.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getAlotHashachar()
    self.comboAlotHashachar.selectitem \
          (self.getIndexFromString(self.listAlotHashacharIDs, value))
    self.comboAlotHashachar.grid(row=0, column=1)

    # Earliest Tallit

    labelEarliestTallit = Label(frameZmanim, text="Earliest Tallit: ")
    labelEarliestTallit.grid(row=1)

    self.listEarliestTallit = ("11 degrees below horizon",
				"10.2 degrees below horizon")

    self.listEarliestTallitIDs = ("11Deg",
				"10.2Deg")

    self.comboEarliestTallit = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listEarliestTallit), \
		listheight = itemHeight*len(self.listEarliestTallit), \
		scrolledlist_items=self.listEarliestTallit)
    self.comboEarliestTallit.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getEarliestTallit()
    self.comboEarliestTallit.selectitem \
          (self.getIndexFromString(self.listEarliestTallitIDs, value))
    self.comboEarliestTallit.grid(row=1, column=1)

    # Kriat Shema

    labelKriatShema = Label(frameZmanim, text="Kriat Shema: ")
    labelKriatShema.grid(row=2)

    self.listKriatShema = ("GR\"O",
			"M\"A")

    self.listKriatShemaIDs = ("GRO", "MA")

    self.comboKriatShema = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listKriatShema), \
		listheight = itemHeight*len(self.listKriatShema), \
		scrolledlist_items=self.listKriatShema)
    self.comboKriatShema.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getKriatShema()
    self.comboKriatShema.selectitem \
          (self.getIndexFromString(self.listKriatShemaIDs, value))
    self.comboKriatShema.grid(row=2, column=1)

    # Tefila

    labelTefila = Label(frameZmanim, text="Tefila: ")
    labelTefila.grid(row=3)

    self.listTefila = ("GR\"O",
			"M\"A")
    self.listTefilaIDs = ("GRO", "MA")

    self.comboTefila = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listTefila), \
		listheight = itemHeight*len(self.listTefila), \
		scrolledlist_items=self.listTefila)
    self.comboTefila.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getTefila()
    self.comboTefila.selectitem \
          (self.getIndexFromString(self.listTefilaIDs, value))
    self.comboTefila.grid(row=3, column=1)

    # Chatzot

    labelChatzot = Label(frameZmanim, text="Chatzot: ")
    labelChatzot.grid(row=4)

    self.listChatzot = ("GR\"O",
			"M\"A")

    self.listChatzotIDs = ("GRO", "MA")

    self.comboChatzot = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listChatzot), \
		listheight = itemHeight*len(self.listChatzot), \
		scrolledlist_items=self.listChatzot)
    self.comboChatzot.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getChatzot()
    self.comboChatzot.selectitem \
          (self.getIndexFromString(self.listChatzotIDs, value))
    self.comboChatzot.grid(row=4, column=1)

    # Mincha Gedola

    labelMinchaGedola = Label(frameZmanim, text="Mincha Gedola: ")
    labelMinchaGedola.grid(row=5)

    self.listMinchaGedola = ("GR\"O",
			"M\"A")
    self.listMinchaGedolaIDs = ("GRO", "MA")

    self.comboMinchaGedola = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listMinchaGedola), \
		listheight = itemHeight*len(self.listMinchaGedola), \
		scrolledlist_items=self.listMinchaGedola)
    self.comboMinchaGedola.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getMinchaGedola()
    self.comboMinchaGedola.selectitem \
          (self.getIndexFromString(self.listMinchaGedolaIDs, value))
    self.comboMinchaGedola.grid(row=5, column=1)

    # Mincha K'tana

    labelMinchaKtana = Label(frameZmanim, text="Mincha K'tana: ")
    labelMinchaKtana.grid(row=6)

    self.listMinchaKtana = ("GR\"O",
			"M\"A")
    self.listMinchaKtanaIDs = ("GRO", "MA")

    self.comboMinchaKtana = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listMinchaKtana), \
		listheight = itemHeight*len(self.listMinchaKtana), \
		scrolledlist_items=self.listMinchaKtana)
    self.comboMinchaKtana.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getMinchaKtana()
    self.comboMinchaKtana.selectitem \
          (self.getIndexFromString(self.listMinchaKtanaIDs, value))
    self.comboMinchaKtana.grid(row=6, column=1)

    # Plag HaMincha

    labelPlagHaMincha = Label(frameZmanim, text="Plag Hamincha: ")
    labelPlagHaMincha.grid(row=7)

    self.listPlagHaMincha = ("GR\"O",
			"M\"A")
    self.listPlagHaMinchaIDs = ("GRO", "MA")

    self.comboPlagHaMincha = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listPlagHaMincha), \
		listheight = itemHeight*len(self.listPlagHaMincha), \
		scrolledlist_items=self.listPlagHaMincha)
    self.comboPlagHaMincha.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getPlagHaMincha()
    self.comboPlagHaMincha.selectitem \
          (self.getIndexFromString(self.listPlagHaMinchaIDs, value))
    self.comboPlagHaMincha.grid(row=7, column=1)

    # Tzait Hakochavim

    labelTzaitHakochavim = Label(frameZmanim, text="Tzait Hakochavim: ")
    labelTzaitHakochavim.grid(row=8)

    self.listTzaitHakochavim = ("72 minutes after sunset",
				"17 minutes after sunset",
				"20 minutes after sunset",
				"40 minutes after sunset",
				"50 minutes after sunset",
				"60 minutes after sunset",
				"5.95 degrees below horizon",
				"6.5 degrees below horizon",
				"7.0 degrees below horizon",
				"7.08 degrees below horizon",
				"7.5 degrees below horizon",
				"8.5 degrees below horizon",
				"8.75 degrees below horizon",
				"10.0 degrees below horizon")

    self.listTzaitHakochavimIDs = ("72min", "17min", "20min",
				"40min", "50min", "60min",
				"5.95deg", "6.5deg", "7.0deg", "7.08deg",
				"7.5deg", "8.5deg", "8.75deg", "10.0deg")

    self.comboTzaitHakochavim = Pmw.ComboBox(frameZmanim, \
		entry_width=self.helperGetEntryWidth(self.listTzaitHakochavim), \
		listheight = itemHeight*len(self.listTzaitHakochavim), \
		scrolledlist_items=self.listTzaitHakochavim)
    self.comboTzaitHakochavim.component('entry').config(state='disabled',
                          disabledbackground='white',
                          disabledforeground='black')
    value = self.calSettings.getTzaitHakochavim()
    self.comboTzaitHakochavim.selectitem \
          (self.getIndexFromString(self.listTzaitHakochavimIDs, value))
    self.comboTzaitHakochavim.grid(row=8, column=1)

    okCancelFrame = Frame(frame)
    okCancelFrame.pack()

    buttonOK = Button(okCancelFrame, text="OK", command=self.okEvent)
    buttonOK.pack(side=LEFT, padx=10)

    buttonCancel = Button(okCancelFrame, text="Cancel", command=self.cancelEvent)
    buttonCancel.pack(side=LEFT, padx=10)

    self.execute(root, self.dialog, buttonOK)

  # Cancel Button was clicked
  def cancelEvent(self):
    self.dialog.destroy()

  # OK Button was clicked
  def okEvent(self):
    index = self.getIndexFromString(self.listAlotHashachar, self.comboAlotHashachar.get())
    self.calSettings.setAlotHashachar(self.listAlotHashacharIDs[index])

    index = self.getIndexFromString(self.listEarliestTallit, self.comboEarliestTallit.get())
    self.calSettings.setEarliestTallit(self.listEarliestTallitIDs[index])

    index = self.getIndexFromString(self.listKriatShema, self.comboKriatShema.get())
    self.calSettings.setKriatShema(self.listKriatShemaIDs[index])

    index = self.getIndexFromString(self.listTefila, self.comboTefila.get())
    self.calSettings.setTefila(self.listTefilaIDs[index])

    index = self.getIndexFromString(self.listChatzot, self.comboChatzot.get())
    self.calSettings.setChatzot(self.listChatzotIDs[index])

    index = self.getIndexFromString(self.listMinchaGedola, self.comboMinchaGedola.get())
    self.calSettings.setMinchaGedola(self.listMinchaGedolaIDs[index])

    index = self.getIndexFromString(self.listMinchaKtana, self.comboMinchaKtana.get())
    self.calSettings.setMinchaKtana(self.listMinchaKtanaIDs[index])

    index = self.getIndexFromString(self.listPlagHaMincha, self.comboPlagHaMincha.get())
    self.calSettings.setPlagHaMincha(self.listPlagHaMinchaIDs[index])

    index = self.getIndexFromString(self.listTzaitHakochavim, self.comboTzaitHakochavim.get())
    self.calSettings.setTzaitHakochavim(self.listTzaitHakochavimIDs[index])

    self.dialog.destroy()
