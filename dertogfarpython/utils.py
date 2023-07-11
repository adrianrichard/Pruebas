import callib

def getWeekday(julianisch):
  weekday = (int(julianisch)) % 7
  return weekday
def getLastDayOfGregorianMonth(month, year):
  if month == 2 and callib.leap_gregorian(year):
    return 29
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    return month_days[month-1]

def isDST(day, month, year, calSettings):
  if calSettings.getDSTMethod() == 0:
    if calSettings.getStartTimeCommon() == 4: # Last
      jdStart = callib.gregorian_to_jd(year,
              calSettings.getStartMonthCommon()+1,
              getLastDayOfGregorianMonth(calSettings.getStartMonthCommon()+1, year))
      while getWeekday(jdStart) != calSettings.getStartWeekdayCommon():
        jdStart -= 1
    else:
      jdStart = callib.gregorian_to_jd(year,
                           calSettings.getStartMonthCommon()+1, 1)
      while getWeekday(jdStart) != calSettings.getStartWeekdayCommon():
        jdStart += 1
      if calSettings.getStartTimeCommon() > 0:
        for i in range(calSettings.getStartTimeCommon()):
          jdStart += 1
          while getWeekday(jdStart) != calSettings.getStartWeekdayCommon():
            jdStart += 1

    if calSettings.getEndTimeCommon() == 4: # Last
      jdEnd = callib.gregorian_to_jd(year,
              calSettings.getEndMonthCommon()+1,
              getLastDayOfGregorianMonth(calSettings.getEndMonthCommon()+1, year))
      while getWeekday(jdEnd) != calSettings.getEndWeekdayCommon():
        jdEnd -= 1
    else:
      jdEnd = callib.gregorian_to_jd(year,
                           calSettings.getEndMonthCommon()+1, 1)
      while getWeekday(jdEnd) != calSettings.getEndWeekdayCommon():
        jdEnd += 1
      if calSettings.getEndTimeCommon() > 0:
        for i in range(calSettings.getEndTimeCommon()):
          jdEnd += 1
          while getWeekday(jdEnd) != calSettings.getEndWeekdayCommon():
            jdEnd += 1

    jd_now = callib.gregorian_to_jd(year, month, day)
    if int(jdEnd) > int(jdStart):
      if int(jd_now) >= int(jdStart) and int(jd_now) < int(jdEnd):
        return True
    else:
      if int(jd_now) < int(jdEnd) or int(jd_now) >= int(jdStart):
        return True
    return False

  elif calSettings.getDSTMethod() == 1:
    if calSettings.getStartTimeIsraeli() == 1: # Last ... before ...
      jdStart = callib.gregorian_to_jd(year,
              calSettings.getStartMonthIsraeli()+1,
              calSettings.getStartDayIsraeli()+1)
      jdStart -= 1
      while getWeekday(jdStart) != calSettings.getStartWeekdayIsraeli():
        jdStart -= 1
    else: # First ... after ...
      jdStart = callib.gregorian_to_jd(year,
                           calSettings.getStartMonthIsraeli()+1,
                           calSettings.getStartDayIsraeli()+1)
      jdStart += 1
      while getWeekday(jdStart) != calSettings.getStartWeekdayIsraeli():
        jdStart += 1

    jd = callib.gregorian_to_jd(year, 12, 31)
    heb = callib.jd_to_hebrew(jd)
    jdEnd = callib.hebrew_to_jd(heb[0], 7, 9) # 9 Tishri
    while getWeekday(jdEnd) != calSettings.getEndWeekdayIsraeli():
      jdEnd -= 1

    jd_now = callib.gregorian_to_jd(year, month, day)
    if int(jd_now) >= int(jdStart) and int(jd_now) < int(jdEnd):
      return True
    else:
      return False
