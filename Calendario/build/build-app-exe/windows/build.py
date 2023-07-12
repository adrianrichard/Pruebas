#!python3
"""
===========================================================================
Main file: make a Windows single-file executable with PyInstaller,
and manually copy some data items to its folder.

This sets program icons automatically, and avoids Python install and morph.

There is no setup.py file for PyIstaller.
Didn't get cx_freeze or py2exe to work, but stopped short...

Need config files to be source code, and user-visible/editable.
Need icon for both the exe, and window borders in Tk runtime.
PyInstaller sets cwd to anything; uses dir of sys.argv[0],
and copies files to folder holding exe for .=exe's dir.
Need exes for included scripts: there may be no Python install.

Python recoding of an original DOS batch-file version; now based on 
a Linux PyInstaller version (with icon code fron a Mac OS X version): 
Python portability makes this nearly the same everywhere.  Could also
neutralize slash diffs with join() and sep, but other parts vary too.

UPDATE: on Windows, make both 64- and 32-bit executables.  The 32-bit
build machine varies from the 64-bit main machine; specialize paths,
and quote to allow for embedded spaces in Python dirs on 32-bit host.
The 32-bit Windows 8 box PyInstaller required runnning as admin, and
upgrading pip and setuptools to fix a Windows path-quoting bug...

*NOTE*: change "bitsize" in this script from 64 to 32 as needed.
===========================================================================
"""

import os, sys, shutil
join, sep = os.path.join, os.path.sep

force = len(sys.argv) > 1                 # remake icon if any arg
startdir = os.getcwd()                    # this build script's dir
python = sys.executable                   # may have embedded spaces!

bitsize = 64  # or 32
mainhost = (bitsize == 64)

def FWP(path):
    # allow long paths on Windows: pyedit auto-save files
    # see mergeall and ziptools for tons of details
    return '\\\\?\\' + os.path.abspath(path)

#----------------------------------------------------------------------------
# make exe's icon if one doesn't already exist
#----------------------------------------------------------------------------

print('ICONS')
iconship  = join('..', '..', '..', 'icons')
iconmake  = join('..', '..', 'build-icons')
iconnames = ['frigcal']

# step into icon build dir and make
for iconname in iconnames:
    iconfile  = iconname + '.ico'
    if force or not os.path.exists(iconship + sep + iconfile):
        os.chdir(iconmake)
        # requires a py with Pillow installed, pre sized/arranged images
        # os.system('%s iconify.py -win images-%s %s' % (python, iconname, iconname))
        os.system('py -3.3 iconify.py -win images-%s %s' % (iconname, iconname))
        os.chdir(startdir)
        shutil.move(join(iconmake, iconfile), join(iconship, iconfile))

#----------------------------------------------------------------------------
# first: copy source tree to temp folder to avoid accidental code loss;
# setup and teardown steps are now automated (run this script in its dir);
#----------------------------------------------------------------------------

# automated setup - run in this file's dir
print('TEMP COPY')
temp = r'C:\Users\mark\Desktop\tempsrc'                # cp can't include self!
if os.path.exists(temp):                               # same dir on 64/32 m/c
    shutil.rmtree(FWP(temp))
os.mkdir(temp)

# move all to temp
shutil.copytree(FWP(r'..\..\..\..\frigcal'), FWP(temp+r'\frigcal'), symlinks=True) 
#shutil.copy('setup.py', temp+r'\TextEditor')          # not for pyinstaller
os.chdir(temp+r'\frigcal')                             # goto temp build dir

#--------------------------------------------------------------------------
# build one-file main exe in .\dist, plus extras for standalone scripts
# can't assume a local Python install to run the included scripts;
#
# UPDATE: PyInstaller's "multipackage" feature (1 bundle, N scripts)
# is currently broken, so make (large) standalone exes for all; blah.
# This seems a deal-breaker, but py2exe is languishing too, and...
#--------------------------------------------------------------------------

# pyinstaller may not be on PATH
if bitsize == 64:
    pyscripts = r'C:\Users\mark\AppData\Local\Programs\Python\Python35\Scripts'
else:
    pyscripts = r'c:\Program Files\Python 3.5\Scripts'

guifreeze = [
    'frigcal-launcher.pyw',
    'frigcal.py',
    'pickcolor.py'
]
    
