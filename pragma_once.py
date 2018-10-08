#!/usr/bin/env python
'''
Prases a file and adds pragmc once to the file
'''
import fnmatch
import os

filepath = '/home/atp/atp-dev/src/gui/common/actor_connection.h'


def add_pragma_once(filepath):
    pragma_once = "#pragma once"
    mfile = open(filepath, 'r+')
    first_line = mfile.readline().strip()
    #print '<'+first_line+'>'
    if first_line != pragma_once:
        mfile.close()
        print 'Not there instead <'+first_line+'>, so adding...'
        with open(filepath, 'r+') as mfile:
            content = mfile.read()
            mfile.seek(0, 0)
            mfile.write(pragma_once.rstrip('\r\n') + '\n' + content)

matches = []
for root, dirnames, filenames in os.walk('/home/atp/atp-dev/src/gui/'):
     for filename in fnmatch.filter(filenames, '*.h'):
         matches.append(os.path.join(root, filename))

for fline in matches:
    print fline
    add_pragma_once(fline)

