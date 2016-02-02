#!/bin/sh
# Copyright (c) 2016 mgroseman - Mike Roseman
# Licensed under the MIT license
#  Use at your own risk

# Wrapper around scripts to remove a list of URLs from Firefox's sessionstore.js
# Output is ${SESSIONSTORE}_modified"

# I know I should convert this to python and it's horribly slow since it processes only one URL at a time.  
# Since I don't need this script often, that is left as an exercise for the reader

#Description of parameters:
#BASE file is generatred via "sessionstore_urls_print.py sessionstore.js > BASEFILE"
#REMAINING file is BASE minus whatever URLs you want to remove.  I actually did a "sort -u" on it to remove duplicates before editing.  Needs to be sorted exactly same as BASE file, since it does a simple diff.
#SESSIONSTORE is sessionstore.js or a copy

if [ $# -lt 3 ]; then
    echo ""
    echo "Usage $0: BASE REMAINING SESSIONSTORE"
    echo ""
    echo "  BASE file -  generatred via \"sessionstore_urls_print.py sessionstore.js > BASEFILE\""
    echo "  REMAINING file  - BASE minus whatever URLs you want to remove.  You can do a \"sort -u\" on it to remove duplicates before editing. Needs to be sorted exactly same as BASE file, since it does a simple diff."
    echo "  SESSIONSTORE  - sessionstore.js or a copy"
    exit 1
fi

BASE=$1
REMAINING=$2
SESSIONSTORE=$3

#TMP=/tmp
# Since this is tmpfs on some systems, faster than disk writes
TMP=/dev/shm

TEMPDIFFFILE=$TMP/$$_diff.tmp
TEMPFILE=$TMP/$$.tmp
TEMPFILE2=$TMP/$$_2.tmp

diff $BASE $REMAINING | grep "<" | awk '{print $2}' > $TEMPDIFFFILE
cp $SESSIONSTORE $TEMPFILE

for i in `cat $TEMPDIFFFILE`
do
  echo "Searching for URL: $i"
  ./removestore_url_1.py $TEMPFILE "$i" > $TEMPFILE2
  mv $TEMPFILE2 $TEMPFILE
done

#Finished filename
cp $TEMPFILE ${SESSIONSTORE}_modified
echo "Created ${SESSIONSTORE}_modified"

#Clean up
rm $TEMPFILE2 $TEMPFILE $TEMPDIFFFILE
  
