#!/usr/bin/python3
"""
simple source-code line count script, used for dev metrics only
"""
import os, glob, sys

srcenc = 'utf8'                                       # [1.7] configs file now utf-8
extras =  [os.path.join('docetc', 'fixeoln.py')]      # [1.7] new but rarely required
extras += [os.path.join('docetc', 'fixeoln-all.py')]  # [2.0] added tree-wide fixer
extras += [os.path.join('docetc', fname+'.py')        # related examples
              for fname in ('__chunkio__', '__hide-unhide__', '__withdraw__')]

# app/exe build scripts count too (but skip iconify.py)
extras += glob.glob('build/build-app-exe/*/build.py'.replace('/', os.sep),)
extras += glob.glob('build/build-source/build.py'.replace('/', os.sep),)

tally = count = 0
for fname in glob.glob('*.py*') + extras:             # files in this dir (mostly)
    if not fname.startswith('__'):                    # skip self and extras in '.'
        fobj = open(fname, encoding=srcenc)
        lcnt = len(fobj.readlines())
        tally += lcnt
        count += 1
        print(fname, '=>', lcnt)
        
print('Total sloc in %d files: %s' % (count, tally))
if sys.platform.startswith('win'):
    input('Press Enter')  # if clicked on Windows


"""
================================================================================
example output (current counts/manifest):

attributeproxy.py => 138
fixfrozenpaths.py => 125
frigcal-launcher.pyw => 245
frigcal.py => 2234
frigcal_configs.py => 82
frigcal_configs_base.py => 659
guimaker_pp4e.py => 110
icsfiletools.py => 736
makenewcalendar.py => 22
pickcolor.py => 83
scrolledlist.py => 140
searchcals.py => 206
sharednames.py => 76
unicodemod.py => 233
docetc/fixeoln.py => 210
docetc/fixeoln-all.py => 252
docetc/__chunkio__.py => 206
docetc/__hide-unhide__.py => 41
docetc/__withdraw__.py => 32
build/build-app-exe/linux/build.py => 195
build/build-app-exe/macosx/build.py => 181
build/build-app-exe/windows/build.py => 224
build/build-source/build.py => 108
Total sloc in 23 files: 6538
================================================================================
"""
