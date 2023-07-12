"""
=====================================================================================
icsfiletools.py: frigcal's iCalendar (".ics") event files interface functions.

Tools to initialize, parse, edit, backup, and save ics iCalendar file(s).
Parser and generator rely on 3rd-party icalendar package, shipped with the
standard zip file, but perhaps not in redistributions (see UserGuide.html).

Note: this file contains 3 non-ASCII Unicode characters, but they work with
Python 3.X's default UTF8 source-code encoding, without a "# -*- coding" line.
=====================================================================================
"""

# Python stdlib
import os, sys, glob, shutil, traceback, time, datetime

# some errors here (TBD: move these to frigcal.py?)
# [1.5] startup errors (parser, file) are not caught/dispayed here (in main())
from tkinter.messagebox import showerror, showwarning


# local: names used in both frigcal script and icsfiletools (avoid redundant code)
from sharednames import Configs, trace, PROGRAM, VERSION, startuperror


# 3rd-party: ensure installed now, used in this file only
try:
    import icalendar                          # [1.5] console + GUI popup
except ImportError:
    # catch missing required packages 
    errtext = ('Error trying to import 3rd-party libraries.\n\n'
        'Required icalendar and/or pytz 3rd-party packages are not installed.\n\n'
        'See Dependencies in UserGuide.html, and fetch the required code from '
        'https://pypi.python.org/pypi/icalendar and https://pypi.python.org/pypi/pytz.')
    startuperror(errtext)   # no exc info
    # plus sys.exit(1) in startuperror
    

# [1.7] alas, cannot reset icalendar's default before it's import "from" (punt!)
# icalendar.parser_tools.DEFAULT_ENCODING = Configs.icsfilesUnicodeEncoding

from icalendar.parser import unescape_char          # currently unused
from icalendar.parser import escape_char, foldline  # [2.0] for Unicode file text


#====================================================================================
# ICS events data structures: created here, used here and in frigcal.py
#====================================================================================
"""
Global calendar and event data structures.
These are created, used, and changed here; and imported and used in frigcal.py.
Classes are used to give mnemonic attr names instead of positional index/unpack.

About EventsTable:

Events from all calendars are stored in a 2-level table, indexed by date and
unique id (UID) for quick access to both displayed and parsed data.   Because
events in the table are stamped with their calendar name, there is no need to
segregate by a 3rd calendar dimension (an initial design) --  the GUI displays
the union of all calendar files' events, and a single combined table still
supports display grouping by calendar, via sorts.

Events in the table also have links back to their parsed icalendar object for
fast in-place updates in memory (files are regenerated only on exit), and GUI
month windows keep UID-indexed tables of displayed events for quick deletion.
This model assumes events have UIDs, but the iCalendar standard requires these. 

Logical model:
EventsTable index uses 2-level dictionary table nesting: [date][uid]

CalendarsTable =               # Parsed file's raw calendar data (all data)
    {icsfilename:              # key: basename of .ics file parsed
         icalendar.cal         # icalendar.cal object, from parser    
    }

EventsTable =                  # Union of all events in all ics files (used data)
    {(m, d, y):                # key: date object for event start (and display) date
        {uid:                  # key: event's required unique id, for fast deletes
            (.calendar,        # ics file name
             .summary,         # event summary text
             .description,     # event description text
             .category,        # category (just 1/first used)
             .uid,             # event's required unique id, for easy access
             .orderby,         # creation (or else mod) date: display order sort
             .veventobj)       # reference link to vevent in icalendar.cal object
        }
    }

Release [1.1] addition (a new table to minimize code impacts):
CalendarsDirty =
    {icsfilename:              # key: basename of .ics file parsed
         Boolean               # True=calendar changed since startup or latest save
    }

Subtlety: IN-PLACE CHANGE to mutable objects shared by multiple references is
crucial in this model.  EventsTable index objects are referenced from registered
GUI event handlers, and there is just one copy of each CalendarsTable parsed
icalendar array, referenced from index objects and used at file regeneration time.
"""
#------------------------------------------------------------------------------------

# in code

CalendarsTable = {}    # {icsfilebasename: icalendar.cal.Calendar()}

EventsTable = {}       # {Edate(): {uid: EventData()} ]

CalendarsDirty = {}    # {icsfilebasename: Boolean} [1.1]


