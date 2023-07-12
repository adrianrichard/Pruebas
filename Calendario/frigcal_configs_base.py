# -*- coding: utf-8 -*-
r"""
======================================================================================
frigcal_configs_base.py:
Default configuration settings, in Python code, loaded at frigcal startup.

DON'T EDIT THIS FILE: instead, tailor your frigcal's appearance and behavior
by adding code to "frigcal_configs.py" that reassigns any of the names here.
That way, your settings will be immune to changes in this file on upgrades.

This file is shipped in UTF-8 Unicode and Windows end-line formats; see
UserGuide.html's "Using the Program" => "Configurations File" section. 

BASE AND USER FILES
-------------------
As of version 2.0, configuration settings are now split into two files:

    frigcal_configs_base.py
        this base file, with system-provided defaults and examples

    frigcal_configs.py
        the user file, with any user-provided customizations (EDIT THIS)

These files are related and used by frigcal as follows:

  -The base file has all the preset defaults, and may change in new versions
  -The user file imports "*" from the base and overrides any of its settings
  -frigcal imports all its settings from the user file, not the base

This simplifies editing work when upgrading to new releases: users normally
need just copy over their prior user file to the new release's folder, instead
of pasting individual settings into the new base file.  Users should still
inspect the base file to see if any new settings are available, and in-place
edits in this base file still work as before (but are discouraged).


THE ESSENTIALS
--------------

HOW TO EDIT
  This file gives multiple example settings for some names; per normal Python
  semantics, only the LAST assignment listed and run will be used.  These
  example settings may be freely changed, reordered, commented-out, or deleted.
  Each name should generally be assigned once, though the program fills in
  defaults (and prints warnings on the console) if they are not.

FOR COLORS
  Give a string color name (e.g., 'maroon') or RGB hex-code triple string
  '#RRGGBB'.  For example, '#B7DA8D' is moss green, and '#DD76C7' is rose.
  Try http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm for defined color names.
  [1.7] For custom colors, see the newly-included "pickcolor.py" utility script;
  it displays a chosen color's '#RRGGBB' string in a GUI, for cut-and-paste.
  Caution: using the same color for text and background will be unreadable.

FOR FONTS
  Give either a tuple ('family', size?, 'style? style? ...) or a string
  'family size? style? style? ...' if the family name contains no spaces.
  The optional size must appear second; negative means pixels instead of
  points, 0 means default size, and omission means 0.  Styles may include
  any mix of: 'bold', 'normal' (non-bold) 'italic', 'roman' (non-italic),
  'underline', and 'overstrike'.  The default style is 'normal roman'.

  For example: ('arial', 16, 'bold'), 'courier 14 normal', 'times 15 italic',
  ('consolas', 12, 'bold italic underline').  Some partial specifiers work
  too ('times', 'times 20'), but don't skip the size ('times bold' fails).
  Note: on Linux, some Asian characters may render better if non-bold,
  and larger font sizes may help in general; see LINUX_ASIAN_FONTS below.
  In [2.0], some fonts have been tailored for Mac OS X appearance as well.

EDIT WITH CARE
  frigcal won't start if there is a syntax error in this file (and you'll get
  error details in both the console window and a GUI popup), so be careful with
  changes here.  You may want to save a backup copy before making edits.  If
  there are no syntax errors, most invalid or missing setting values do not
  cause the program to fail or stop, but are replaced with defaults and may
  trigger messages on the console; please verify your values.  Import this
  module separately in a Python interactive session to error check.


ADDITIONAL NOTES
----------------

USING NON-ENGLISH STRINGS HERE [1.7]
  The first line in this file gives the Unicode encoding of its content,
  including all its embedded string literals.  Python defaults to UTF-8
  (which handles simple ASCII) if no such line is present, but other encodings
  can be used above too (e.g., latin-1).  You can also use Python's '\uhhhh'
  and '\Uhhhhhhhh' Unicode code-point escapes in any of this file's strings.
  Non-English strings can be used in file paths, category names, and more;
  see the example in event-color category names below.

EVENT FOREGROUND COLORS [1.7]
  As of version 1.7, event summary color values can be either a string giving
  background only (the former scheme), or a 2-item tuple giving both background
  and foreground colors (the new enhanced scheme). For example, a color setting:

    'wheat'
         sets the event widget's background color only, leaving its
         foreground (the event text) the default black

    ('navy', 'orange')
         sets the event widget's background color to 'navy' and its
         foreground (the event text) color to 'orange'

  In all cases, the default event background and foreground are white and black,
  and each color value may still be either a color name or #RRGGBB hex code.
  Caution: using the same color for text and background will be unreadable, and
  some error cases may result in this; see the console for color error messages.

COLOR NAME CHANGES [1.6]
  Standard Windows installs of Pythons 3.4+ use version 8.6 of the Tk library
  underlying tkinter, which changes the meaning of four color names.  "green",
  "purple", "maroon", and "grey/gray" render more darkly, and some of the new
  8.6 name equivalents aren't available in older Tk versions (e.g., the former
  "green" becomes "lime", but "lime" doesn't work in prior Tks!).

  This file maps changed colors to portable names (e.g., GREEN).  As a rule of
  thumb, though, using '#RRGGBB' hex strings instead of color names will make
  your colors portable across all Pythons and Tks (see "pickcolor.py" to create
  these strings).  For more details on this Tk change:

    http://learning-python.com/books/python-changes-2014-plus.html#s359
    http://www.tcl.tk/cgi-bin/tct/tip/403.html
    https://bugs.python.org/issue23982, or
    https://www.tcl.tk/man/tcl/TkCmd/colors.htm.

TBDs
  A plain text configs file wouldn't require Python coding skills, but also
  wouldn't help much, as errors may still preclude program launch.  Values
  could also be verified once at startup instead of on each config.
======================================================================================
"""


