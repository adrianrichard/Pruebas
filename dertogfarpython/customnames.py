import callib

import torah

def getWeekdayName(weekday):
  if weekday == 0:
    return "Sunday"
  if weekday == 1:
    return "Monday"
  if weekday == 2:
    return "Tuesday"
  if weekday == 3:
    return "Wednesday"
  if weekday == 4:
    return "Thursday"
  if weekday == 5:
    return "Friday"
  if weekday == 6:
    return "Shabbat"
  return ""

def getGregorianMonthName(month):
  if month == 1:
    return "January"
  elif month == 2:
    return "February"
  elif month == 3:
    return "March"
  elif month == 4:
    return "April"
  elif month == 5:
    return "May"
  elif month == 6:
    return "June"
  elif month == 7:
    return "July"
  elif month == 8:
    return "August"
  elif month == 9:
    return "September"
  elif month == 10:
    return "October"
  elif month == 11:
    return "November"
  elif month == 12:
    return "December"

def getJewishMonthName(month, year):

  if month == 1:
    return "Nisan"
  elif month == 2:
    return "Iyyar"
  elif month == 3:
    return "Sivan"
  elif month == 4:
    return "Tammuz"
  elif month == 5:
    return "Av"
  elif month == 6:
    return "Elul"
  elif month == 7:
    return "Tishri"
  elif month == 8:
    return "Heshvan"
  elif month == 9:
    return "Kislev"
  elif month == 10:
    return "Tevet"
  elif month == 11:
    return "Shevat"
  elif month == 12:
    if callib.hebrew_leap(year):
      return "Adar I"
    else:
      return "Adar"
    
  elif month == 13:
    return "Adar II"

def getOmerCount(omerCount):
  return str(omerCount) + " L'Omer"

def getTorahSectionName(section):
  if (section == torah.ID_BERESHITH):
    return "Bereshith";
  if (section == torah.ID_NOAH):
    return "Noah";
  if (section == torah.ID_LEHLEHA):
    return "Le'h Leha";
  if (section == torah.ID_VAYERA):
    return "Vayera";
  if (section == torah.ID_HAYESARAH):
    return "Haye Sarah";
  if (section == torah.ID_TOLEDOTH):
    return "Toledoth";
  if (section == torah.ID_VAYETSE):
    return "Vayetse";
  if (section == torah.ID_VAYISHLAH):
    return "Vayishlah";
  if (section == torah.ID_VAYESHEB):
    return "Vayesheb";
  if (section == torah.ID_MIKKETS):
    return "Mikkets";
  if (section == torah.ID_VAYIGGASH):
    return "Vayiggash";
  if (section == torah.ID_VAYHEE):
    return "Vayhee";
  if (section == torah.ID_SHEMOTH):
    return "Shemoth";
  if (section == torah.ID_VAERA):
    return "Vaera";
  if (section == torah.ID_BO):
    return "Bo";
  if (section == torah.ID_BESHALLAH):
    return "Beshallah, Shabbat Shirah";
  if (section == torah.ID_YITHRO):
    return "Yithro";
  if (section == torah.ID_MISHPATIM):
    return "Mishpatim";
  if (section == torah.ID_TERUMAH):
    return "Terumah";
  if (section == torah.ID_TETSAVVEH):
    return "Tetsavveh";
  if (section == torah.ID_KITISSA):
    return "Ki Tissa";
  if (section == torah.ID_VAYAKHEL):
    return "Vayakhel";
  if (section == torah.ID_PEKUDE):
    return "Pekude";
  if (section == torah.ID_VAYIKRA):
    return "Vayikra";
  if (section == torah.ID_TSAV):
    return "Tsav";
  if (section == torah.ID_SHEMINI):
    return "Shemini";
  if (section == torah.ID_TAZRIANG):
    return "Tazria";
  if (section == torah.ID_METSORANG):
    return "Metsora";
  if (section == torah.ID_AHAREMOTH):
    return "Aharemoth";
  if (section == torah.ID_KEDOSHIM):
    return "Kedoshim";
  if (section == torah.ID_EMOR):
    return "Emor";
  if (section == torah.ID_BEHAR):
    return "Behar";
  if (section == torah.ID_BEHUKKOTHAI):
    return "Behukkothai";
  if (section == torah.ID_BEMIDBAR):
    return "Bemidbar";
  if (section == torah.ID_NASO):
    return "Naso";
  if (section == torah.ID_BEHAALOTEHA):
    return "Behaaloteha";
  if (section == torah.ID_SHELAHLEHA):
    return "Shelah Leha";
  if (section == torah.ID_KORAH):
    return "Korah";
  if (section == torah.ID_HUKATH):
    return "Hukath";
  if (section == torah.ID_BALAK):
    return "Balak";
  if (section == torah.ID_PINHAS):
    return "Pinhas";
  if (section == torah.ID_MATOTH):
    return "Matoth";
  if (section == torah.ID_MASEH):
    return "Maseh";
  if (section == torah.ID_DEBARIM):
    return "Debarim, Shabbat Hazon";
  if (section == torah.ID_VAETHANAN):
    return "Vaethanan, Shabbat Nahamu";
  if (section == torah.ID_EKEB):
    return "Ekeb";
  if (section == torah.ID_REEH):
    return "Reeh";
  if (section == torah.ID_SHOFETIM):
    return "Shofetim";
  if (section == torah.ID_KITETSE):
    return "Ki Tetse";
  if (section == torah.ID_KITABO):
    return "Ki Tabo";
  if (section == torah.ID_NITSABIM):
    return "Nitsabim";
  if (section == torah.ID_VAYELEH):
    return "Vayeleh";
  if (section == torah.ID_HAAZINU):
    return "Haazinu";

  if (section == torah.ID_SHEKALIM):
    return "Shabbat Shekalim";
  if (section == torah.ID_ZAHOR):
    return "Shabbat Za'hor";
  if (section == torah.ID_PARAH):
    return "Shabbat Parah";
  if (section == torah.ID_HAHODESH):
    return "Shabbat Hahodesh";
  if (section == torah.ID_SHUVA):
    return "Shabbat Shuva";

  return "";
