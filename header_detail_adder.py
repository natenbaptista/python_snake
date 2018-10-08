#!/usr/bin/env python
'''
Prases a file and adds pragmc once to the file
'''
import fnmatch
import os

global h_details
h_details="/*\n *  AMP(Adaptive Media Platform)\n *  @author     Naten Steven Baptista\n *              Anupam Mukherjee\n *  @version    0.0.0 All Rights Reserved (C) Enepath\n */"

filepath = '/home/atp/atp-dev/src/gui/common/actor_connection.h'


def add_header_details(filepath):
    mfile = open(filepath, 'r+')
    h_line = mfile.readline().strip()
    mfile.close()
    print '<'+h_line+'>'
    if h_line != "/*":
        with open(filepath, 'r+') as mfile:
            content = mfile.read()
            mfile.seek(0, 0)
            mfile.write(h_details+'\n'+content)


matches = []
for root, dirnames, filenames in os.walk('/home/atp/atp-dev/src/gui/'):
     for filename in fnmatch.filter(filenames, '*.h'):
         matches.append(os.path.join(root, filename))

for fline in matches:
    print fline
    add_header_details(fline)