# For platform/version-dependent settings
import sys, tkinter, os



# For platform-specific choices (available in frigcal_configs.py too)

RunningOnMac     = sys.platform.startswith('darwin')       # all OS (X)
RunningOnWindows = sys.platform.startswith('win')          # all Windows
RunningOnLinux   = sys.platform.startswith('linux')        # all Linux



# For Python- or Tk-specific choices

PyVersion = float(sys.version[:3])    # e.g., '3.5.0 ...' => 3.5
TkVersion = tkinter.TkVersion         # e.g., 8.5 or 8.6 (Win Py 3.4+ use Tk 8.6)
print('Using Python', PyVersion, 'and Tk', TkVersion)    # display versions [1.6]



# Portable color choices that differ between Tk 8.6 and earlier (see above) [1.6]

GREEN  = 'green'  if TkVersion < 8.6 else 'lime'         # 'lime' only in 8.6+
PURPLE = 'medium purple'                                 # same in all versions
MAROON = 'maroon' if TkVersion < 8.6 else 'indian red'   # not exactly, but close
GRAY   = 'grey'   if TkVersion < 8.6 else 'silver'       # 'silver' only in 8.6+



#=====================================================================================
# MONTH AND IMAGE WINDOW BEHAVIOR (last setting wins: multiple examples)
#=====================================================================================


# Event click/press bindings model, 'mouse' or 'touch': see UserGuide.html

clickmode = 'touch'         # single-press model
clickmode = 'mouse'         # double-press model, with inline summary edits



# Month windows' initial size in pixels or % (but fully resizable thereafter)

initwinsize = None          # if None, automatically sized by content (but may vary)
initwinsize = '1000x800'    # string giving absolute pixels: '<width>x<height>'
initwinsize = 0.75          # float <= 1.0 giving % of full screen's width and height
initwinsize = (0.60, 0.80)  # tuple = (% of full screen width, % of full screen height)



# Month windows' minimum size in pixels (to avoid shrinking too much if few events)

minwinsize = None           # if None, no limit on shrink (but some controls vanish)
minwinsize = initwinsize    # if same, can only grow, not shrink
minwinsize = '650x400'      # pixels: '<width>x<height>'



# Month windows' start position (or add at end of initwinsize: '800x600+10+10') 

