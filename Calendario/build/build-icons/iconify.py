#!/usr/bin/python
"""
================================================================================
iconify.py 2.0 - bundle presized images as Windows or Mac OS icon files,
on any platform that runs Python: Windows, Mac, Linux, and more.

  iconify.py -win imagesdir iconname   # make iconname.ico  from imagesdir/*
  iconify.py -mac imagesdir iconname   # make iconname.icns from imagesdir/*
  iconify.py                           # input all parameters interactively

Author and copyright: © M. Lutz 2014-2017 (learning-python.com)
License: provided freely, but with no warranties of any kind.
Version 2.0, May, 2017: create Mac OS .icns files too, refactor to functions.
Version 1.0, Oct, 2014: initial release, Windows .ico files only, script.

Runs on Python 2.X or 3.X, requires Pillow (PIL) image library:
  -fetch and install Python from https://www.python.org/downloads/
  -fetch and install Pillow from https://pypi.python.org/pypi/Pillow

This command-line script creates a ".ico" Windows or ".icns" Mac OS (X) icon
file from all the image files in a folder, per the policies described in the
generator functions ahead.  It works on any Python platform -- you can use it
to make Windows or Mac icons on Windows, and Mac or Windows icons on Mac.

----
USAGE:
  [py[thon]] iconify.py [icontype imagedir iconname]

where:
  icontype is either "-win" to make a Windows .ico file,
  or "-mac" to make a Mac .icns file

  imagedir is the name of the directory holding your images
  
  iconname is the icon file to create, without its .ico or .icns

Both imagedir and iconname are either a simple name (relative
to and located in this folder, ".") or a full directory path.

All three parameters are requested and input at the console
if omitted in the command line (e.g., on Windows clicks).

EXAMPLES:
  On Windows, make a Mac myapp.icns from images in .\images:
      C:\...> iconify.py -mac images myapp

  On Windows, make a Windows myprog.ico from images in C:\icons\source:
      C:\...> py -3 iconify.py -win C:\icons\source myprog

  On Mac or Linux, make a Windows myprog.ico from images in ./images
      ~/...$ python iconify.py -win images myprog

  On Mac or Linux, make a Mac myapp.icns from images in ~/icons/source
      ~/...$ python3 iconify.py -mac ~/icons/source myapp

  On any platform, enter parameters interactively:
      python iconify.py  (or click this file on Windows)

----
PRESIZING IMAGES:
    Before running iconify, first copy your (ideally large) original image to
    the image folder and resize to lower dimensions for icon use as desired.
    This can be done manually (e.g., via Paint on Windows or Preview on Mac),
    or automatically with command-line tools (e.g., "sip" on Mac) or Python
    scripts using image-processing libraries (e.g., Pillow).

    For example, on Mac the included resize-on-mac.sh script uses "sips" to 
    automatically resize a 1024x1024 original to an images folder, with one
    image for each common dimension (16, 32, 64, 128, 256, 512, and 1024).
    This folder can then be used as input to iconify to make an icon:

       ./resize-on-mac.sh pyedit images-pyedit         # resize 1024 to folder
       python3 iconify.py -mac images-pyedit pyedit    # make pyedit.ico
       python3 iconify.py -win images-pyedit pyedit    # make pyedit.icns

    On Windows, it generally suffices to include a handful of resized images
    (e.g., 512 and 256), but the full set may help. Linux icons are TBD; at
    a minimum, a GIF, made manually or automatically, works for app-bar icons.

----
ICON FORMATS:
  This code makes little sense without its target binary data formats:

  For Windows icon file format, try:
    http://en.wikipedia.org/wiki/ICO_(file_format),
    http://msdn.microsoft.com/en-us/library/ms997538.aspx, or a search.

  For Mac icon file format, see:
    https://en.wikipedia.org/wiki/Apple_Icon_Image_format
    https://developer.apple.com/library/content/documentation/
         GraphicsAnimation/Conceptual/HighResolutionOSX/
         Optimizing/Optimizing.html#//apple_ref/doc/uid/TP40012302-CH7-SW1

----
TBD: could also PIL.Image.resize((32, 32)) if needed to shrink.
TBD: could rely on PIL for some manual actions here (e.g., loads).
TBD: could use PIL (PILLOW) to code a portable image resizer script too.
================================================================================
"""

import sys, os, struct, mimetypes
try:
    import PIL.Image
except:
    print('Sorry, you must install Pillow to use this script.')
    print('See https://pypi.python.org/pypi/Pillow or pip.')
    sys.exit(1)
    
if sys.version[0] == '2':
    input = raw_input   # 2.X compatibility

Exts = {'-mac': '.icns', '-win': '.ico'}   # what we build

def exitPrompt():
    # stay up till Enter pressed if clicked to run on Windows
    if sys.platform.startswith('win') and sys.stdin.isatty():
        input('Press Enter/Return to Exit.')

def shutdown(message, statuscode=1):
    print(message)
    exitPrompt()
    sys.exit(statuscode)   # 0=good


