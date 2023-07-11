#!/bin/sh 
#
# Run on Mac: automatic image resize + icon build.
#

./resize-on-mac.sh Frigcal1024 images-frigcal

python3 iconify.py -mac images-frigcal frigcal
python3 iconify.py -win images-frigcal frigcal