initwinposition = '+10+10'  # start +X+Y offset in pixels from top left (clones too)
initwinposition = None      # if None, default = GUI chooses (generally preferred)



# Month image-windows' start position (for all month's images) [1.4]

initimgposition = '+0+0'    # start +X+Y offset in pixels from top left corner
initimgposition = None      # if None, default = GUI chooses (generally preferred)



#=====================================================================================
# MONTH WINDOW APPEARANCE (last setting wins: multiple examples)
#=====================================================================================


# Month window background color

rootbg = None                   # None=tk default
rootbg = 'tan'                  # see above for format
rootbg = 'navy'                 
rootbg = 'steelblue'



# Month day-tiles background color

daysbg = None                   # None=tk default
daysbg = 'beige'                # see above for format
daysbg = 'lightblue'
daysbg = 'powderblue'



# Font for text on month day-tiles: number and events (and event-select list)

daysfont = None                              # None=tk default
daysfont = ('courier', 16, 'bold italic')    # see above for format
daysfont = ('times', 9, 'bold underline')
daysfont = ('calibri', 12, 'normal')
daysfont = ('arial', 9, 'bold')              # default

# Customize by platform: larger font on Mac and Linux [2.0]

if RunningOnMac:
    daysfont = ('arial', 10, 'bold')         # or menlo, monaco        

elif RunningOnWindows:
    pass  # use default (last) above         # or consolas

elif RunningOnLinux:
    daysfont = ('arial', 10, 'bold')         # or inconsolata



# Font for text on month and day names at top of window

monthnamefont = ('times', 12, 'bold italic')
daynamefont = ('times', 9)

# Customize by platform

if RunningOnMac:
    monthnamefont = ('arial', 15, 'bold italic')  
    daynamefont = ('monaco', 10)

elif RunningOnWindows:
    monthnamefont = ('arial', 14, 'bold italic')
    daynamefont = ('consolas', 9)

elif RunningOnLinux:
    monthnamefont = ('arial', 14, 'bold italic')
    daynamefont = ('inconsolata', 9)



# Font for text on buttons and toggles at top and bottom of month windows
# This is also used for buttons in event-edit and even-list dialog popups

controlsfont = None                          # None=tk default
controlsfont = ('arial', 8, 'bold')          # see above for format

# Customize by platform

if RunningOnMac:
    controlsfont = ('arial', 9, 'bold')      # use larger fonts on Mac



# Current-day shading color, defaults to gray if not set or None [1.6]

currentdaycolor = GRAY                       # or rootbg to match border?



#=====================================================================================
# FOOTER PANEL: size (start or fixed), background color, and font
#=====================================================================================


footerheight = 5                         # in #lines, or None=tk default
footerresize = False                     # True=grows with window, else fixed #lines
footercolor  = 'beige'                   # (see above) or None=tk default (white)
footerfont   = ('courier', 10, 'bold')   # (see above) or None=tk default


# Custom footer fonts on Mac OS X and Linux [2.0]

if RunningOnMac:
    footerfont  = ('courier', 12, 'normal')     # or menlo, monaco, etc.

elif RunningOnWindows:
    pass  # use default (last) above            # or consolas, etc.

elif RunningOnLinux:
    footerfont  = ('courier', 11, 'bold')       # or inconsolata, etc.


# Footer display control

clearfooter = False                      # True=erase footer text on go to new month



#=====================================================================================
# EVENT VIEW/EDIT DIALOG: appearance (None=tk default, see intro for values)
#=====================================================================================


eventdialogfg   = 'beige'
eventdialogbg   = 'tan'
eventdialogfont = ('courier', 12, 'bold')          # default


# Customize by platform: larger on Linux and Mac, non-bold on Mac [2.0]

if RunningOnMac:
    eventdialogfont = ('courier', 14, 'normal')    # or menlo, monaco

elif RunningOnWindows:
    pass  # use default (last) above               # or consolas

elif RunningOnLinux: 
    eventdialogfont = ('courier', 13, 'bold')      # or inconsolata


# Event view/edit dialog's description text area size (new in [2.0])

eventdialogtextheight = 10      # number lines (None=default=5; Tk default=24)
eventdialogtextwidth  = None    # number characters (None=Tk default=80)


