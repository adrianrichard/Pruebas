#!/usr/bin/python3
"""
==========================================================================
chunkio.py: Read and write large files in chunks, instead of all at once.
NOT USED by frigcal: supplemental example only.

It's been reported that Windows error 22 -- "Invalid argument' can be
raised when writing buffers to files > 64M on networked drives with
older MSVC libraries.  This doesn't seem an issue in frigcal: Python 3
is required and uses later MSVC libs, and calendar files are relatively
small (the developer's largest is 876K and this spans 12 years' events;
64M wouldn't be reached until some 897 comparable years of events, and
it's somewhat unlikely that anyone would be using frigcal that long...).
Still, this module's functions could be used to avoid the potential
altogether if ever needed, with a slight speed hit on loads and saves.

Note: chunk size means bytes for binary files, but characters (chars)
for text.  Due to end-of-line translations on Windows and Unicode
encoding/decoding everywhere, a char may map to and from one or more
bytes.  Hence, buffer size cannot map to absolute bytes for text files.
Given that we're interested only in avoiding excessively large buffer
transfers here, the inexactness for text should be acceptable.  Python
may manage text transfer buffers in additional ways beyond both program
control and this module's scope (text is not bytes in a Unicode world).
==========================================================================
"""

import os, sys

chunk = 1025 * 500   # 500k bytes or chars: default chunk size and threshold

trace = lambda *args: print('.', end = '', flush=True)   # : None to disable


def read(filepath, fileobj, chunk=chunk, verify=True):
    """
    ---------------------------------------------
    read and return all from fileobj;
    caller closes file and handles exceptions;
    ---------------------------------------------
    """
    size = os.path.getsize(filepath)              # number bytes, not chars
    if size <= chunk:
        return fileobj.read()                     # read all at one
    else:
        buffer = b'' if 'b' in fileobj.mode else ''
        while True:
            trace('read chunk')
            fetch = fileobj.read(chunk)           # upto 'chunk' bytes or chars
            if not fetch:                         # empty means eof
                break
            else:
                buffer += fetch

        if verify and 'b' in fileobj.mode:
            # not for text: \r\n -> \n, and Unicode decoding
            assert len(buffer) == size

        return buffer


def write(fileobj, content, chunk=chunk, verify=True):
    """
    ---------------------------------------------
    write all of content to fileobj;
    caller closes file and handles exceptions;
    ---------------------------------------------
    """
    size = len(content)                           # number bytes or chars
    if size <= chunk:
        written = fileobj.write(content)          # write all at once
    else:
        written = 0
        while True:
            trace('write chunk')
            store = content[:chunk]               # upto 'chunk' bytes or chars
            if not store:                         # empty means end of string
                break
            else:
                written += fileobj.write(store)   # same as len(store)
                content = content[chunk:]
                
        if verify:
            assert written == size                # number bytes or chars

    return written
        
                    
if __name__ == '__main__':
    """
    ---------------------------------------------
    self-test: change to use your local files
    ---------------------------------------------
    """
    tempfile = 'tempcopy'
    diffcmd  = 'fc' if sys.platform.startswith('win') else 'diff'

    # [1.6] updated paths for new test file locations
    binfiles  = [sys.executable,                     # e.g., r'C:\Python33\python.exe'
                 os.path.join('..', 'MonthImages',
                     'AlternateMonthImages', 'Original-jpegs', '01_DSC03208.JPG')]
    
    textfiles = ['__chunkio__.py',
                 '..' + os.sep + 'Calendars' + os.sep + 'frigcal-default-calendar.ics',
                 '..' + os.sep + 'UserGuide.html']
                #r'..\Calendars\working--Full-Calendar-From-Outlook-July1112.ics']

    # test default and small
    for achunk in (chunk, 1024*10):
        print ('*' * 79, '\n[%d]\n' % achunk)
        
        # binary mode files
        print('[binary]')
        for test in binfiles + textfiles:
            inf  = open(test, 'rb')
            outf = open(tempfile, 'wb')
            got  = read(test, inf, achunk)
            write(outf, got, achunk)
            inf.close(); outf.close()
            print(os.popen('%s %s %s' % (diffcmd, tempfile, test)).read(), end='')

        print('='* 79, '\n')
        
        # text mode files
        print('[text]')
        for test in textfiles:
            inf  = open(test, 'r', encoding='utf8')
            outf = open(tempfile, 'w', encoding='utf8')
            got  = read(test, inf, achunk)
            write(outf, got, achunk)
            inf.close(); outf.close()
            print(os.popen('%s %s %s' % (diffcmd, tempfile, test)).read(), end='')

    os.remove(tempfile)
    if sys.platform.startswith('win'): input('Press Enter to close')




"""
Expected self-test output *pattern* (your files, python, and paths may vary):

*******************************************************************************
[512500]

[binary]
Comparing files tempcopy and C:\PYTHON33\PYTHON.EXE
FC: no differences encountered

Comparing files tempcopy and MONTHIMAGES\01_DSC03208.JPG
FC: no differences encountered

Comparing files tempcopy and __CHUNKIO__.PY
FC: no differences encountered

Comparing files tempcopy and CALENDARS\FRIGCAL-DEFAULT-CALENDAR.ICS
FC: no differences encountered

Comparing files tempcopy and USERGUIDE.HTML
FC: no differences encountered

===============================================================================

[text]
Comparing files tempcopy and __CHUNKIO__.PY
FC: no differences encountered

Comparing files tempcopy and CALENDARS\FRIGCAL-DEFAULT-CALENDAR.ICS
FC: no differences encountered

Comparing files tempcopy and USERGUIDE.HTML
FC: no differences encountered

*******************************************************************************
[10240]

[binary]
..........Comparing files tempcopy and C:\PYTHON33\PYTHON.EXE
FC: no differences encountered

........................Comparing files tempcopy and MONTHIMAGES\01_DSC03208.JPG
FC: no differences encountered

Comparing files tempcopy and __CHUNKIO__.PY
FC: no differences encountered

....................Comparing files tempcopy and CALENDARS\FRIGCAL-DEFAULT-CALENDAR.ICS
FC: no differences encountered

..........................Comparing files tempcopy and USERGUIDE.HTML
FC: no differences encountered

===============================================================================

[text]
Comparing files tempcopy and __CHUNKIO__.PY
FC: no differences encountered

....................Comparing files tempcopy and CALENDARS\FRIGCAL-DEFAULT-CALENDAR.ICS
FC: no differences encountered

..........................Comparing files tempcopy and USERGUIDE.HTML
FC: no differences encountered

Press Enter to close
"""