class Edate:
    """
    encapsulate and name event date numbers
    """
    def __init__(self, month, day, year):
        self.month = month                          # a namedtuple may do some of this, but not all
        self.day = day
        self.year = year

    @staticmethod                                   # copy datetime.{date, datetime} object attrs 
    def from_datetime(dateobject):                  # staticmethod optional if 3.X class calls only
        return Edate(dateobject.month, dateobject.day, dateobject.year)

    def to_datetime_date(self):
        return datetime.date(**self.__dict__)       # copy attrs to a datetime.date object

    def as_tuple(self):
        return (self.month, self.day, self.year)

    def as_string(self):
        return '%02d/%02d/%4d' % self.as_tuple()    # formatted display

    # support use in dictionary key, comparisons, sort key
    
    def __hash__(self):
        return hash(self.as_tuple())                # dictionary key (else by addr)
    
    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()  # comparisons (else by addr) 

    def __lt__(self, other):                        # sort keys (else fails)
        """
        [1.4] order events on dates by year first (y-m-d), not month;
        but keep as_tuple() format (m-d-y): it's also used for displays;
        was originally: return self.as_tuple() < other.as_tuple()
        """
        return ((self.year,  self.month,  self.day) <
                (other.year, other.month, other.day))

        
class EventData:
    """
    maximal attrs set, for both icsindex and widget values
    """
    def __init__(self,
        uid='', calendar='', summary='', description='', category='', orderby='', veventobj=None):
        
        self.uid = uid                      # event unique id, required by iCalendar std
        self.calendar = calendar            # calendar file's basename (not path)
        self.summary = summary              # for event summary in month, elsewhere
        self.description = description      # for extra text in footer, edit dialog
        self.category = category            # for colorizing event summary entries
        self.orderby = orderby              # for ordering events entries initially
        self.veventobj = veventobj          # a reference to icalender object: updates, deletes

        # or: for (name, value) in kargs.update(defaults): setattr(self, name, value)
        
    def copy(self):
        return EventData(**self.__dict___)  # use attrs dict for keyword args


#====================================================================================
# ICS events file parser: creates/returns in-memory data from file(s) 
#====================================================================================

def parse_ics_files():
    """
    load events from ics file(s), once at startup;
    on any exception here, script aborts (with popup+message): no way to proceed;
    don't reinitialize tables here: they are already imported by object via 'from'!;
    any errors here are caught and displayed by the caller: the data may be bad;
    calendar paths are relative to ".": frigcal.py os.chdir()s to install folder;

    VTEXT is a str subclass, and works as is: no extra str() conversion is needed;
    icalendar uses the UTF8 iCalendar default Unicode encoding scheme throughout;
    from_ical parse auto unescapes any "\X" icalendar sequences and does Unicode decoding;
    to_ical generate auto adds "\X" escapes if needed and does Unicode encoding;
    see also the note about reading all at once here, in generate_ics_files() ahead;
    """
    global CalendarsTable, EventsTable
    trace('Parsing', Configs.icspath)
    icsfiles = glob.glob(os.path.join(Configs.icspath, '*.ics'))

    # parse/index each ics file's data
    for icsfile in icsfiles:                                        # for all ics files in folder
        trace('loading', icsfile, '...')
        icsfilenopath = os.path.basename(icsfile)                   # strip directory path prefix
        
        # read ics text: use config=ics Unicode default (bytes works too)
        unicode = icalendar.parser.DEFAULT_ENCODING                 # changeable in source code only
        calfile = open(icsfile, 'r', encoding=unicode)              # [1.7] but don't hardcode 'utf8'
        try:
            icstext = calfile.read()                                # all at once: small files
        finally:
            calfile.close()                                         # exc or not (not 'with': eibti)

        # parse ics text: 3rd party package(s), major dependency
        icsarray = icalendar.cal.Calendar.from_ical(icstext)        # .cal optional but explicit
        CalendarsTable[icsfilenopath] = icsarray                    # add to global calendars table
        CalendarsDirty[icsfilenopath] = False                       # no changes yet at startup [1.1]

        # extract data use here, index by start date and uid
        for event in icsarray.walk('VEVENT'):                       # for all events in parsed calendar

            # icalendar.prop.vDDDTypes: .dt is datetime.{date or datetime} with .m/d/y
            startdate = event['DTSTART']                # required start date
            datestamp = event['DTSTAMP']                # required modtime: display order if no created
            createdon = event.get('CREATED', None)      # optional createtime: for display order

            # icalendar.prop.vText (VText): .to_ical() is bytes, str() decodes auto
            uniqueid  = event['UID']                    # required id, for update searches
            labeltext = event.get('SUMMARY', '')        # for main label, and view/edit dialog
            extratext = event.get('DESCRIPTION', '')    # for footer, and view/edit dialog
            category  = event.get('CATEGORIES', '')     # for coloring, and view/edit dialog

            if isinstance(category, list):
                category = category[0]                  # if multiple, use just one (first) for coloring

            # vdates: .dt is a datetime.date/datetime object
            # transfer to custom date type for better control here
            eventdate = Edate.from_datetime(startdate.dt)
            if createdon:
                orderdate = Edate.from_datetime(createdon.dt)
            else:
                orderdate = Edate.from_datetime(datestamp.dt)

            # vtext: see above--ok as is, but undo odd '\X' escapes in some existing data
            labeltext = labeltext.replace('\\"', '"')
            extratext = extratext.replace('\\"', '"')       # '\"' -> '"'
            
            # [1.4] undo =5C's from file, restoring '\'; see unescape function ahead
            labeltext = backslash_unescape(labeltext)
            extratext = backslash_unescape(extratext)       # '=5C' -> '\'
            
            # index this file's event data for date by start m/d/y
            icsdata = EventData(uid=uniqueid,
                                calendar=icsfilenopath,
                                summary=labeltext,
                                description=extratext,
                                category=category,
                                orderby=orderdate,
                                veventobj=event)
            
            if eventdate not in EventsTable.keys():            # .keys(), bcause EIBTI
                EventsTable[eventdate] = {}                    # first event for this date
            EventsTable[eventdate][uniqueid] = icsdata         # add to global events union table


