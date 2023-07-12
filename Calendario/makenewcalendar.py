#!/usr/bin/python3
"""
=====================================================================================
makecalendar.py (frigcal utility script)
Run me to generate a new named calendar file in the calendars folder.
The new calendar's name is input in this script's console window.
Reuses file creation code in icsfiletools written for the default file.
Not required if you use just existing files or the automatic default file.
=====================================================================================
"""

import os   # for chdir

# [2.0] for frozen app/exes, fix module+resource visibility (sys.path)
import fixfrozenpaths

# [2.0] make relative calendar paths map to frigcal's install folder
os.chdir(fixfrozenpaths.fetchMyInstallDir(__file__))   # absolute

import icsfiletools
icsfiletools.ask_init_default_ics_file()
input('Calendar created; (re)start frigcal to use [press Enter].')
