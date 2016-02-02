#!/usr/bin/python
# Copyright (c) 2016 mgroseman - Mike Roseman
# Licensed under the MIT license
#  Use at your own risk
#
# Delete tabs containing the included URL in a sessionstore.js file.

# Newer versions of Firefox seem to want it to be stopped for it to create
#  the sessionstore.js file.
# Location of that file:  $HOME/.mozilla/firefox/CACHHEDIR/sessionstore.js
#  backups are located in sessionstore-backups/
# Please backup your file before running this.  I guarantee no lack of bad things.
#
# Note:  An easy way to read this one-line JSON is "cat sessionstore.js | json_reformat"

#So I can write to standard error in Python 2+3.  Then the print() statements don't affect the output

from __future__ import print_function
import simplejson, sys

if len(sys.argv) < 3:
    print >>sys.stderr, ("Usage: command sessionstore.js\n"
                         "Modified JSON will be printed to STDOUT\n")
    sys.exit(1)

file = open(sys.argv[1], 'rb')
try:
    i = 0
    json = simplejson.load(file)

    print("Searching for: %s" % sys.argv[2], file=sys.stderr)
    for window in json["windows"]:
        for tab in window["tabs"]:
            entries = tab["entries"]
            if len(entries) > 0 and entries[len(entries) - 1]["url"] == sys.argv[2]:
               i += 1
               print("Removing this tab:", file=sys.stderr)
               print(tab, file=sys.stderr)
               print("Found count: %d" % i, file=sys.stderr)
               #Delete this tab
               window["tabs"].remove(tab) 

    #Dump new JSON to standard out
    print(simplejson.dumps(json))

finally:
    file.close()
