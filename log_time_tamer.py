#!/usr/bin/env python
'''
Parses a guilog current or last whose file is specified in 'filepath'
and changes all UTC reocrded timestamps to local time specified in the
timezone().
Use ./log_time_tamer.py > test_local_time.txt (pipe to file)
'''
from datetime import datetime, date
import pytz
from pytz import timezone

filepath = '/home/atp/Downloads/customer_debugging/stratis/17.07.10/current'

def get_my_timezone_time(utc_time_str):
    if len(utc_time_str.strip()) is not 15:
        return '*'+utc_time_str+'*'
    try:
        woutc = datetime.strptime(utc_time_str, "%Y%m%d-%H%M%S") #without UTC [time naive]
    except:
        return '*'+utc_time_str+'*'
    wutc = pytz.utc.localize(woutc) #localized with UTC [time aware]
    #print wutc
    myztime = wutc.astimezone(timezone('Asia/Singapore')) #convert to Zone
    return myztime.strftime("%Y%m%d-%H%M%S")

mfile = open(filepath, 'r')
mfind = '201707'
for mline in mfile:
    if mfind in mline:
        mline.strip()
        start = mline.find(mfind)
        utc_time_str = mline[start:start+15]
        my_time_str = get_my_timezone_time(utc_time_str)
        mline = mline.replace(utc_time_str, my_time_str)
        print mline.strip()
    else:
        print mline.strip()