#-------------------------------------------------------------------------------
# Get run parameters
#-------------------------------------------------------------------------------

def getParameters():
    """
    Get parameters from command line if all present, else console user.
    Returns icontype ('-mac' or '-win'), imagedir, and iconname (sans ext).
    """
    if len(sys.argv) == 4:
        icontype, imagedir, iconname = sys.argv[1:]       # all args xor inputs
    else:
        icontype = input('icontype (-mac or -win)?  ')
        imagedir = input('imagedir (images source)? ')
        iconname = input('iconname (no extension)?  ')    # without '.ico'/'.icns'

    # error checking
    if icontype not in Exts:
        shutdown('Invalid icontype value.')
    if not os.path.isdir(imagedir):
        shutdown('Invalid imagedir folder.')
    if not os.path.exists(os.path.abspath(os.path.dirname(iconname))):
        shutdown('Invalid iconname folder.')

    return (icontype, imagedir, iconname)


#-------------------------------------------------------------------------------
# Load image files 
#-------------------------------------------------------------------------------

def loadImages(imagedir, icontype, usePng=True, useJpg=False, useBmp=False):
    """
    Just PNG for now; BMP for Windows and JPG for Mac are TBD.
    imagedir is a folder pathname, icontyep is '-mac' or '-win'.
    Returns two lists: loaded files and their (path) names.
    [2.0] Recoded to use mimetypes, not glob and case mapping;
    was: imagenames += glob.glob(os.path.join(imagedir, '*.png')).
    """
    
    imagenames = []
    for filename in os.listdir(imagedir):
        path = os.path.join(imagedir, filename)
        mime = mimetypes.guess_type(filename)[0]   # (type, encoding)
        
        if mime == 'image/png' and usePng:   # any case, where it matters
            imagenames.append(path)

        elif mime == 'image/jpeg' and icontype == '-mac' and useJpg:
            imagenames.append(path)

        elif mime == 'image/x-ms-bmp' and icontype == '-win' and useBmp:
            imagenames.append(path)

    if len(imagenames) == 0:
        shutdown('No image files found: check your imagesdir folder.')

    imagedatas = []
    for imagename in imagenames:
        imagefile = open(imagename, 'rb')
        imagedata = imagefile.read()
        imagefile.close()
        imagedatas.append(imagedata)

    return (imagedatas, imagenames)


#-------------------------------------------------------------------------------
# Windows icon generator [1.0]
#-------------------------------------------------------------------------------

def writeWindowsIcon(iconfile, imagedatas, imagenames, verbose=True):
    """
    Write icon to already-opened iconfile for already-loaded imagedatas.
    All integer items in file are written little-endian, MSB last ('<').

    For Windows, packs any-sized images into file after a directory,
    and Windows will choose and possibly scale an appropriate match.
    This is substantially simpler than Mac .icns format (see ahead).

    [2.0] Recoded to order images by most-to-least pixels.  This may
    or may not matters in modern Windows.  Window title-bar icons may
    be blurrier in the opposite order, and the new order shouldn't hurt.
    
    Hint: large images may be best - scaling down is better than up.
    Caveat: this script supports PNG images, but for simplicity not BMP.
    """
    
    # 1) HEADER: 3 2-byte ints

    hdrsize = 6
    hdrfmt  = "<hhh"
    iconfile.write(struct.pack(hdrfmt,
                    0,                       # reserved, always 0
                    1,                       # 1=.ico icon, 2=.cur cursor 
                    len(imagedatas)          # number images in file
                    ))

    # 2) DIRECTORY: 1..N 16-byte records, bytes/shorts/ints, for width/height/size/offset/etc.

    dirsize = 16
    dirfmt  = "<BBBBhhii"
    imgoffset = hdrsize + (dirsize * len(imagedatas))

    # bit per pixel: this table seems a hack, but no direct map in PIL itself?
    # example: common PNG => 'RGBA' => 32bpp (8 bits (byte) * 4 bands (RGBA))
    mode_to_bpp = {'1': 1, 'L': 8, 'P': 8,
                   'RGB': 24, 'RGBA': 32, 'CMYK': 32, 'YCbCr': 24, 'I': 32, 'F': 32}

    # analyze with PIL, add rank and image info
    withRankAndPIL = []
    for (imagedata, imagename) in zip(imagedatas, imagenames):
        pilimg = PIL.Image.open(imagename)
        size = pilimg.size
        width, height = size       # a 2-tuple
        rank = width * height
        bitsperpixel = mode_to_bpp[pilimg.mode]
        withRankAndPIL.append((rank, imagedata, imagename, size, bitsperpixel))

    # order most-to-least pixels (descending)
    withRankAndPIL.sort(key=(lambda x: x[0]), reverse=True)

    # write directory entries
    for (rank, imagedata, imagename, size, bitsperpixel) in withRankAndPIL:
        width, height = size                 # a 2-tuple
        if width  >= 256: width  = 0         # 0 means 256 (or more), per spec (and practice)
        if height >= 256: height = 0
        if verbose:
            print('Adding:', imagename, '[%dx%d] %s' % (width, height, size))
            
        iconfile.write(struct.pack(dirfmt,
                    width,                   # width, in pixels,  0..255
                    height,                  # height, in pixels, 0..255
                    0,                       # ?color count/palette (0 if >= 8bpp)
                    0,                       # reserved, always 0
                    1,                       # ?color planes: 0 or 1 treated same (>1 matters)
                    bitsperpixel,            # ?bits per pixel (0 apparently means inferred)
                    len(imagedata),          # size of image data in bytes
                    imgoffset                # offset to image data from start of file            
                    ))
        imgoffset += len(imagedata)

    # 3) IMAGE BYTES: packed into rest of icon file sequentially

    # in same order as directory entries
    for imagedata in (info[1] for info in withRankAndPIL):
        iconfile.write(imagedata)


