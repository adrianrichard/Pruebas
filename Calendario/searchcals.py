#!/usr/bin/env python3
"""
=====================================================================================
searchcals.py: frigcal calendar-search utility script.

[2.0] This command-line tool searches all your frigcal calendar files' events
for a keyword, in event summaries, descriptions, categories, or all three.  It
prints matching events' calendars and dates (in mm/dd/yyyy format and sorted by
date), to help you access them quickly in the frigcal main script's GUI.

For instance, you can jump to a matching event listed in this script's output
by entering its date in the GUI's GoTo input field in mm/dd/yyyy format, and
pressing Enter or GoTo.  The GUI will move to the event's month and highlight
its day tile.  In fact, dates output here can be copy-and-pasted into the GoTo
field directly (try Ctrl-c/v on Windows and Linux, and Command-c/v on Mac OS X).

This script is launched from and prints to a command-line interface (e.g.,
Terminal on Mac and Linux, and Command Prompt on Windows), and should be run
in your frigcal install folder, because it uses your normal frigcal_configs.py
settings to locate your calendar files in the same fashion as the GUI.
See also README.txt for running scripts in frozen app/executable packages.

-------------------------------------------------------------------------------------
USAGE

Example: search for occurrences of "bread" in all fields on Windows.

    (open Command Prompt)
    C:\...\somedir> cd C:\...\frigcal
    C:\...\frigcal> py -3 searchcals.py bread -all

Example: search for all occurrences of "french" in summaries on Mac or Linux.

    (open Terminal)
    /.../somedir$ cd /.../frigcal
    /.../frigcal$ python3 searchcals.py french -sum

Format:
    [python] searchcals.py searchfor (-sum | -des | -cat | -all)
    
where:
    [python] is your Python's name, and optional on some installs
    
    searchfor stands for the term you wish to find
        quote multiple words: use "new york" on Windows, 'new york' on Unix
        the search is always case-insensitive (e.g., 'a' == 'A')

    one of the four items in the (...) is used to specify a mode
        -sum finds events having searchfor in summary fields only
        -des finds events having searchfor in description fields only
        -cat finds events having searchfor in category fields only
        -all finds events having searchfor in summary, description, or category
    
Search is implemented by this command-line script and is not part of the GUI
itself, because adding this to the GUI would complicate an intentionally
simplistic interface for a very rare use case.  Coding note: much of this
script parrots parts of icsfiletools.py (which is too GUI-oriented to reuse).

-------------------------------------------------------------------------------------
FULL EXAMPLE RUNS

The first two of the following run on Windows, the third on Unix (Mac OS X).

C:\...\frigcal> searchcals.py nasa -all
Using Python 3.5 and Tk 8.6
Searching for 'nasa' in -all
Parsing all calendars in Calendars
Searching calendar frigcal-default-calendar.ics
    FOUND on date 07/05/2015
    FOUND on date 07/15/2015
    FOUND on date 08/04/2015
    FOUND on date 08/24/2015
    FOUND on date 08/25/2015
    FOUND on date 08/26/2015
    FOUND on date 12/31/2015
Searching calendar Holidays.ics
Searching calendar trips.ics
Searching calendar working--Full-Calendar-From-Outlook-July1112.ics
    FOUND on date 08/30/2005
    FOUND on date 08/31/2005
    FOUND on date 09/01/2005
    FOUND on date 05/13/2011
Number matches found: 11

C:\...\frigcal> searchcals.py "las vegas" -sum
Using Python 3.5 and Tk 8.6
Searching for 'las vegas' in -sum
Parsing all calendars in Calendars
Searching calendar frigcal-default-calendar.ics
    FOUND on date 12/11/2016
    FOUND on date 01/08/2017
Searching calendar Holidays.ics
Searching calendar trips.ics
Searching calendar working--Full-Calendar-From-Outlook-July1112.ics
    FOUND on date 09/18/2006
Number matches found: 3

/.../frigcal$ python3 searchcals.py 'new york' -sum
Using Python 3.5 and Tk 8.5
Searching for 'new york' in -all
Parsing all calendars in Calendars
Searching calendar frigcal-default-calendar.ics
Searching calendar Holidays.ics
Searching calendar trips.ics
Searching calendar working--Full-Calendar-From-Outlook-July1112.ics
    FOUND on date 12/13/2005
    FOUND on date 12/14/2005
    FOUND on date 12/15/2005
Number matches found: 3
=====================================================================================
"""