# See also controlsfont above, used for buttons in event-edit (and other) dialogs



#=====================================================================================
# SPECIAL-CASE FONTS (e.g., for Asian or monospace characters on Linux)
#=====================================================================================


#-------------------------------------------------------------------------------------
# Bold fonts can make some Asian characters (and possibly others) render unreadably
# on Linux, but bold seems to work well on Windows for all fonts, and non-bold seems
# too dull for other cases to be the default (though YMMV).  You may also want to
# use a larger font size here, but this is too subjective to set a policy here.
#-------------------------------------------------------------------------------------

LINUX_ASIAN_FONTS = False   # and/or test RunningOnLinux?

if LINUX_ASIAN_FONTS:
    daysfont        = ('arial', 9, 'normal')
    footerfont      = ('courier', 10, 'normal')
    eventdialogfont = ('courier', 12, 'normal')


#-------------------------------------------------------------------------------------
# Monospace fonts: platform-specific (currently unused - example only).
# Consolas isn't monospace on Linux, but inconsolata isn't monospace on Windows.
# Courier works for monospace on all three, but may have a duller appearance.
#-------------------------------------------------------------------------------------

MONOSPACE_FONTS = False

if MONOSPACE_FONTS:
    if RunningOnMac:                               # or monaco, courier
        daysfont = ('menlo', 10, 'bold')

    elif RunningOnWindows:                         # or courier
        daysfont = ('consolas', 10, 'bold')

    elif RunningOnLinux:                           # or courier                              
        daysfont = ('inconsolata', 10, 'bold')

    else:                                          # others?
        daysfont = ('courier new', 10, 'bold')



#=====================================================================================
# ICS CALENDAR FILE FORMATTING
#=====================================================================================


#-------------------------------------------------------------------------------------
# [1.4] Retain literal backslashes in Summary and Description text, via quoted-printable
# '=5C' notation escapes?  See version 1.4 notes in UserGuide.html for full details.
# If True, retains '\' but risks file portability: other GUIs may not undo '=5C' (if any).
# If False, drops some '\', and 2-char literal '\n' becomes 1-char newline on reloads.
#-------------------------------------------------------------------------------------

retainLiteralBackslashes = True          # True=escape and retain any literal '\'



#=====================================================================================
# CALENDAR AND IMAGE FOLDERS (last setting wins: multiple examples)
#=====================================================================================


#-------------------------------------------------------------------------------------
# iCalendar '.ics' event files folder path, with auto-created 'Backups' subfolder.
# All '*.ics' files in this folder are loaded as calendars at program start-up.
# The Backups subfolder saves prior versions of changed files before they are updated.
# DEFAULT is 'Calendars\*.ics' files, in subfolder of the main script's folder.
#-------------------------------------------------------------------------------------

icspath = r'C:\my-archived-folder\Calendar\ICSFiles'         # other folders
icspath = r'Calendars\subfolder-for-event-type'              # subsets
icspath = None                                               # None=DEFAULT


#-------------------------------------------------------------------------------------
# iCalendar '.ics' files 'Backup' subfolder maximum size.
# Keep up to this many latest backups of each .ics in 'icspath\Backups' subfolder.
#-------------------------------------------------------------------------------------

maxbackups = 10


#-------------------------------------------------------------------------------------
# Month image files folder path: 12 image files, mapped to months by sorted filename.
# Image files are displayed in a popup without resizing, if Images is toggled on in
# the GUI.  Requires Pillow install, unless you use PNGs on a Python using Tk 8.6+
# (e.g., Py3.4+ on Windows), or GIF/PPM/PPGs on any Py3.X [1.6].  To use images of
# your own, either change the default folder in-place, or change the path here.  The
# DEFAULT is 'MonthImages\*.{png, jpg, etc.}' files, in subfolder of script's folder.
#-------------------------------------------------------------------------------------

