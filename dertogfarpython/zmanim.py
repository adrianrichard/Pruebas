import times
import locations
import math
from utils import *

# Returns a list of tuples of the form (name of zmanim, time as a string)
# e.g. [("Alot Hashachar", "05:00AM"), ("Earliest Tallit", "06:00AM")]
def getZmanimForDay(calSettings, gday, gmonth, gyear):
  currentLocationName = calSettings.getCurrentLocationName()
  currentLocation = locations.getLocationData(currentLocationName)
  result = []

  # Alot Hashachar

  timeStr = ""
  if calSettings.getAlotHashachar() == "16Deg":
    time = times.GetSunriseDegreesBelowHorizon(gmonth, gday, gyear, 16.1, currentLocation)
    if isDST(gday, gmonth, gyear, calSettings):
      time[0] += 1
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getAlotHashachar() == "72min":
    time = times.GetSunrise(gmonth, gday, gyear, currentLocation)
    if isDST(gday, gmonth, gyear, calSettings):
      time[0] += 1
    time = times.SubtractMinutes(time, 72)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getAlotHashachar == "90min":
    time = times.GetSunrise(gmonth, gday, gyear, currentLocation)
    if isDST(gday, gmonth, gyear, calSettings):
      time[0] += 1
    time = times.SubtractMinutes(time, 90)
    timeStr = times.FormatTime(calSettings, time)

  result = result + [("Alot Hashachar", timeStr)]

  # Earliest Tallit

  timeStr = ""
  if calSettings.getEarliestTallit() == "11Deg":
    time = times.GetSunriseDegreesBelowHorizon(gmonth, gday, gyear, 11, currentLocation)
    if isDST(gday, gmonth, gyear, calSettings):
      time[0] += 1
    timeStr = times.FormatTime(calSettings, time)
  if calSettings.getEarliestTallit() == "10.2Deg":
    time = times.GetSunriseDegreesBelowHorizon(gmonth, gday, gyear, 10.2, currentLocation)
    if isDST(gday, gmonth, gyear, calSettings):
      time[0] += 1
    timeStr = times.FormatTime(calSettings, time)

  result = result + [("Earliest Tallit", timeStr)]

  timeSunrise = times.GetSunrise(gmonth, gday, gyear, currentLocation)
  if isDST(gday, gmonth, gyear, calSettings):
    timeSunrise[0] += 1
  timeSunset = times.GetSunset(gmonth, gday, gyear, currentLocation)
  if isDST(gday, gmonth, gyear, calSettings):
    timeSunset[0] += 1

  timeStr = times.FormatTime(calSettings, timeSunrise)
  result = result + [("Hanetz Hachama", timeStr)]

  # Kriat Shema

  timeStr = ""
  if calSettings.getKriatShema() == "MA":
    time = timeSunrise[:]
    time = times.GetProportionalHours(3, timeSunrise, timeSunset)
    time = times.SubtractMinutes(time, 36)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getKriatShema() == "GRO":
    time = times.GetProportionalHours(3, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Kriat Shema", timeStr)]

  # Tefila

  timeStr = ""
  if calSettings.getTefila() == "MA":
    time = times.GetProportionalHours(4, timeSunrise, timeSunset)
    time = times.SubtractMinutes(time, 24)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTefila() == "GRO":
    time = times.GetProportionalHours(4, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Tefila", timeStr)]

  # Chatzot

  timeStr = ""
  if calSettings.getChatzot() == "MA":
    time = times.GetProportionalHours(6, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getChatzot() == "GRO":
    time = times.GetProportionalHours(6, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Chatzot", timeStr)]

  # Mincha Gedola

  timeStr = ""
  if calSettings.getMinchaGedola() == "MA":
    time = times.GetProportionalHours(6.5, timeSunrise, timeSunset)
    time = times.AddMinutes(time, 6)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getMinchaGedola() == "GRO":
    time = times.GetProportionalHours(6.5, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Mincha Gedola", timeStr)]

  # Mincha K'tana

  timeStr = ""
  if calSettings.getMinchaKtana() == "MA":
    time = times.GetProportionalHours(6.5, timeSunrise, timeSunset)
    time = times.AddMinutes(time, 42)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getMinchaKtana() == "GRO":
    time = times.GetProportionalHours(9.5, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Mincha K'tana", timeStr)]

  # Plag HaMincha

  timeStr = ""
  if calSettings.getPlagHaMincha() == "MA":
    time = times.GetProportionalHours(10.75, timeSunrise, timeSunset)
    time = times.AddMinutes(time, 57)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getPlagHaMincha() == "GRO":
    time = times.GetProportionalHours(10.75, timeSunrise, timeSunset)
    timeStr = times.FormatTime(calSettings, time)
  result = result + [("Plag Hamincha", timeStr)]

  timeStr = times.FormatTime(calSettings, timeSunset)
  result = result + [("Shkiat Hachama", timeStr)]

  timeStr = ""
  if calSettings.getTzaitHakochavim() == "72min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 72)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "17min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 17)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "20min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 20)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "40min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 40)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "50min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 50)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "60min":
    time = timeSunset[:]
    time = times.AddMinutes(time, 60)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "5.95deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 5.95, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "6.5deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 6.5, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "7.0deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 7.0, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "7.08deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 7.08, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "7.5deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 7.5, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "8.5deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 8.5, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "8.75deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 8.75, currentLocation)
    timeStr = times.FormatTime(calSettings, time)
  elif calSettings.getTzaitHakochavim() == "10.0deg":
    time = times.GetSunsetDegreesBelowHorizon(gmonth, gday, gyear, 10.0, currentLocation)
    timeStr = times.FormatTime(calSettings, time)

  result = result + [("Tzait Hakochavim", timeStr)]

  shaaZmanit = int(times.GetShaaZmanit(timeSunrise, timeSunset))
  timeShaaZmanit = (int(math.floor(shaaZmanit / 60)), shaaZmanit % 60)
  timeStr = times.FormatTimeShaaZmanit(timeShaaZmanit)
  result = result + [("Sha'a Zmanit", timeStr)]

  return result