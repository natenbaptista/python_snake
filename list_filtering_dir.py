#!/usr/bin/env python
import os

def printlist(mlist):
    print '\n{}'.format(filelist)


filelist = os.listdir("/home/atp/gui/")
printlist(filelist)

#can sort, sorted() function takes list and tuples or other iterations as well
filelist = sorted(filelist)
printlist(filelist)

#Now filter using list comprehension only G_* files
filelist = [prgm for prgm in filelist if prgm[0:2] == "G_"]
printlist(filelist)