#====================================================================================
# ICS events edits: update in-memory data structures (run from event edit callbacks)
#====================================================================================


def add_event_data(edate, widgetdata):
    """
    add new or pasted event to data structures (GUI updates GUI);
    uses new widgetdata (GUI) with new uid, edate is true date;
    """
    newuid = widgetdata.uid
                     
    # new icalendar event object
    newvevent = new_vevent(
        uid=newuid,
        summary=widgetdata.summary,
        dtstart=edate.to_datetime_date(),
        description=widgetdata.description,
        category=widgetdata.category)
    icscalendar = CalendarsTable[widgetdata.calendar]
    icscalendar.add_component(newvevent)         # add to parsed data's list-like object
    CalendarsDirty[widgetdata.calendar] = True   # change: backup and write file on close [1.1]

    # new used-data index
    datenow  = datetime.date.today()             # datetime.date(y,m,d)
    edatenow = Edate.from_datetime(datenow)      # to own date for compares in sorts
    newicsdata = widgetdata                      # no .copy() needed: made anew in dialog
    newicsdata.veventobj = newvevent             # link for update/delete later in this session
    newicsdata.orderby   = edatenow              # set for window refills later in this session
    if edate not in EventsTable.keys():
        EventsTable[edate] = {}
    EventsTable[edate][newuid] = newicsdata


def delete_event_data(edate, icsdata):
    """
    delete event from data structures (GUI deletes GUI);
    uses existing icsdata (index);
    if no more vevents on exit, one is added then (not here);
    """
    # delete from icalendar event object              
    icscalendar = CalendarsTable[icsdata.calendar]
    vevent = icsdata.veventobj                     # link: avoid rewalk search
    icscalendar.subcomponents.remove(vevent)       # assumes object compares work!
    CalendarsDirty[icsdata.calendar] = True        # change: backup and write file on close [1.1]

    # delete from used-data index
    uid = icsdata.uid
    del EventsTable[edate][uid]        # remove known event from date table
    if not EventsTable[edate]:         # also remove date if events now empty     
        del EventsTable[edate]


