#===================================================================
# Automatically build+publish this folder's content, only.
#
# Launch this script from Terminal in its own folder, with:
#     cd $C/frigcal/docetc/docimgs
#     bash _publish.sh
#
# Also run by $W/_admin/BUILD-THUMBSPAGE-CLIENTS/_PUBLISH.sh, to 
# update all thumbspage external clients in a single step.
#
# This script builds screenshot folders for online viewing only.
# This app also has a build/ folder for complete-package builds.
#===================================================================

# get common defs
source ~/MY-STUFF/Websites/_admin/BUILD-THUMBSPAGE-CLIENTS/common.sh

# the root page could be an imageless gallery page, but isn't
platforms='macosx windows linux'

# build 3 galleries (+ android someday?)
for platform in $platforms; do
    py3 $C/thumbspage/thumbspage.py $platform <<-EOF
	
	
	
	
	EOF
done	

# cp docimgs/ to deleted pub version
cd $W/Programs/Current/Complete/frigcal-products/unzipped/docetc
rm -rf docimgs
cp -pR $C/frigcal/docetc/docimgs .

# installed tag comment in all 4 (HEADER in galleries)
py3 $M/insert-analytics.py docimgs/index.html
for platform in $platforms; do
    py3 $M/insert-analytics.py docimgs/$platform/index.html
done

# publish to union and zip; adds ip-anon line to all index.html for zip+upload
cd $W
py3 _PUBLISH.py | tail -n 20
cd UNION/frigcal-products/unzipped/docetc
py3 $Z/zip-create.py docimgs.zip docimgs -skipcruft | tail -n 20

# upload, unzip, remove
SCP docimgs.zip htdocs/frigcal-products/unzipped/docetc
SSH <<-EOF
	cd htdocs/frigcal-products/unzipped/docetc
	rm -rf docimgs
	unzip -d . docimgs.zip
	rm docimgs.zip
	exit
	EOF

rm docimgs.zip    # local UNION copy
