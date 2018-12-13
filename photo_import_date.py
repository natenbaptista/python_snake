#!/usr/bin/env python
'''
This program was used to change the date timestamps of photos
that were moved from the Xperia internal memory.
This program is ment to run in linux only.
'''
import os
import re  # re is regulare expression operator
import datetime
import time
dpath = "C:\Data\Downloads\phoney\/"
if os.name is 'nt':
    print 'Operating system is WINDOWS'
    import pywintypes
    import win32file
    import win32con


def get_pic_timestamp(filename):
    msplit = re.split('\_|\.', filename)  # regular expression split _ & .
    return msplit[1] + msplit[2]


def get_screenshot_timestamp(filename):
    msplit = re.split('\_|\-|\.', filename)  # regular expression split _ & .
    return msplit[1] + msplit[2]


def get_rmscr_timestamp(filename):
    msplit = re.split('\_|\.', filename)  # regular expression split _ & .
    return msplit[0] + msplit[1]


def get_img_timestamp(filename):
    msplit = re.split('\_|\.', filename)  # regular expression split _ & .
    return msplit[1] + '000000'


def set_date_for_file(mdatetime, filename, dpath):
    if os.name is 'nt':  # for windows OS
        print mdatetime
        ndatetime = datetime.datetime(
            int(mdatetime[0:4]),
            int(mdatetime[4:6]),
            int(mdatetime[6:8]),
            int(mdatetime[8:10]),
            int(mdatetime[10:12]),
            int(mdatetime[12:14]))
        print ndatetime
        # Now convert it into seconds
        nseconds = time.mktime(ndatetime.timetuple())
        # Note that this section changes the CREATED DATE and not the modified date
        wintime = pywintypes.Time(nseconds)
        winfile = win32file.CreateFile(
            dpath + filename, win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None, win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL, None)
        win32file.SetFileTime(winfile, wintime, None, None)
        winfile.close()
        # now change the modified and accessed time as well
        os.utime(dpath + filename, (nseconds, nseconds))
    elif os.name is 'posix':  # for linux OS
        mcmd = ['touch', '-t', mdatetime[0:12], dpath + filename]
        print mcmd


for filename in os.listdir(dpath):
    print filename
    # if any(re.findall(r'PIC_|b|c', filename, re.IGNORECASE)):
    #     print 'found'
    # else:
    #     print 'not found'
    if bool(re.search('PIC_', filename)):  # can use regular expression search as well
        mdate = get_pic_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    elif 'Screenshot_' in filename:
        mdate = get_screenshot_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    elif '_rmscr' in filename:
        mdate = get_rmscr_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    elif 'IMG_' in filename:
        mdate = get_img_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    elif 'DSC_' in filename:
        mdate = get_img_timestamp(filename)
        set_date_for_file(mdate, filename, dpath)
    # break