def update_event_data(edate, icsdata, widgetdata):
    """
    update event in data structures (GUI updates GUI);
    uses both icsdata (index) and widgetdata (gui);
    
    IN-PLACE change via references to shared, single objects is crucial
    for both icscalendar and index items, as index objects are registered
    for events, and there's just one icscalender object used at file
    regenerations time; in fact, cidata IS icsdata here: it could be
    updated more directly than currently done here;
    """
    # update icalendar event object (in-place!)         
    vevent = icsdata.veventobj                     # link: avoid rewalk search
    update_vevent(                                 # assumes in-place changes work!
        vevent,
        widgetdata.summary,
        widgetdata.description,
        widgetdata.category)
    CalendarsDirty[icsdata.calendar] = True        # change: backup and write file on close [1.1]

    # update used-data index (in-place!)
    uid = icsdata.uid
    cidata = EventsTable[edate][uid]
    cidata.summary     = widgetdata.summary
    cidata.description = widgetdata.description
    cidata.category    = widgetdata.category
    assert cidata is icsdata  # sanity check


def update_event_summary(icsdata, summary):
    """
    update exiting vevent object's summary only, in-place;
    used by Return key callback for inline summary field edits;
    """
    vevent = icsdata.veventobj                 # linked vevent object
    update_vevent_summary(vevent, summary)     # update icalendar data (in-place!)
    CalendarsDirty[icsdata.calendar] = True    # change: backup and write file on close [1.1] 


#------------------------------------------------------------------------------------

"""
interface with the icalendar API to set/update data in its objects
obj.add(field, value) converts to internal types based on field + value;
obj['field'] = val does not convert, and can leave some as invalid text;
"""

def replace_vevent_property(vevent, name,  value):
    # TBD: there seems no way to change apart from deleting and adding anew
    if name in vevent:
        del vevent[name]      # optional items may be missing (categories)
    vevent.add(name, value)   # use field-specific library type encoding


"""
[1.4] workaround for unwanted transforms in the underlying icalendar lib:
else these wind up dropping their literal '\' in transit to/from the file,
and a 2-char literal '\n' in a text field is changed to a 1-char newline;
to verify, enter text [a\nb\nc\;d\,e"f\"g] in a Summary or Description:
its backslashes should save and load intact (all are mutated/dropped by the
underlying lib without this patch);  or, in Python, where \\ means \:

>>> text = 'a\nb\nc\;d\,e"f\"g'                   # escapes interpreted
>>> text = 'a\\nb\\nc\\;d\\,e"f\\"g'              # each '\\' is 1 '\'
>>> e = text.replace('\\', '=%2X' % ord('\\'))
>>> e
'a=5Cnb=5Cnc=5C;d=5C,e"f=5C"g'
>>> u = text.replace('=%2X' % ord('\\'), '\\')
>>> u
'a\\nb\\nc\\;d\\,e"f\\"g'

TBD: better solution in ics lib?  this patch seems a hack, but the ics lib
is undocumented and convoluted, and literal backslashes seem likely to be very
rare in user text;  an earlier version escaped just [r'\n', r'\;', r'\,', r'\"'];
*CAVEAT*: this risks file portability, as it uses quoted-printable notation
which may not be recognized by other calendar programs (a non-issue if there are
no '\' or frigcal is the sole file user) --> made patch switchable in Configs;
"""

# warn of default just once if missing
retainLiteralBackslashes = Configs.retainLiteralBackslashes

def backslash_escape(text):
    # escape text from gui, all '\' -> '=5C'?
    if not retainLiteralBackslashes:
        return text
    else:
        return text.replace('\\', '=%2X' % ord('\\'))
    
def backslash_unescape(text):
    # unescape text from file, all '=5C' -> '\'?
    if not retainLiteralBackslashes:
        return text
    else:
        return text.replace('=%2X' % ord('\\'), '\\')


def update_vevent_summary(vevent, summary):
    """
    update exiting vevent object's summary only in-place
    isolate icalendar library api details here
    """
    summary = backslash_escape(summary)            # [1.4] '\' -> '=5C'?
    replace_vevent_property(vevent, 'SUMMARY', summary)
    

def update_vevent(vevent, summary, description, category):
    """
    update exiting vevent object in-place
    isolate icalendar library api details here
    """  
    timenow = datetime.datetime.today()            # datetime.datetime(y,m,d,h,m,s,ms)

    summary     = backslash_escape(summary)        # [1.4] '\' -> '=5C'?
    description = backslash_escape(description)
    
    replace_vevent_property(vevent, 'SUMMARY',     summary)
    replace_vevent_property(vevent, 'DESCRIPTION', description)
    replace_vevent_property(vevent, 'CATEGORIES',  category)        # just one here
    replace_vevent_property(vevent, 'DTSTAMP',     timenow)         # set new modtime: raw dt


