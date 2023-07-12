"""
=====================================================================================
sharednames.py: common names used in both frigcal script and icsfiletools module.
Collected here so not coded redundantly in both files (and forgotten by updates!).
=====================================================================================
"""

# Python stdlib
import traceback, sys
from tkinter.messagebox import showerror
from tkinter import Tk

# constants
PROGRAM  = 'frigcal'
VERSION  = 2.0


# console messages
# set to (lamba *args: None) to turn off, and consider a .pyw on Windows
# trace = print

# [1.7] print \u escapes to suppress exceptions if non-ASCII text goes to a console
# which doesn't handle it, but special-case to avoid enclosing quotes for ASCII text;
# this is an issue on Windows in general, and on Mac OS X for GUIs run with no console;
# isascii() could be generalized for any code via functions--def tryit(func): try: func(),
# and tryit(lambda: parg.encode('ascii'))--but then which exceptions should imply False?;

def trace(*pargs, **kargs):
    def isascii(text):
        try:    text.encode('ascii')
        except: return False
        else:   return True
    print(*((parg if isascii(parg) else ascii(parg)) for parg in pargs), **kargs)


def startuperror(message):
    """
    [1.5] show an error message as a GUI popup and shutdown, before the
    actual GUI has been built; used by filepath/parser errors here, but
    elsewhere for import errors for configs file and icalender 3rd party
    lib;  none of these can print to the console only (or expect input from
    it), as there may be no console on Windows, and GUI users expect GUIs;
    caller adds sys.exc_info and traceback to message if appropriate;
    must be here: imported from frigcal, which is not yet fully formed; 
    """
    traceback.print_exc()             # exc to console, but also a GUI popup
    root = Tk()                       # no GUI yet: make a dummy, hidden root
    root.iconify()
    showerror('%s: Startup Error' % PROGRAM, message)
    sys.exit(1)  # fatal errors: can't continue


# local: helper class to provide defaults for missing attrs [1.2]
from attributeproxy import AttributeProxy

# local: user config options - colors, fonts, paths, modes
try:
    import frigcal_configs                                    # formerly: as Configs
except:
    # catch errors in configs file, [1.5]: plus GUI popup
    exctext = traceback.format_exc()
    errtext = ('Error while loading configs file.\n\n'
        'An error in frigcal_configs.py is preventing frigcal start.\n\n'
        "Please correct this file's error or restore a backup copy.\n"
        'You can import this module by itself in Python to debug it.\n'
        "The error returned by Python for frigcal's import follows:\n\n")
    startuperror(errtext + exctext)
    
else:
    Configs = AttributeProxy(frigcal_configs, warnof=True)    # okay: wrap for defaults [1.2]


# defaults
Configs.icspath = Configs.icspath or 'Calendars'      # in '.', calendars = all *.ics
Configs.imgpath = Configs.imgpath or 'MonthImages'    # in '.', 12 *.{jpg, gif, etc.}

