#!/usr/bin/env python
import os
import re  # re is regulare expression operator
from subprocess import call

dpath = "/home/atp/Downloads/test-date-pics/"


def get_pic_timestamp(filename):
    msplit = re.split('\_|\.', filename)  # regular expression split _ & .
    return msplit[1] + msplit[2]

def get_rmscr_timestamp(filename):
    msplit = re.split('\_|\.', filename)  # regular expression split _ & .
    return msplit[0] + msplit[1]

# touch -t 201202121500.00 monkey


def set_date_for_file(mdatetime, filename, dpath):
    mcmd = ['touch', '-t', mdatetime[0:12], dpath + filename]
    print mcmd
    #running = ["ls", "-l"]
    call(mcmd)

for filename in os.listdir(dpath):
    print filename
    # if any(re.findall(r'PIC_|b|c', filename, re.IGNORECASE)):
    #     print 'found'
    # else:
    #     print 'not found'
    if 'PIC_' in filename:
        mdate = get_pic_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    elif '_rmscr' in filename:
        mdate = get_rmscr_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)

print os.name