imgpath = r'C:\my-archived-folder\Calendar\MonthImages'      # other folders
imgpath = r'MonthImages\AlternateMonthImages\DrawnImages1'   # alternate sets
imgpath = r'MonthImages\AlternateMonthImages\DrawnImages1\WithTrees'
imgpath = r'MonthImages\AlternateMonthImages\OriginalLabeled\Small'
imgpath = r'MonthImages\AlternateMonthImages\OriginalLabeled\Large'
imgpath = None                                               # None=DEFAULT


#-------------------------------------------------------------------------------------
# On Linux + Mac: change any Windows '\' path separators to '/' [1.6].
# This code fixes paths if you keep the Windows '\' in the examples above.
#-------------------------------------------------------------------------------------

if not RunningOnWindows:
    if icspath: icspath = icspath.replace('\\', os.sep) 
    if imgpath: imgpath = imgpath.replace('\\', os.sep)      # either may be None



#=====================================================================================
# EVENT SUMMARY COLORS (by category name and/or calendar-file name)
#=====================================================================================


#-------------------------------------------------------------------------------------
# The following settings are meant as examples only: edit or replace as you prefer.
# Event category colors span calendars, and override any calendar color settings.
#
# To colorize events:
# 1) Edit the category and/or calendar color dictionaries here, giving either
#    a color name or #RRGGBB hex-code string for each color value.
# 2) Enter event category and calendar names in the GUI's View/Edit and Create
#    dialogs opened on event and day clicks, respectively.  An empty category
#    name in the GUI picks up either the calendar's color, or the color of a
#    category-dictionary entry whose key is an explicit empty string (a default). 
#
# See also the top of this file for:
#   -More on color setting values, and the chooser utility script "pickcolor.py"
#   -Notes about color name changes in in Tk 8.6+ (e.g., Python 3.4+ on Windows)
#   -Version 1.7's event foreground colors extension: color values can now be strings
#    giving background only, or (bg, fg) tuples giving both background and foreground
#
# Also note that the widget used to select from category names may have a limited
# size on some systems (e.g., Linux) and small screens; use fewer names if needed.
#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------
# CATEGORIES MAP: event category name => event summary widget color.
# Category entered in event's GUI, color = color name or RGB hex triple '#RRGGBB'.
# These span all calendars, and override calendar_colors below for specific events.
# Category name '' can be used to provide default for all events with no category.
# Default is 'white' if category's name is not listed here (and calendar not colored).
#-------------------------------------------------------------------------------------

category_ignorecase = True   # caseless lookup? (if True: travel=Travel, Travel=travel)


# Basic category names (color neutral)

category_colors = {
    'travel':           'tan',             # example names/colors: EDIT OR REPLACE
    'birthday':         'yellow',          # key=category, value='bg' or ('bg', 'fg')
    'anniversary':      'red',            
    'milestone':        'sky blue',
    'business':         'orange',
    'pybooks':          'pink',
    'education':         PURPLE,           # [1.6] differs in Tk 8.6+
    'politics':          MAROON,           # [1.6] differs in Tk 8.6+
    'weather':          'wheat',
    'conference':       'lavender',
    'gadgets':          'forest green',
    'other':            'light green'
    }


# Add any legacy categories (used in other calendars)

category_colors.update({
    'Red Category':     'red',
    'Green Category':    GREEN             # [1.6] differs in Tk 8.6+
    })


# Add any absolute color names (_x names appear early in list sort order);
# the leading '_' here is not significant - for sort order grouping only

category_colors.update({
    '_red':             'red',
    '_green':            GREEN,            # [1.6] differs in Tk 8.6+
    '_oldgreen':        'green',
    '_purple':           PURPLE,           # [1.6] differs in Tk 8.6+
    '_oldpurple':       'purple', 
    '_orange':          'orange',
    '_blue':            'sky blue',
    '_wheat':           'wheat',
    '_cyan':            'cyan',
    '_gray':             GRAY,             #[1.6] differs in Tk 8.6+
    '_yellow':          'yellow',
    '_lavender':        'lavender',
    '_violet':          'violet',
    '_dark red':        'indian red',
    '_beige':           'beige'            # plus _many_ more: see the web
    #,'':               'yellow'           # if used: a default category
    })