import os   # for chdir

# [2.0] for frozen app/exes, fix module+resource visibility (sys.path)
import fixfrozenpaths

# [2.0] make relative calendar paths map to frigcal's install folder
os.chdir(fixfrozenpaths.fetchMyInstallDir(__file__))   # absolute


import sys, glob, shutil, traceback, time, datetime
from sharednames import Configs, trace
import icalendar  # required 3rd-party package


def parse_and_search_ics_files(searchfor, mode):
    """
    load events from ics file(s), search for search term per mode arg;
    on any exception here, script aborts: there is no way to proceed;
    this mimics icsfiletools.parse_ics_files, which has docs cut here;
    """
    nummatches = 0
    trace('Parsing all calendars in', Configs.icspath)
    icsfiles = glob.glob(os.path.join(Configs.icspath, '*.ics'))

    # parse/index each ics file's data
    for icsfile in icsfiles:                                        # for all ics files in folder
        icsfilenopath = os.path.basename(icsfile)                   # strip directory path prefix
        trace('Searching calendar', icsfilenopath)

        # read ics text: use config=ics Unicode default (bytes works too)
        unicode = icalendar.parser.DEFAULT_ENCODING                 # changeable in source code only
        calfile = open(icsfile, 'r', encoding=unicode)              # [1.7] but don't hardcode 'utf8'
        try:
            icstext = calfile.read()                                # all at once: small files
        finally:
            calfile.close()                                         # exc or not (not 'with': eibti)

        # parse ics text: 3rd party package(s), major dependency
        icsarray = icalendar.cal.Calendar.from_ical(icstext)        # .cal optional but explicit

        # extract data used here, find searchterm
        calmatches = []
        for event in icsarray.walk('VEVENT'):                       # for all events in parsed calendar

            # icalendar.prop.vDDDTypes: .dt is datetime.{date or datetime} with .m/d/y
            startdate = event['DTSTART']                # required start date

            # icalendar.prop.vText (VText): .to_ical() is bytes, str() decodes auto
            labeltext = event.get('SUMMARY', '')        # for main label, and view/edit dialog
            extratext = event.get('DESCRIPTION', '')    # for footer, and view/edit dialog
            category  = event.get('CATEGORIES', '')     # for coloring, and view/edit dialog
            if isinstance(category, list):
                category = category[0]                  # if multiple, use just one (first) for coloring

            # neutralize case differences (probably a good thing)
            searchfor = searchfor.lower()
            labeltext = labeltext.lower()
            extratext = extratext.lower()
            category  = category.lower()
            
            match = (
                (mode == '-sum' and searchfor in labeltext) or
                (mode == '-des' and searchfor in extratext) or
                (mode == '-cat' and searchfor in category)  or
                (mode == '-all' and searchfor in labeltext + ' ' + extratext + ' ' + category))

            if match:
                # order parts for later sorting here
                nummatches += 1
                dt = startdate.dt
                dateforsort = dt.year, dt.month, dt.day
                calmatches.append(dateforsort)

        # report this calendar's matches        
        if calmatches:
            # order same as GUI's GoTo input here for copy/paste
            for (yyyy, mm, dd) in sorted(calmatches):
                print('    FOUND on date %02d/%02d/%04d' % (mm, dd, yyyy))
                
        # goto next icsfile calendar
    return nummatches


if __name__ == '__main__':
    usage = 'Usage: [python] searchcals.py searchfor (-sum | -des | -cat | -all)'
    if len(sys.argv) != 3:
        print(usage)
    elif sys.argv[2] not in ['-sum', '-des', '-cat', '-all']:
        print(usage)
    else:
        searchfor, mode = sys.argv[1:3]
        print('Searching for', repr(searchfor), 'in', mode)
        nummatches = parse_and_search_ics_files(searchfor, mode)
        print('Number matches found:', nummatches)