def new_vevent(uid, summary, dtstart, description, category):
    """
    make new vevent object for new event, via icalendar api;
    isolate icalendar library api details here;
    dtstart is a datetime.date object for clicked date on Add
    dialogs, else None when making a new event on current date;
    """
    datenow = datetime.date.today()                # datetime.date(y,m,d)
    timenow = datetime.datetime.today()            # datetime.datetime(y,m,d,h,m,s,ms)

    summary     = backslash_escape(summary)        # [1.4] '\' -> '=5C'?
    description = backslash_escape(description)
        
    vevent = icalendar.Event()
    vevent.add('UID',         uid)
    vevent.add('SUMMARY',     summary)             # or [key]=val (see above)
    vevent.add('DTSTART',     dtstart or datenow)  # event's start date
    vevent.add('DTSTAMP',     timenow)             # vevent mod time                 
    vevent.add('CREATED',     timenow)             # vevent creation time
    vevent.add('DESCRIPTION', description)         # a vtext, but str works here
    vevent.add('CATEGORIES',  category )           # or a list (but frigcal uses just 1)
    return vevent


#====================================================================================
# ICS events file generator: save in-memory data to ics file(s)
#====================================================================================

def generate_ics_files():
    """"
    store events in ics file(s), once at exit (and only after good backup);
    
    [1.5] note: calendar files are written here, and read in the parse function, all
    at once with .read() and .write(all), not in chunks via .read(N) and .write(part);
    these files are relatively small (the developer's largest is 876K for 12 years),
    and arbitrary buffer sizes should work on all platforms under Python 3.X today;
    an old Windows issue precluded writing buffers > 64M on network drives, but is
    fixed in recent libs (and 64M equates to 897 comparable years of events for the
    developer!); for more details and a chunk-based coding, see docetc\__chunkio__.py;
    """
    trace('Generating', Configs.icspath)
    for icsfilename in CalendarsTable.keys():                 #  .keys() optional but explicit
        if not CalendarsDirty[icsfilename]:
            # no changes since startup or save: don't backup/write this file [1.1]
            continue
        
        try:
            icsfilepath = os.path.join(Configs.icspath, icsfilename)
            icscalendar = CalendarsTable[icsfilename]

            if not icscalendar.walk('VEVENT'):    # a list
                # if no events remain after deletes, add a required one now (rare but true)
                vevent = new_vevent(                                  # fix name error [1.5]
                    dtstart=None,
                    uid=icalendar_unique_id() + '-' + icsfilename,    # make unique if > one [1.5]
                    summary='%s-generated event' % PROGRAM,
                    description='Required sole event generated.\n'    # add pointer text [1.5]
                                'To completely remove this calendar from the GUI,\n'
                                'delete its ics file from your Calendars folder.',
                    category='_dark red')                             # [2.0] color? (else white)
                icscalendar.add_component(vevent)                     # was 'system internal'

            trace('writing', icsfilepath, '...')
            text = icscalendar.to_ical()                       # big dependency, this!
            #tofile = open(icsfile, 'w', encoding='utf8')      # use ics default encoding?
            tofile = open(icsfilepath, 'wb')                   # actually, text is bytes not str
            try:
                tofile.write(text)                             # all at once: small files
            finally:
                tofile.close()                                 # flush, exc or not (with?: eibti)
            CalendarsDirty[icsfilename] = False                # no changes since last saved [1.1]

        except:
            # console message + popup dialog, skip file but keep going ([1.4] help pointer)
            traceback.print_exc()
            showerror('%s: Generate Error' % PROGRAM,
                'Error while generating file "%s".\n\n'
                'Prior version retained in Backups.\n'
                'See "Handling Backup/Save Errors" in "?" help for more details.\n\n'
                'Python exception text follows:\n\n%s\n%s'
                % (icsfilename, sys.exc_info()[0], sys.exc_info()[1]))
                

#====================================================================================
# ICS events file backup: copy ics file(s) to backup folder
#====================================================================================