#-------------------------------------------------------------------------------
# Mac OS (X) icon generator [2.0]
#-------------------------------------------------------------------------------

def writeMacIcon(iconfile, imagedatas, imagenames, verbose=True):
    """
    Write icon to already-opened iconfile for already-loaded imagedatas.
    All integer items in file are written big-endian, or MSB first ('>').

    For Mac, uses only images of allowed fixed sizes, and codes them in the
    icon for both standard and high resolution, the latter of which has 4
    times the pixel density in the same screen-area size.

    For example, a 512x512 pixel image is coded by this script as _both_
    a 512x512 standard-resolution icon and a 256x256 high-resolution icon:
    both "512x512" and "256x256@2x" in Apple-speak.  A 1024x1024 is just
    512x512@2x (there is no standard-resolution 1024x1024).
    
    Hint: on Macs, "iconutil -c icns folder.iconset" is an alternative
    if this script does not suffice, and "sips -z H W img.png --out new.png"
    resizes images (but Mac uses a "best" if you don't provide all sizes).
    See notes at the top of this file for more on resizing images for iconify.

    Hint: large images may be best - scaling down is better than up.
    Caveat: this script supports PNG images, but for simplicity not JPEG.
    """
    
    # must all be square (width=height) and of standard pixel sizes
    sizetotypes = {
        16:   [b'icp4'],            # 16x16   std only  (no 8x8@2x) 
        32:   [b'icp5', b'ic11'],   # 32x32   std -AND- 16x16@2x   high
        64:   [b'icp6', b'ic12'],   # 64x64   std -AND- 32x32@2x   high
        128:  [b'ic07'],            # 128x128 std only  (no 64x64@2x) 
        256:  [b'ic08', b'ic13'],   # 256x256 std -AND- 128x128@2x high
        512:  [b'ic09', b'ic14'],   # 512x512 std -AND- 256x256@2x high
        1024: [b'ic10']             # 1024x1024 (10.7) = 512x512@2x high (10.8) 
    }
    
    # 0) ANALYZE: filter out bad-sized images, add type codings

    withtypes = []
    for (imagedata, imagename) in zip(imagedatas, imagenames):
        pilimg = PIL.Image.open(imagename)
        width, height = pilimg.size   # a 2-tuple
        if width != height or width not in sizetotypes:
            print('Invalid image size, discarded: %d x %d.' % (width, height))
        else:
            icontypes = sizetotypes[width]
            for icontype in icontypes:
                withtypes.append([icontype, imagedata])   # both std + high?
            if verbose:
                message = 'Adding: %s [%dx%d] as types %s'
                print(message % (imagename, width, height, icontypes))

    imagedatas = withtypes
    imagedatas.sort(key=lambda x: x[0])   # order by ascending type codes
         
    # 1) HEADER: 4-byte "magic" + 4-byte filesize (including header itself)

    iconfile.write(b'icns')
    filelen = (8 +
        sum((8 + len(imagedata)) for [icontype, imagedata] in imagedatas))
    iconfile.write(struct.pack('>I', filelen))

    # 2) IMAGE TYPE+LENGTH+BYTES: packed into rest of icon file sequentially

    for [icontype, imagedata] in imagedatas:
        # data length includes type and length fields (4+4)
        iconfile.write(icontype)                                # 4 byte type
        iconfile.write(struct.pack('>I', 8 + len(imagedata)))   # 4-byte length
        iconfile.write(imagedata)                               # and the image


#-------------------------------------------------------------------------------
# Main: package images in an icon file
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    (icontype, imagedir, iconname) = getParameters()
    (imagedatas, imagenames) = loadImages(imagedir, icontype)
    
    iconfile = open(iconname + Exts[icontype], 'wb')

    if icontype == '-mac':
        writeMacIcon(iconfile, imagedatas, imagenames)
    else:
        writeWindowsIcon(iconfile, imagedatas, imagenames)

    iconfile.close()
    print('Finished: see %s.' % os.path.abspath(iconname + Exts[icontype]))
    exitPrompt()  # Windows clicks

