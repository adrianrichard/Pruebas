#!/bin/sh 
#
# Run on Mac: automatic image resizing (pre-iconify).
#
# Pass arg #1 = the name (sans extension) of a 1024x1024 PNG image. 
# The resizes will appear in folder whose name is in argument #2:
#
#     ./resize-on-mac.sh pyedit images-pyedit   
#
# After running this, run iconify against the resized images dir:
#
#      python3 iconify.py -mac images-pyedit pyedit
#      python3 iconify.py -win images-pyedit pyedit
#
rm -rf $2
mkdir $2
sips -z 16 16     $1.png --out $2/$1_16x16.png
sips -z 32 32     $1.png --out $2/$1_32x32.png
sips -z 64 64     $1.png --out $2/$1_64x64.png
sips -z 128 128   $1.png --out $2/$1_128x128.png
sips -z 256 256   $1.png --out $2/$1_256x256.png
sips -z 512 512   $1.png --out $2/$1_512x512.png
cp                $1.png       $2/$1_1024x1024.png

# to build:
# python3 iconify.py -mac $2 $1 
# python3 iconify.py -win $2 $1 