def backup_ics_files(maxbkps=Configs.maxbackups):
    """
    backup ics files to subdir prior to saving new data (always!)
    automatically prunes oldest version(s) of files in Backups if needed;
    
    TBD: should backups no longer matching a calendar name in .. be removed?
    if not, renames can leave old backups, but users can delete these too,
    and it's not clear that deleting backups for a prior file is warranted;
    """
    trace('Backing up', Configs.icspath)
    allbackupspath = os.path.join(Configs.icspath, 'Backups')
    if not os.path.exists(allbackupspath):
        try:
            os.mkdir(allbackupspath)    # make backup folder if needed
        except:
            # initial mkdir failure
            taceback.print_exc()
            trace(sys.exc_info())
            showerror('%s: Backup Error' % PROGRAM,
                      'Error creating Backup subfolder: save cancelled.')
            return False

    for icsfilename in CalendarsTable.keys():
        if not CalendarsDirty[icsfilename]:
            # no changes since startup or save: don't backup/write this file [1.1]
            continue

        try:
            # trim backups folder if needed
            # keeps most recent N-1 of each, based on sort order of bkp names

            basename = icsfilename
            backuppatt  = 'date*-time*--' + basename
            currbackups = glob.glob(os.path.join(allbackupspath, backuppatt))
            currbackups.sort(reverse=True)
            prunes = currbackups[(Configs.maxbackups - 1):]      # earliest last
            for prunee in prunes:                                # globs have paths
                trace('pruning', prunee)
                try:                                             # [1.5] file deletes can fail:
                    os.remove(prunee)                            # but don't cancel bkp/save
                except:
                    traceback.print_exc()                        # or trace(sys.exc_info())
                    showwarning('%s: Pruning Error' % PROGRAM,
                       'Error while pruning file:\n"%s"\n\n'
                       'File skipped, but backup/save continued.\n\n'
                       "If not deleted on next backup/save, check this file's permissions."
                        % prunee)

            # transfer current file to back folder/name
            # TBD: move is quick and may be less error prone,
            # but copy retains original file in case save fails

            pathname = os.path.join(Configs.icspath, icsfilename)
            datetimestamp = time.strftime('date%y%m%d-time%H%M%S')          # add date/time prefix
            backupname = '%s--%s' % (datetimestamp, basename)
            backuppath = os.path.join(allbackupspath, backupname)
            trace('saving', pathname, '\n\tto', backuppath)
            shutil.copy2(pathname, backuppath)                              # copy content (write)
                                       
            # OR: os.rename(icsfile, backuppath)                            # or move quickly?
            # OR: open(backuppath, 'wb').write(open(icsfile, 'rb').read())  # or manual copy?
            
        except:
            # on any and first failure for this file ([1.4] help pointer)
            traceback.print_exc()
            showerror('%s: Backup Error' % PROGRAM,
                   'Error while backing up file "%s".\n\n'
                   'Save cancelled, prior backups retained.\n'
                   'See "Handling Backup/Save Errors" in "?" help for more details.\n\n'
                   'Python exception text follows:\n\n%s\n%s'
                    % (icsfilename, sys.exc_info()[0], sys.exc_info()[1]))
            return False  # give up now: won't save, so no reason to backup any others
    
    return True  # True = all worked, False = failed and stopped


#====================================================================================
# ICS events file creation: default file, or new files on request
#====================================================================================

# make a new .ics iCalendar file with one event: a truly empty file does not work;
# see UserGuide.html for iCalendar support model, the standard, and example content;
# icalendar API can make these strings too (see new_vevent() above), but text is easy;
# this logic is also used by makenewcalendar.py script, with name input at console,
# but not by empty-calendar logic in generate code above (uses new_vevent() API);


# calendar template:
# requires 'version' + 'prodid', and at least 1 nested component
initfile_calendartext = \
"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:%(program)s %(version)s
%(event)s
END:VCALENDAR"""


# nested event component template:
# requires 'uid' + 'dtstamp' (+ 'dtstart' if no cal 'method')
# [2.0] use Unicode symbols and make this event more descriptive
# [2.0] use preset colored category: if it doesn't exist, uses white
initfile_eventtext = \
"""BEGIN:VEVENT
DTSTART;VALUE=DATE:%(dtstart)s
SUMMARY:✓ Calendar created
DESCRIPTION:☞ Your %(calname)s iCalendar ics file was generated ☜
 \\nIt is stored in your Calendars folder\\, and can now be selected in the
 \\nCalendar pulldown of event-edit dialogs opened on day clicks and pastes.\\n