# [1.7] Add (bg, fg) color tuples (can also be mixed into other tables above);
# the leading '+' here is not significant - for sort order grouping only

category_colors.update({
    '+blues':           ('navy', 'white'),
    '+christmas':       ('dark green', 'red'),
    '+Важное событие':  ('black', 'orange'),
    '+purples':         ('purple', 'lavender'),       # key = 'category'
    '+packers':         ('green', 'gold'),            # value = 'bg' or ('bg', 'fg')
    '+broncos':         ('orange', 'blue'),
    '+seahawks☂':      ('navy', GREEN),
    '+重要事件':         ('indian red', 'white'),      # [1.7] non-English text 
    '+greens':          ('forest green', 'white'),    # [2.0] white foreground
    '+neons':           ('cyan', 'yellow'),
    '+goth':            ('black', GRAY),
    })


# For testing only: error cases and None=default

"""
category_colors.update({
    '+BAD1':            [1, 2, 3],
    '+BAD2':            (25,  'black'),               # fails on bg
    '+BAD3':            ('black', 25),                # fails on fg
    '+BAD4':            ('nonesuch', 'black'),
    '+BAD5':            ('black', 'nonsuch'),
    '+BADNonesuch':     'nonesuch',
    '+OKNone':          None,                         # None=''=nonmatch=>dflt
    })
"""


#-------------------------------------------------------------------------------------
# CALENDARS MAP: ics calendar file name => event summary widget color.
# File is basename (no path), color = color name or RGB hex triple '#RRGGBB'.
# These span all events in a calendar file, but category_colors above overrides these.
# Default is 'white' if a file's name is not listed here (and category not colored).
# Examples only: edit me (and okay if an ics file name in the table does not exist).
#-------------------------------------------------------------------------------------

calendar_colors = {                        # example names/colors: EDIT OR REPLACE
    'Bills.ics':        'cyan',            # key=filename, value='bg' or ('bg', 'fg')
    'Holidays.ics':     ('red', 'white'),  # [1.7] (bg, fg) tuple works here too
    'trips.ics':         GREEN,            # [1.6] differs in Tk 8.6+
    'business.ics':      GRAY,             # [1.6] differs in Tk 8.6+            
    'Personal.ics':     'beige'
    }             



#=====================================================================================
# END OF CODE (suggestions only follow)
#=====================================================================================



"""
======================================================================================

Examples of more advanced config techniques:

# 1) Proportional window height
initwinwide = 800
initwinsize = '%dx%d' % (initwinwide, int(initwinwide * .80))  # high=80% of wide

# 2) Window size per platform/version (e.g., if this implies distinct devices)
if RunningOnWindows:
    winversion = sys.getwindowsversion()
    majorminor = (winversion.major, winversion.minor)
    if majorminor >= (6, 2):
        initwinsize = '800x600'            # Windows 8=6.2, 8.1=6.3 (tablet?)
    else:
        initwinsize = '1000x800'           # Windows 7=6.1 (laptop/desktop?)
elif RunningOnLinux:
    initwinsize = '1000x800'               # Linux laptop?
else:
    initwinsize = '1000x800'               # Mac OS X laptop?

# 3) Scale window size to actual display (caveat: this pops up a temp window);
# *this has been subsumed* by a float/tuple initwinsize giving % of full screen,
# applied in frigcal.py automatically only after root Tk() window is created;

from tkinter import Tk
root = Tk()                                # get full screen size from tkinter GUI
swide = root.winfo_screenwidth()           # in pixels: (e.g., 1920)
shigh = root.winfo_screenheight()          # in pixels: (e.g., 1080)
root.destroy()
initwinsize = '%dx%d' % (int(swide * (2/3)),            # wide=2/3 of full screen
                         int(.80 * (swide * (2/3))))    # high=80% of width

# 4) Themes: prompt for a settings set/theme name in the console window at
# startup and choose from different assignment sets in this file with an 'if'

theme = input('theme?')         # 3.x only
if theme == 'blues':
    ...
    ...settings here, plus month images path?
    ...
elif theme == 'browns':
    ...
    ...other settings here
    ...
else:
    ...default settings here?
======================================================================================
"""
