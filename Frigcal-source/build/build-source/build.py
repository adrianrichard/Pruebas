#!/usr/bin/env python3
"""
=============================================================================
Make a frigcal source-code package (a zipfile scrubbed of private content).
This is just a few moves and a zip; there are no frozen builds here.
Unlike the app/exe scripts, this may be run on Windows, Mac, or Linux.

*NOTE*: remove any unzipped app/exe folders in build/ before running this.

[may22] Updated for new macOS build machine: republish source-code package
with an import patch in pytz/lazy.py for a Python 3.10 change and breakage.
=============================================================================
"""

import os, sys, shutil
join, sep = os.path.join, os.path.sep
startdir = os.getcwd()                    # this build script's dir

# 'python3' fails in both IDLE and PyEdit RunCode (env's PATH not inherited?)
python = sys.executable

#----------------------------------------------------------------------------
# make app's icon if one doesn't already exist
#----------------------------------------------------------------------------

pass  # handle this manually in build-app-exe, as icons differ per platform

#----------------------------------------------------------------------------
# copy frigcal to avoid accidents and recursive-copy loop
#----------------------------------------------------------------------------

# automated setup - run in this file's dir

if sys.platform.startswith('darwin'):
    temp = '/Users/me/Desktop/tempsrc'             # cp can't include self! [may22]
elif sys.platform.startswith('win'):
    temp = r'C:\Users\mark\Desktop\tempsrc'        # or use $HOME, etc.
elif sys.platform.startswith('linux'):
    temp = '/home/name/Desktop/tempsrc'

if os.path.exists(temp):
    shutil.rmtree(temp)
os.mkdir(temp)

# copy all to temp
print('Building tree')
shutil.copytree(join('..', '..', '..', 'frigcal'),
                join(temp, 'frigcal'), symlinks=True)     # with metadata, nofollow links

#----------------------------------------------------------------------------
# make the source zipfile
#----------------------------------------------------------------------------

# zip command: use portable ziptools (vs: 'zip -r %s %s' % (thezip, thedir))
thedir = 'Frigcal-source'
thezip = thedir + '.zip'

if sys.platform.startswith('darwin'):
    code = '~/MY-STUFF/Code/ziptools/link'    # [may22] / now verboten
elif sys.platform.startswith('win'):
    code = r'C:\Users\lutz\Downloads\Mergeall-source\test\ziptools'
elif sys.platform.startswith('linux'):
    code = '/media/name/Desktop/MY-STUFF/Code/mergeall/test/ziptools'

zipit = '%s %s/zip-create.py %s %s -skipcruft' % (python, code, thezip, thedir)
zipit = zipit.replace('/', os.sep)

# rename and move source product folder here
shutil.move(join(temp, 'frigcal'), join(temp, thedir))
if os.path.exists(thedir):
    shutil.rmtree(thedir)                      # nuke bogus retained temp?
shutil.move(join(temp, thedir), '.')
shutil.rmtree(temp)                            # rm temp build tree 

# remove zipped app, exes, src in the build tree for space
for (root, subs, files) in os.walk(join(thedir, 'build')):
    for file in files:
        if file.startswith(('Frigcal', 'prev-Frigcal')) and file.endswith('.zip'):
            filepath = join(root, file)
            print('Removing', filepath)
            os.remove(filepath)
            dummy = open(filepath + '.stripped', 'w')
            dummy.write('**REMOVED**')
            dummy.close()

# drop personal calendar items: make new default on start
prunee = join(thedir, 'Calendars')
for item in os.listdir(prunee):
    if item not in ('README.txt', '2.0-examples'):
        itempath = join(prunee, item)
        print('Removing', itempath)
        if os.path.isdir(itempath):
            shutil.rmtree(itempath)
        else:
            os.remove(itempath)

# drop other non-public stuff (or: all _*/ ?)
print('Removing _private, __pycache__, _old-screenshots, _private_')
shutil.rmtree(join(thedir, '_private'))
shutil.rmtree(join(thedir, '__pycache__'))
shutil.rmtree(join(thedir, '_old-screenshots'))
shutil.rmtree(join(thedir, '_private_'))           # [may22] shrinkpix-era dup

# zip the reorganized source folder
if os.path.exists(thezip):
    shutil.move(thezip, 'prev-'+thezip)        # save previous version
os.system(zipit)                               # run zip in build-source
shutil.rmtree(thedir)                          # rm temp folder copy 

print('Done: see', thezip)

# +unzip and copy elsewhere for easy access
