# -*- coding: utf-8 -*-
r"""
======================================================================================
frigcal_configs.py: optional user-provided configuration settings.

Code simple Python assignments in this file to customize your frigcal's
appearance and behavior.  Your settings will be loaded at frigcal startup.
See frigcal_configs_base.py for the full set of options you can customize
by reassigning names here, along with their defaults and documentation.

DETAILS:

This file is shipped in UTF-8 Unicode and Windows or Unix end-line format;
see UserGuide.html's "Using the Program" => "Configurations File" section. 

In version 2.0+, EDIT THIS FILE for all user-defined customizations, instead
of changing the frigcal_configs_base.py base file in-place.  This file (not
the base) is imported by frigcal at startup, and imports "*" from the base
file initially to load preset "factory" defaults.  Any assignments you code
here will override (i.e., replace) the corresponding default assignments in
the base file automatically.

Your customizations here will also be immune to changes in the base file when
upgrading to new frigcal versions, as long as you save your version of this
file and restore it in the new version after installation.  Any errors in
this file are still reported by both GUI popup and console message as before.

See the frigcal_configs_base.py base file in this folder for setting examples,
settings available, and all settings documentation.  Coding note: the initial
"from *" here could be avoided by having the base file import this (instead
of vice versa), but per Python philosophy: Explicit Is Better Than Implicit. 
======================================================================================
"""
import sys, os  # for platform, etc.

# Load the base file's defaults first (don't delete this line!)
from frigcal_configs_base import *


# ----User-defined customizations of frigcal_configs_base.py follow----

# Code your assignments here; they'll be immune to base-file changes on upgrades


"""
rootbg = '#A28264'     # removed the 3 quotes above and below to activate code
daysbg = 'wheat'       # basic settings include colors, fonts, etc.
"""


# Calendar files folder (else uses install folder's Calendars)
"""
if RunningOnMac:
    icspath = '/MY-STUFF/Code/frigcal/Calendars'        # outside app and source?
elif RunningOnWindows:
    icspath = r'C:\MY-STUFF\Code\frigcal\Calendars'     # outside exe and source?
elif RunningOnLinux:
    icspath = '/home/ubuntu-user/frigcal/Calendars'
"""


# Calendar files alternative: user guide's screenshots demo files, in install dir
"""
if RunningOnMac:
   #icspath = '/MY-STUFF/Code/frigcal/Calendars/2.0-examples/Screenshots-Demo-Calendars'
    icspath = '/Applications/Frigcal.app/Contents/Resources/Calendars/2.0-examples/Screenshots-Demo-Calendars'
elif RunningOnWindows:
   #icspath = r'C:\MY-STUFF\Code\frigcal\Calendars\2.0-examples\Screenshots-Demo-Calendars' 
    icspath = r'C:\Program Files\Frigcal\Calendars\2.0-examples\Screenshots-Demo-Calendars' 
elif RunningOnLinux:
   #icspath = '/home/ubuntu-user/My-Code/Frigcal/Calendars/2.0-examples/Screenshots-Demo-Calendars'
    icspath = '/home/ubuntu-user/Desktop/frigcal/Calendars/2.0-examples/Screenshots-Demo-Calendars'
"""


# Month images folder (else uses install folder's MonthImages)
"""
imgpath = 'MonthImages/AlternateMonthImages/DrawnImages1'.replace('/', os.sep)   # portable
"""


# And many more... see frigcal_configs_base.py