CATEGORIES:%(category)s
CREATED:%(created)s
DTSTAMP:%(dtstamp)s
UID:%(uid)s
X-%(program)s-VERSION:%(version)s
END:VEVENT"""


# [2.0] when the default event is generated in first run, also make
# an event that gives the text of the Unicode cheatsheet file; this
# has been too obscure to find, and seems important to underscore
initunicode_eventtext = \
"""BEGIN:VEVENT
DTSTART;VALUE=DATE:%(dtstart)s
SUMMARY:Unicode cheatsheet
DESCRIPTION:%(filetext)s
CATEGORIES:_wheat
CREATED:%(created)s
DTSTAMP:%(dtstamp)s
UID:%(uid)s
X-%(program)s-VERSION:%(version)s
END:VEVENT"""


def init_default_ics_file(forcename=''):
    """
    if forcename is passed in, make a new calendar file with basename = forcename;
    else make a default calendar file if no .ics is present on first (or later) startup;
    any errors here are caught and displayed by the caller: the path setting may be bad;
    """
    if forcename or not glob.glob(os.path.join(Configs.icspath, '*.ics')):
        basename = forcename or ('%s-default-calendar.ics' % PROGRAM)
        initfilepath = os.path.join(Configs.icspath, basename)
        trace('Creating new calendar file:', initfilepath)          # not 'initial' [1.5]
        initfile = open(initfilepath, 'w', encoding='utf8')         # icalendar default

        # initial file creation notice event
        datetimenow = icalendar_datetime_now()
        initeventtext = initfile_eventtext % dict(
            dtstart=icalendar_date_now(),
            created=datetimenow,
            dtstamp=datetimenow,
            uid=icalendar_unique_id(),
            program=PROGRAM.upper(),
            version=VERSION,
            category='+blues' if not forcename else '+greens',
            calname='default' if not forcename else '"%s"' % forcename)

        # [2.0] echo Unicode cheatsheet file as an event too, if first run        
        if not forcename:
            try:
                unicodefilename = os.path.join('docetc', 'unicode-cheat-sheet.txt')
                unicodefiletext = open(unicodefilename, encoding='utf8').read()
                unicodefiletext = icalendar.parser.escape_char(unicodefiletext)
                unicodefiletext = icalendar.parser.foldline(unicodefiletext)
            except:
                pass  # punt on any file/encoding error: just a convenience
            else:
                datetimenow = icalendar_datetime_now()
                initeventtext += '\n' + initunicode_eventtext % dict(
                    dtstart=icalendar_date_now(),
                    created=datetimenow,
                    dtstamp=datetimenow,
                    uid=icalendar_unique_id() + '-unicodefile',   # else same second=id!
                    program=PROGRAM.upper(),
                    version=VERSION,
                    filetext=unicodefiletext)

        # insert event(s) into calendar structure
        initfiletext = initfile_calendartext % dict(
            program=PROGRAM,
            version=VERSION,
            event=initeventtext)
            
        initfile.write(initfiletext)
        initfile.close()


def ask_init_default_ics_file():
    # this is imported and used by the makecalendar.py script
    try:
        basename = input('Name of calendar file to create (without .ics)? ' )
    except EOFError:
        basename = ''
    if basename:
        init_default_ics_file(basename + '.ics')


def icalendar_datetime_now():
    # get formatted current date/time
    now = datetime.datetime.today()           # datetime.datetime(2014, 9, 7, 8, 48, 26, 277682)
    fmt = icalendar.vDatetime(now).to_ical()  # bytes [str(fmt) is no-op, str(now)='2014-09-07' + time]
    return fmt.decode(encoding='utf8')        # str '20140907T084826' ['yyyymmddThhmmss' (TBD: +'Z'?)]  

def icalendar_date_now():
    # get formatted current date
    now = datetime.date.today()               # datetime.date(2014, 9, 7)
    return icalendar.vDate(now).to_ical().decode(encoding='utf8')    # str '20140907'
    
def icalendar_unique_id():
    """
    get globally unique string: prog+date+time+processid
    this is unique only for this second: amend if required (see generate, init)
    there is an alternative uid generator in icalendar.tools which uses random
    """
    datetimestamp = time.strftime('date%y%m%d-time%H%M%S')
    processid = 'pid%s' % str(os.getpid())
    return PROGRAM + '-' + datetimestamp + '-' + processid
