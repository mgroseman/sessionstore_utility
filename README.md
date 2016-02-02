# sessionstore_utility
Linux utilities to both display and delete URLs contained in a sessionstore.js file, which Firefox's method to save a tab session.

When Firefox is configured to save your tabs, it will create a sessionstore.js file when it shuts down.
  (There is also a recovery.js that is similar and is probably used for crashes.  Either can be used by these scripts.)
  
The file is a One-Line JSON format, which is almost impossible to read easily.
One way to convert the file to human-readable JSON is to use this utility included on some Linuxes:  "json_reformat"
I'm not sure if Firefox can read a coverted file, but you are welcome to try.

I had about 5,000 open tabs on my main computer.  I needed an offline way to weed them down, since the browser was becoming sluggish.  This is that tool, since I couldn't find anything similar.
You can simply dump a sessionstore.js to view the list of URLs if you want to save for later, or you can use that output to generate a difference list of URLs you want to remove.  
Usecases:   
  A) You have way too many tabs open and the system is either sluggish or out of memory.
  B) There is a tab out there that is causing an issue.
  C) You just want a text dump of all the URLs someone had open.  (Could be useful for forensics.)

The wrapper shell script is horribly inefficient if you have many tabs open, but it worked for my needs.  About 30 minutes to remove all 5,000 tabs from a 5,000 tab file.  (You'd never actually do that)

Scripts:
sessionstore_urls_print.py - Will print all URLs from sessionstore.js to STDOUT
sessionstore_removeurl.py - Will remove one URL from sessionstore.js and send new version to STDOUT
sessionstore_wrapper.sh  - Wrapper to remove a large set of URLs.

* Copyright (c)2016 Mike Roseman
* Licensed under the MIT license
*  Use at your own risk.  I have only done limited testing on a single use-case.
