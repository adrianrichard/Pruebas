#================================================================================
# Build+publish the full Frigcal source-code package.  Run anywhere with:
#
#     bash _publish.sh
#
# This publishes just the source-code package.  App and executable packages
# have their own build/ scripts which must be run on specific platforms; are
# each built as an atomic zip which can be uploaded in a single step; and are 
# rarely updated due to flux in build tools, platforms, and Python itself.
#
# Notes:
# - Largely adapted from Mergeall's earlier _publish.sh (de-rundancy me?).
# - This works only on Frigcal's host; paths and structure are host specific.
# - docetc/docimgs/ also has a _publish.sh to upload just its image galleries.
# - This used to all be done manually; automation makes changes much easier. 
#================================================================================

# Get common defs - host specific
source ~/MY-STUFF/Websites/_admin/BUILD-THUMBSPAGE-CLIENTS/common.sh

Pause=y
function announce() { 
    echo
    echo $1
    if [ $Pause == 'y' ]; then 
        read -p 'Press enter/return to continue' 
    fi
}


#------------------------------------------------------------------------------
# 1) Update three image galleries in $C first, iff not already current.
# They usually are up to date, because thumbspage changes more often.
#------------------------------------------------------------------------------

read -p "Make galleries now in $C (y or n)? " userreply
if [[ -n $userreply && $userreply == 'y' ]]
then 
    cd $C/frigcal/docetc/docimgs
    platforms='macosx windows linux'
    for platform in $platforms; do
        py3 $C/thumbspage/thumbspage.py $platform <<-EOF
	
	
	
	
	EOF
    done

    # mergeall nested gallery: not used here
    # cd $C/mergeall/docetc
    # py3 $C/thumbspage/thumbspage.py GUI-changes-3.3 \
    #    useDynamicIndexLayout=True \
    #    inputCleanThumbsFolder=True inputThumbMaxSize=128,128 inputUseViewerPages=True
fi


#------------------------------------------------------------------------------
# 2) Make source-package zip in Code/, copy to Websites/, and unzip.
# The build.py script does some housecleaning, and runs a zip-create.py.
#------------------------------------------------------------------------------

announce 'Making source-package zip'
pubdir=$W/Programs/Current/Complete/frigcal-products

cd $C/frigcal/build/build-source
py3 build.py
cp -p Frigcal-source.zip $pubdir
cp -p Frigcal-source.zip ../../_private_/Frigcal-source--$stamp.zip

cd $pubdir
rm -rf unzipped
py3 $Z/zip-extract.py Frigcal-source.zip . -permissions
mv Frigcal-source unzipped


#------------------------------------------------------------------------------
# 3) Add analytics code, and assume image galleries are current.
# Else, run thumbspage first (step 1); analytics are anonymized ahead.
#------------------------------------------------------------------------------

announce 'Adding analytics'
cd unzipped

# main/newest guide
py3 $M/insert-analytics.py UserGuide.html

# screenshot galleries
py3 $M/insert-analytics.py docetc/docimgs/index.html
py3 $M/insert-analytics.py docetc/docimgs/macosx/index.html
py3 $M/insert-analytics.py docetc/docimgs/windows/index.html
py3 $M/insert-analytics.py docetc/docimgs/linux/index.html

# old docs: is it eol yet?
py3 $M/insert-analytics.py docetc/DeveloperGuide.html


#------------------------------------------------------------------------------
# 4) Copy the .zip and unzipped/ folder to union, zip as a combo for upload.
# The _PUBLISH.py step adds IP-anonymize code in analytics, and fixes readmes.
#------------------------------------------------------------------------------

announce 'Building site and upload zip'
cd $W
py3 _PUBLISH.py | tail -n 20

cd UNION/frigcal-products
py3 $Z/zip-create.py fccombo.zip unzipped Frigcal-source.zip -skipcruft


#------------------------------------------------------------------------------
# 5) Upload combo zip to site and unzip there: remakes .zip+unzipped/.
#------------------------------------------------------------------------------

announce 'Uploading and unzipping on server'
SCP fccombo.zip htdocs/frigcal-products
SSH <<-EOF
	cd htdocs/frigcal-products
	rm -rf unzipped Frigcal-source.zip
	unzip -d . fccombo.zip
	rm fccombo.zip
	exit
	EOF

rm fccombo.zip   # local UNION copy


#--------------------------------------------
# 6) Download and verify zip: live to local 
#--------------------------------------------

cd $temp
rm -rf UserGuide.html Frigcal-source.zip frigcal-source diffallf mergeallf

# content
printf '\n** Diff: there should be 1 diff in UserGuide for analytics\n'
curl -O https://learning-python.com/frigcal-products/unzipped/UserGuide.html
diff UserGuide.html $C/frigcal/UserGuide.html

# zipfile
printf '\n** Cmp: there should be no cmp output for zip\n'
curl -O https://learning-python.com/frigcal-products/Frigcal-source.zip
cmp -bl Frigcal-source.zip $C/frigcal/_private_/Frigcal-source--$stamp.zip

# unzippped content
py3 $Z/zip-extract.py Frigcal-source.zip . > /dev/null    # makes Frigcal-source/

printf '\n** Diffall: there should be 7 for unzip = -top, 4 pkgs~strips\n'
py3 $C/mergeall/diffall.py Frigcal-source $C/frigcal -skipcruft > diffallf
tail -n 13 diffallf

printf '\n** Diffall: search for *UNIQ to see diffs\n'
grep --context=8 '*UNIQ' diffallf

printf '\n** Mergeall: there should be 8 uniqueto 24 uniquefrom\n'
py3 $C/mergeall/mergeall.py $C/frigcal Frigcal-source -skipcruft -report > mergeallf
tail -n 10 mergeallf

printf '\n** Mergeall: these should mirror the diffall diffs\n'
tail -n 78 mergeallf

# keep to eyeball: rm -rf UserGuide.html Frigcal-source.zip Frigcal-source diffallf mergeallf
echo 'Bye.'
