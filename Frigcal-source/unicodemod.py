#!/usr/bin/python
r"""
===============================================================================
unicodemod.py (Python 3.X or 2.X; for 3.X, requires 3.3 or later)
Copyright: August 27, 2016 by M. Lutz (learning-python.com).
License: provided freely, but with no warranties of any kind.

Usage: "[python] unicodemod.py [filepathname encodefrom encodeto]"

Convert a text file from an old Unicode encoding to a new Unicode encoding
(e.g., from 'latin1' or 'utf16', to 'utf8' or 'latin-1'), changing the text
file in-place.  Parameters are input in the console window, unless all are
passed on the command line in the order given above.

For frigcal (this script's original use case), converting existing ".ics"
calendar files to UTF-8 is an alternative to configuring the default Unicode
type in code, and allows the general UTF-8 scheme to be used for newly-saved
files and text that may be outside an original and narrower encoding's scope.
See the first example in "EXAMPLE USAGE" below for frigcal suggested use.
For other use cases, this script provides a general file encoding converter.

-------------------------------------------------------------------------------

DROPPING THE BOM (encoding name guidelines):

Short story: for encodings that may include BOMs at the start of files
(UTF-8, UTF-16, UTF-32), this script strips the BOM on input to avoid
conversion errors, but requires a BOM-generating encoding name to be
used if a BOM is required in the output.  Read on if that is unclear.

The full story: to avoid conversion errors, this script automatically
discards a Unicode BOM (byte order mark) code point at the start of the
decoded input file's data, if one is retained by the 'from' encoding
name specified by the user.  Otherwise, the retained BOM code point:

1) May fail to encode in narrower 'to' encodings (e.g., Latin-1 or ASCII),
   even if the rest of the file's text is encodable in the target format.
   
2) May be silently added as a duplicate BOM for 'to' encodings that add
   BOMs of their own (e.g., "utf-8-sig", "utf-16", and "utf-32").

3) May be added incorrectly to encodings that prohibit a BOM per the
   Unicode standard (e.g., "utf-16-le", "utf-32-be").

Discarding the BOM from input here ensures that none of these cases can
occur.  It also avoids requiring the user to give a 'from' encoding name
that always strips the BOM on input, whether present or not.  "utf-8-sig"
does for UTF-8, but the case for UTF-16 and UTF-32 is more complex.

With this script, any encoding name that handles the input suffices for
the 'from' value, because a BOM is automatically stripped.  For example,
"utf-8" works for UTF-8 files, whether they have a BOM or not.  Note,
however, that this script never itself automatically restores a BOM.
For use cases that require a BOM in the output, use a BOM-generating
encoding name for 'to' that writes the BOM anew, such as "utf-8-sig".

Also note that this script need not account for encoding details or
other byte interpretations, because it strips BOM code points after they
have been decoded, not in their raw and still-encoded form.  For example,
UTF-8's xef\xbb\xbf BOM bytes are just the standard \ufeff BOM Unicode
code point when decoded.  UTF-32's 4-byte encoded BOM format is
similarly irrelevant here.

Concrete encoding-name guidelines:

-For UTF-8 files: "utf-8-sig" discards a BOM if present, "utf-8" does
 not, and neither requires a BOM; either name can be used here for the
 'from' encoding, regardless of file content.  For 'to', use "utf-8"
 to omit a BOM in output, but use "utf-8-sig" to add (or restore) one.

-For UTF-16 files: the generic "utf-16" both requires a BOM to be
 present and discards it, and order-specific names "utf-16-le" and
 "utf-16-be" do neither; any of the three can be used for 'from' here.
 For the 'to' encoding, the generic "utf-16" always adds (or restores)
 a BOM, but the order-specific names do not.

-For UTF-32: the rules are the same as for UTF-16, but replace "16"
 with "32" in the encoding names.

See "docetc/unicodemod-bom-examples.txt" (relative to this file's URL or
folder), as well as the book "Learning Python, 5th Edition" for detailed
examples of BOM processing by encoding names in Python.  For the official
story on the BOM itself, see "http://unicode.org/faq/utf_bom.html#BOM".

-------------------------------------------------------------------------------

CODING NOTES:

Text file APIs used here auto-decode on input and auto-encode on output.
Writes to a temp file initially to avoid changing the original file if any
Unicode error.  Could instead encode to bytes manually and use binary mode
for output.  For 3.X/2.X compatibility, uses 3.3+ u'...' Unicode literals.

CAVEATS/TBDs:

1) As coded, this script loads a file's entire content into memory.  It
   could instead read line-by-line to support pathologically-large files.

2) As coded, this will write end-lines in the running platform's format on
   3.X only, which may be undesirable in some use cases.  Using codecs.open()
   on 3.X too would resolve this (it's available in both 2.X and 3.X, and
   never does end-line mapping).  See "docetc/fixeoln.py" relative to this
   file's folder to convert end-lines in Unicode files generally if needed.

3) Some text editors may support Unicode encoding conversions too, by simple
   opens and saves (but Python code is more fun).

-------------------------------------------------------------------------------

EXAMPLE USAGE (edited for space; on Unix use "cmp -b" instead of "fc /B"):

# utf-8 to latin-1 works if content is in latin-1's code-point range

  c:\...\frigcal> unicodemod.py myicsfile latin-1 utf-8
  c:\...\frigcal> unicodemod.py myicsfile utf-8 latin-1

# utf-8-sig adds or restores a BOM in the final UTF-8 format

  c:\...\frigcal> unicodemod.py somefile utf-8 utf-16
  c:\...\frigcal> unicodemod.py somefile utf-16 utf-8-sig

# dropping and adding a BOM to UTF-8 files

  c:\...\frigcal> unicodemod.py somefile utf-8-sig utf-8
  c:\...\frigcal> unicodemod.py somefile utf-8 utf-8-sig

# dropping and adding a BOM to UTF-16 files (little-endian)

  c:\...\frigcal> unicodemod.py somefile utf-16 utf-16-le
  c:\...\frigcal> unicodemod.py somefile utf-16-le utf-16
  
# interactive mode, non-BOM UTF-8: BOM added to UTF-32, omitted from result

  c:\...\frigcal> fc /B c:\temp\data.txt c:\original\data.txt
  FC: no differences encountered

  c:\...\frigcal> py unicodemod.py
  Path name of file to be converted? c:\temp\data.txt
  Unicode encoding to convert file from? utf8
  Unicode encoding to convert file to? utf32
  Will convert "c:\temp\data.txt" from "utf8" to "utf32" in-place; continue? y
  File successfully converted from utf8 to utf32.
  Press Enter to exit.

  c:\...\frigcal> py unicodemod.py
  (same, but from "utf32" to "utf8")

  c:\...\frigcal> fc /B c:\temp\data.txt c:\original\data.txt
  FC: no differences encountered

# to check the script's work in Python

  c:\...frigcal> py
  >>> open(r'somefilename', 'rb').read()[:500]

SEE ALSO: 'docetc/fixeoln.py' for a Unicode-aware end-line converter.
===============================================================================
"""

