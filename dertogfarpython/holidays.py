import callib

# Returns the weekday from a given hebrew date (0 for Sunday,
# 1 for Monday,...)
def getWeekdayOfHebrewDate(hebDay, hebMonth, hebYear):
  # Calculating the julian date
  julianisch = callib.hebrew_to_jd(hebYear, hebMonth, hebDay)
  wochentag = (int(julianisch)) % 7
  return wochentag

def berechne_feiertag(g_tag, g_monat, g_jahr, diaspora):
  julianisch = callib.gregorian_to_jd(g_jahr, g_monat, g_tag)
  hebjahr, hebmonat, hebtag = callib.jd_to_hebrew(julianisch)

  listHolidays = []

  # Holidays in Nisan

  hagadolTag = 14
  while getWeekdayOfHebrewDate(hagadolTag, 1, hebjahr) != 6:
    hagadolTag -= 1
  if hebtag == hagadolTag and hebmonat == 1:
    listHolidays.append("Shabat Hagadol")

  if hebtag == 14 and hebmonat == 1:
    listHolidays.append("Erev Pesach")
  if hebtag == 15 and hebmonat == 1:
    listHolidays.append("Pesach I")
  if hebtag == 16 and hebmonat == 1:
    if diaspora:
      listHolidays.append("Pesach II")
    else:
      listHolidays.append("Chol Hamoed")
  if hebtag == 17 and hebmonat == 1:
    listHolidays.append("Chol Hamoed")
  if hebtag == 18 and hebmonat == 1:
    listHolidays.append("Chol Hamoed")
  if hebtag == 19 and hebmonat == 1:
    listHolidays.append("Chol Hamoed")
  if hebtag == 20 and hebmonat == 1:
    listHolidays.append("Chol Hamoed")
  if hebtag == 21 and hebmonat == 1:
    if not diaspora:
      listHolidays.append("Pesach VII (Yizkor)")
    else:
      listHolidays.append("Pesach VII")
  if hebtag == 22 and hebmonat == 1:
    if diaspora:
      listHolidays.append("Pesach VIII (Yizkor)")

  # Yom Hashoah

  if getWeekdayOfHebrewDate(27, 1, hebjahr) == 5:
    if hebtag == 26 and hebmonat == 1:
      listHolidays.append("Yom Hashoah")
  elif hebjahr >= 5757 and getWeekdayOfHebrewDate(27, 1, hebjahr) == 0:
    if hebtag == 28 and hebmonat == 1:
      listHolidays.append("Yom Hashoah")
  else:
    if hebtag == 27 and hebmonat == 1:
      listHolidays.append("Yom Hashoah")

  # Holidays in Iyar

  # Yom Hazikaron

  if getWeekdayOfHebrewDate(4, 2, hebjahr) == 5: # If 4th of Iyar is a Thursday ...
    if hebtag == 2 and hebmonat == 2: # ... then Yom Hazicaron is on 2th of Iyar
      listHolidays.append("Yom Hazikaron")
  elif getWeekdayOfHebrewDate(4, 2, hebjahr) == 4:
    if hebtag == 3 and hebmonat == 2:
        listHolidays.append("Yom Hazikaron")
  elif hebjahr >= 5764 and getWeekdayOfHebrewDate(4, 2, hebjahr) == 0:
    if hebtag == 5 and hebmonat == 2:
      listHolidays.append("Yom Hazikaron")
  else:
    if hebtag == 4 and hebmonat == 2:
      listHolidays.append("Yom Hazikaron")

  # Yom Ha'Azmaut

  if getWeekdayOfHebrewDate(5, 2, hebjahr) == 6:
    if hebtag == 3 and hebmonat == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  elif getWeekdayOfHebrewDate(5, 2, hebjahr) == 5:
    if hebtag == 4 and hebmonat == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  elif hebjahr >= 5764 and getWeekdayOfHebrewDate(4, 2, hebjahr) == 0:
    if hebtag == 6 and hebmonat == 2:
      listHolidays.append("Yom Ha'Atzmaut")
  else:
    if hebtag == 5 and hebmonat == 2:
      listHolidays.append("Yom Ha'Atzmaut")

  if hebtag == 14 and hebmonat == 2:
    listHolidays.append("Pesach Sheni")

  # Holidays in Sivan

  if hebtag == 5 and hebmonat == 3:
    listHolidays.append("Erev Shavuot")
  if hebtag == 6 and hebmonat == 3:
    if diaspora:
      listHolidays.append("Shavuot I")
    else:
      listHolidays.append("Shavuot\n(Yizkor)")
  if hebtag == 7 and hebmonat == 3:
    if diaspora:
      listHolidays.append("Shavuot II\n(Yizkor)")

  # Holidays in Tammuz

  if getWeekdayOfHebrewDate(17, 4, hebjahr) == 6:
    if hebtag == 18 and hebmonat == 4:
      listHolidays.append("Fast of Tammuz")
  else:
    if hebtag == 17 and hebmonat == 4:
      listHolidays.append("Fast of Tammuz")

  # Holidays in Av

  if getWeekdayOfHebrewDate(9, 5, hebjahr) == 6:
    if hebtag == 10 and hebmonat == 5:
      listHolidays.append("Fast of Av")
  else:
    if hebtag == 9 and hebmonat == 5:
      listHolidays.append("Fast of Av")
  if hebtag == 15 and hebmonat == 5:
    listHolidays.append("Tu B'Av")

  # Holidays in Elul

  if hebtag == 29 and hebmonat == 6:
    listHolidays.append("Erev Rosh Hashana")

  # Holidays in Tishri

  if hebtag == 1 and hebmonat == 7:
    listHolidays.append("Rosh Hashana I")
  if hebtag == 2 and hebmonat == 7:
    listHolidays.append("Rosh Hashana II")
  if getWeekdayOfHebrewDate(3, 7, hebjahr) == 6:
    if hebtag == 4 and hebmonat == 7:
      listHolidays.append("Tzom Gedaliah")
  else:
    if hebtag == 3 and hebmonat == 7:
      listHolidays.append("Tzom Gedaliah")
  if hebtag == 9 and hebmonat == 7:
    listHolidays.append("Erev Yom Kippur")
  if hebtag == 10 and hebmonat == 7:
    listHolidays.append("Yom Kippur\n(Yizkor)")
  if hebtag == 15 and hebmonat == 7:
    if diaspora:
      listHolidays.append("Sukkot I")
    else:
      listHolidays.append("Sukkot")
  if hebtag == 16 and hebmonat == 7:
    if diaspora:
      listHolidays.append("Sukkot II")
    else:
      listHolidays.append("Chol Hamoed")
  if hebtag == 17 and hebmonat == 7:
    listHolidays.append("Chol Hamoed")
  if hebtag == 18 and hebmonat == 7:
    listHolidays.append("Chol Hamoed")
  if hebtag == 19 and hebmonat == 7:
    listHolidays.append("Chol Hamoed")
  if hebtag == 20 and hebmonat == 7:
    listHolidays.append("Chol Hamoed")
  if hebtag == 21 and hebmonat == 7:
    listHolidays.append("Hoshana Raba")
  if hebtag == 22 and hebmonat == 7:
    if not diaspora:
      listHolidays.append("Shemini Atzereth\n(Yizkor)")
      listHolidays.append("Simchat Torah")
    else:
      listHolidays.append("Shemini Atzereth\n(Yizkor)")
  if hebtag == 23 and hebmonat == 7:
    if diaspora:
      listHolidays.append("Simchat Torah")

  # Holidays in Kislev

  if hebtag == 25 and hebmonat == 9:
    listHolidays.append("Chanukka I")
  if hebtag == 26 and hebmonat == 9:
    listHolidays.append("Chanukka II")
  if hebtag == 27 and hebmonat == 9:
    listHolidays.append("Chanukka III")
  if hebtag == 28 and hebmonat == 9:
    listHolidays.append("Chanukka IV")
  if hebtag == 29 and hebmonat == 9:
    listHolidays.append("Chanukka V")
  # Holidays in Tevet

  if hebtag == 10 and hebmonat == 10:
    listHolidays.append("Fast of Tevet")

  if callib.hebrew_month_days(hebjahr, 9) == 30:
    if hebtag == 30 and hebmonat == 9:
      listHolidays.append("Chanukka VI")
    if hebtag == 1 and hebmonat == 10:
      listHolidays.append("Chanukka VII")
    if hebtag == 2 and hebmonat == 10:
      listHolidays.append("Chanukka VIII")
  if callib.hebrew_month_days(hebjahr, 9) == 29:
    if hebtag == 1 and hebmonat == 10:
      listHolidays.append("Chanukka VI")
    if hebtag == 2 and hebmonat == 10:
      listHolidays.append("Chanukka VII")
    if hebtag == 3 and hebmonat == 10:
      listHolidays.append("Chanukka VIII")

  # Holidays in Shevat

  if hebtag == 15 and hebmonat == 11:
    listHolidays.append("Tu B'Shevat")

  # Holidays in Adar (I)/Adar II

  if callib.hebrew_leap(hebjahr):
    monatEsther = 13
  else:
    monatEsther = 12
    
  if getWeekdayOfHebrewDate(13, monatEsther, hebjahr) == 6:
    if hebtag == 11 and hebmonat == monatEsther:
      listHolidays.append("Fast of Esther")
  else:
    if hebtag == 13 and hebmonat == monatEsther:
      listHolidays.append("Fast of Esther")

  if hebtag == 14 and hebmonat == monatEsther:
    listHolidays.append("Purim")
  if hebtag == 15 and hebmonat == monatEsther:
    listHolidays.append("Shushan Purim")

  if callib.hebrew_leap(hebjahr):
    if hebtag == 14 and hebmonat == 12:
      listHolidays.append("Purim Katan")
    if hebtag == 15 and hebmonat == 12:
      listHolidays.append("Shushan Purim Katan")

  return listHolidays
