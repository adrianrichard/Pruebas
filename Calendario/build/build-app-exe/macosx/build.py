#!/usr/bin/env python3
"""
=============================================================================
Make a Mac OS X App bundle (folder), using py2app.
Based on the more-complicated build.py of PyEdit.
Main file: run me in this folder to build the app.

An app allows text files to be associated (though irrelevant here)
makes the program immune from Python changes; requires no Python installs;
and better supports file drag-and-drops, program icons, and more (but also
does a woefully-good job of hiding user-config source files and auto-saves!).

Mac app also required... a mac-format .icns icon (the latter became an 
iconify.py extension), and fixfrozenpaths.py's context configurations.

Besides the executable, the app needs:
-frigcal_configs.py: must be source code, and user-visible and editable;
-frigcal_configs_base.py: must be source for its documentation
-icon for the exe/app (window borders/app bar for Windows/Linux);
-UserGuide.html and docetc items it uses at runtime;
-docetc image for the Help dialog
-all included scripts, and in frozen form
 
py2app sets the cwd to the bundle's Contents/Resource folder in all cases:
add '.' to sys.path, and use files copied to .=Resources, to which __file__
will refer.  Associations are irrelevant and unused here.

NOTE: it's assumed that the frozen app, plus the Python and Tk included 
in the app bundle are univeral binaries, supporting both 64- and 32-bit
machines.  This appears to be so, though the app's portability to older 
OS X versions remains to be shown (10.11 El Capitan is build host).
=============================================================================
"""

import os, sys, shutil
join, sep = os.path.join, os.path.sep
force = len(sys.argv) > 1                 # remake icon if any arg
startdir = os.getcwd()                    # this build script's dir

# 'python3' fails in both IDLE and PyEdit RunCode (env's PATH not inherited?)
python = '/usr/local/bin/python3'  # sys.executable (else proxy in PyEdit?)

#----------------------------------------------------------------------------
# make app's icon if one doesn't already exist
#----------------------------------------------------------------------------

iconship = join('..', '..', '..', 'icons')
iconmake = join('..', '..', 'build-icons')
iconname = 'frigcal'
iconfile = iconname + '.icns'

# step into icon build dir and make
if force or not os.path.exists(iconship + sep + iconfile):
    os.chdir(iconmake)
   #os.system('iconutil -c icns %s.iconset' % iconname)                    # Apple util
   #os.system('./resize-on-mac.sh Pyedit1024new images-pyedit')            # just once
    os.system('%s iconify.py -mac images-pyedit %s' % (python, iconname))  # iconify 2.0
    os.chdir(startdir)
    shutil.move(join(iconmake, iconfile), join(iconship, iconfile))     # mv to ship

#----------------------------------------------------------------------------
# first, copy source tree to temp folder to avoid accidental code loss;
# [update - setup and teardown steps are now automated (run this script in 
# its dir), and Info.plist edits are now automatic by setup.py options;]
#----------------------------------------------------------------------------

# automated setup - run in this file's dir
temp = '/Users/blue/Desktop/tempsrc'                   # cp can't include self!
if os.path.exists(temp):
    shutil.rmtree(temp)
os.mkdir(temp)

# move all to temp, add setup.py
shutil.copytree('../../../../frigcal', temp+'/frigcal', symlinks=True) 
shutil.copy('setup.py', temp+'/frigcal')               # add setup script to root
os.chdir(temp+'/frigcal')                              # goto temp build dir
 
#----------------------------------------------------------------------------
# cp so use frigcal name for both the app-bundle folder and auto-menu title;
# this name must also be used in this project's setup.py file here;
# we can't rename these after the build, and the launcher is ingrained;
#----------------------------------------------------------------------------

# shutil.copy('textEditor.py', 'PyEdit.py')
# rename after launcher app built ahead

#----------------------------------------------------------------------------
# build app-bundle folder in ./dist, using ./setup.py, copying N extras
# to the main Resources folder along with the generated program itself;
# this uses --resources to copy non-code extras, and -extras-scripts to
# also freeze releated scripts shipped with frigcal, so that they can
# be run from the app's Content/MacOS folder without a ".py" extension 
# and without requiring a separate Python install.  Source is incuded 
# for its docs only -- won't run as source.
#----------------------------------------------------------------------------

extras = [                         # tbd: use a 'tools' folder?
    'frigcal_configs.py',          # ship these in Content/Resources='.'
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

alsofreeze = [
    'frigcal.py',
    'makenewcalendar.py',          # freeze these into exec in Content/MacOS
    'searchcals.py',               # also ship source in Resources for their docs (only)
    'unicodemod.py',               # freezes require no Py install; source does
    'pickcolor.py',
]

exitstat = os.system(
    '%s setup.py py2app' 
    '   --excludes frigcal_configs,frigcal_configs_base'      # user-facing, in Resources
    '   --iconfile icons/frigcal.icns'
    '   --extra-scripts %s'
    '   --resources %s'
    '   --packages PIL'
    % (python, ','.join(alsofreeze), ','.join(extras + alsofreeze))
)

if exitstat:
    print('ERROR: build failed:', exitstat)
    sys.exit(exitstat)   # don't continue here

#----------------------------------------------------------------------------
# cleanup: move and zip the app folder for easy xfer and backup (it has
# _very_ many files: nearly 3K files+folders for the current PyEdit App);
# [update - teardown actions are now automated (but still no data to copy)]
# don't copy extras to Contents/Resources folder here: automatic via the 
# py2app args above;  fixfrozenpaths.py arranges to see these as needed;
# DON'T -skipcruft in the zip command: py2app makes a Resources/site.pyc!
#----------------------------------------------------------------------------

# zip command: use portable ziptools (vs: 'zip -r %s %s' % (thezip, thedir))
thedir = 'Frigcal.app'
thezip = thedir + '.zip'
code   = '/MY-STUFF/Code/ziptools/link'
zipit  = '%s %s/zip-create.py ../%s %s' % (python, code, thezip, thedir)

# move dist product folder here
os.chdir(startdir)
if os.path.exists('dist'):
    shutil.rmtree('dist')                      # nuke bogus retained temp?
shutil.move(temp+'/frigcal/dist', '.')
shutil.rmtree(temp)                            # rm temp build tree 

# zip the nested app folder - unzip to test and use here or elsewhere
if os.path.exists(thezip):
    shutil.move(thezip, 'prev-'+thezip)        # save previous version
if os.path.exists(thedir):
    shutil.rmtree(thedir)                      # nuke unzipped version

os.chdir('dist')   
shutil.move('frigcal-launcher.app', thedir)

# drop personal calendar items: make new default on start
prunee = 'frigcal.app/Contents/Resources/Calendars'
for item in os.listdir(prunee):
    if item not in ('README.txt', '2.0-examples'):
        itempath = join(prunee, item)
        print('Removing', itempath)
        if os.path.isdir(itempath):
            shutil.rmtree(itempath)
        else:
            os.remove(itempath)       

os.system(zipit)                               # run zip in dist: has app dir
os.chdir('..')   
shutil.rmtree('dist')                          # rm dist: _very_ many files

print('Done: see ./%s' % thezip)

# +unzip app and copy it to /Applications to make it official

