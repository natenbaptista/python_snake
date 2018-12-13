#!/usr/bin/env python
# If you are sure that the created dates are perfect and the modified dates are wrong,
# then user this script to add the created date to the filename.
# Then use another scrip later to force the modified date same as the filename.

import os
import time
import datetime
import sys
import random

dpath = 'E:\date_change_folder\/'

for filename in os.listdir(dpath):
    # a = datetime.datetime.fromtimestamp(os.path.getmtime(dpath + filename))
    file_name, file_extension = os.path.splitext(filename)
    a = datetime.datetime.fromtimestamp(os.path.getctime(dpath + filename))
    year = str(a.year)
    year = year[2:]
    month = str(a.month).zfill(2)
    day = str(a.day).zfill(2)
    hour = str(a.hour).zfill(2)
    minute = str(a.minute).zfill(2)
    second = str(a.second).zfill(2)
    print ("<{}> File real Created date time ({} {} {} {}:{}:{})".format(filename, year, month, day, hour, minute, second))
    new_filename = year + month + day + '_' + hour + minute + second + file_extension
    print ('    Renaming <{}> to <{}>.'.format(filename, new_filename))
    while True:
        try:
            os.rename(dpath + filename, dpath + new_filename)
            break
        except:
            print '     *ERROR* Duplicate File Name! attempting to rename again'
            second = str(random.randint(0, 59)).zfill(2)
            new_filename = year + month + day + '_' + hour + minute + second + file_extension