scriptfreeze = [
    'makenewcalendar.py',          # freeze these into exes in main folder 
    'searchcals.py',               # also ship source for their docs (only)
    'unicodemod.py',               # freezes require no Py install; source does
]

# allow for embedded quotes (not just '%s\\pyinstaller' or '"%s\\pyinstaller"')
for target in guifreeze:
    print('\nBUILDING:', target)
    exitstat = os.system(
        'cmd /C ""%s\\pyinstaller"'
        '   --onefile'
        '   --windowed'
        '   --icon icons\\frigcal.ico'
        '   --exclude-module frigcal_configs'
        '   --exclude-module frigcal_configs_base'
        '   --hidden-import PIL'    # added Sep-2017 (and installed for py3.5)
        '   %s"' % (pyscripts, target))  

    if exitstat:
        print('ERROR: build failed:', exitstat)
        sys.exit(exitstat)   # don't continue here

for target in scriptfreeze:
    print('\nBUILDING:', target)
    exitstat = os.system(
        'cmd /S /C ""%s\\pyinstaller"'
        '   --onefile'
        '   --console'
        '   --icon icons\\frigcal.ico'
        '   --exclude-module frigcal_configs'
        '   --exclude-module frigcal_configs_base'
        '   %s"' % (pyscripts, target))

    if exitstat:
        print('ERROR: build failed:', exitstat)
        sys.exit(exitstat)   # don't continue here

#--------------------------------------------------------------------------
# use exe (not script) name
#--------------------------------------------------------------------------

# shutil.move(r'dist\textEditor.exe', r'dist\PyEdit.exe')

#--------------------------------------------------------------------------
# copy extras to exe's folder: source code arranges to see these;
# not --add-data: it gets unzipped in a Temp dir the user won't see...
#--------------------------------------------------------------------------

extras = [                         # tbd: use a 'tools' folder?
    'frigcal_configs.py',          # ship these in install folder='.'
    'frigcal_configs_base.py',
    'README.txt', 
    'icons',
    'docetc',
    'UserGuide.html',
    'Calendars',
    'MonthImages',
    'icalendar',
    'pytz'
]

extras = extras + scriptfreeze

for name in extras:
    if os.path.isfile(name):
         shutil.copy(name, 'dist')
    else:
         shutil.copytree(name, join('dist', name))

#----------------------------------------------------------------------------
# cleanup: move and zip the exe folder for easy xfer (just a few files here);
# [update - teardown actions are now automated (but still no data to copy)]
#----------------------------------------------------------------------------

# zip command: use portable ziptools
thedir = 'Frigcal' + ('-64bit' if bitsize == 64 else '-32bit')
thezip = thedir + '.zip'
if bitsize == 64:
    code = r'C:\MY-STUFF\Code\mergeall\test\ziptools'
else:
    code = r'D:\MY-STUFF\Code\mergeall\test\ziptools'

# allow spaces
zipit = r'"%s" %s\zip-create.py %s %s -skipcruft' % (python, code, thezip, thedir)

# move dist product folder here
os.chdir(startdir)
if os.path.exists('dist'):
    shutil.rmtree('dist')                          # nuke bogus retained temp?
shutil.move(FWP(temp+r'\frigcal\dist'), '.')
shutil.rmtree(temp)                                # rm temp build tree 

# zip the exe=dist folder - unzip to test and use here or elsewhere
if os.path.exists(thezip):
    shutil.move(thezip, 'prev-'+thezip)            # save previous version?
if os.path.exists(thedir):
    shutil.rmtree(FWP(thedir))                     # nuke unzipped version

os.rename('dist', thedir)                          # rename for unzip name

# drop personal calendar items: make new default on start
prunee = thedir + r'\Calendars'
for item in os.listdir(prunee):
    if item not in ('README.txt', '2.0-examples'):
        itempath = join(prunee, item)
        print('Removing', itempath)
        if os.path.isdir(itempath):
            shutil.rmtree(itempath)
        else:
            os.remove(itempath)       

os.system(zipit) 
shutil.rmtree(FWP(thedir))                         # no need to save raw dist

print('Done: see .\%s' % thezip)
if sys.stdin.isatty():
   input('Press enter to close')                   # stay up if clicked (Win)

# +unzip exe folder, and move to C:\Programs (?) to make it permanent
