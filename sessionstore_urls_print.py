#!/usr/bin/python
# Copyright (c) 2016 mgroseman - Mike Roseman
# Licensed under the MIT license
#  Use at your own risk
#
# Print current URLs in saved tabs by Firefox.
# Newer versions of Firefox seem to want it to be stopped for it to create 
#  the sessionstore.js file.   
# Location of that file:  $HOME/.mozilla/firefox/CACHHEDIR/sessionstore.js
#  backups are located in sessionstore-backups/
# Please backup your file before running this.  I guarantee no lack of bad things.


import simplejson, sys

if len(sys.argv) < 2:
    print >>sys.stderr, ("Usage: command <sessionstore_filename>\n"
                         "URLs in tab order will be dumped to stdout\n")
    sys.exit(1)

file = open(sys.argv[1], 'rb')

try:
    #Load json into array
    json = simplejson.load(file)

    for window in json["windows"]:
        for tab in window["tabs"]:
            entries = tab["entries"]
            if len(entries) > 0 :
	       #Current webpage is *last* entry in the list.  
               #Previous entries are the tab history
               print(entries[len(entries) - 1]["url"])

finally:
    file.close()