from __future__ import print_function
import sys, os

if sys.version[0] == '2':                  # runs on 2.X too
    import codecs
    input = raw_input
    open = codecs.open                     # same, but no end-line mapping

trace = lambda *args: None #print          # trace is for extra prints
BOM_CODEPOINTS = [u'\uFFFE', u'\uFEFF']    # decoded BOMs, strip if in input[0] (py3.3+)


#
# process arguments or inputs
#
if len(sys.argv) == 4:
    interactive = False
    filepath, encodefrom, encodeto = sys.argv[1:4]
else:
    interactive = True
    filepath = encodefrom = encodeto = ''
    try:
        filepath   = input('Path name of file to be converted? ')
        encodefrom = input('Unicode encoding to convert file from? ')
        encodeto   = input('Unicode encoding to convert file to? ')
    except EOFError:
        pass


#
# convert the file
#
if not (filepath and encodefrom and encodeto):
    print('Conversion cancelled; no changes made.')
else:
    verify = 'yes'
    if interactive:
        vermsg = 'Will convert "%s" from "%s" to "%s" in-place; continue? '
        verify = input(vermsg % (filepath, encodefrom, encodeto))
    if not verify or verify.lower() not in ['y', 'yes']:
        print('Conversion cancelled; no changes made.')
    else:
        try:
            # main processing code
            infile  = open(filepath, mode='r', encoding=encodefrom)
            unitext = infile.read()
            infile.close()

            if unitext[0:1] in BOM_CODEPOINTS:
                unitext = unitext[1:]
                trace('Note: Unicode BOM in previous format discarded')

            outfile = open(filepath+'.tmp', mode='w', encoding=encodeto)
            outfile.write(unitext)
            outfile.close()
        except Exception as E:
            print('Error while converting encodings; no changes made.')
            print('Exception encountered:', E)
        else:
            try:
                # move temp to result
                os.remove(filepath)
                os.rename(filepath+'.tmp', filepath)   # permissions?
            except Exception as E:
                print('Error while moving temp file.')
                print('See converted version in "%s".' % (filepath+'.tmp'))
                print('Exception encountered:', E)
            else:
                sucmsg = 'File successfully converted from %s to %s.'
                print(sucmsg % (encodefrom, encodeto))


if interactive and sys.platform.startswith('win'):
    input('Press Enter to exit.')  # icon clicks (args imply shell usage mode)
