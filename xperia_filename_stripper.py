#!/usr/bin/env python
# Use this to extract/subtract a string from the filename or strip characters from the end of the file name
# This script only RENAMES files and DOES NOT apply timestamps to the file or changes the modification date.

import os
import time
import datetime
import sys
import random

dpath = 'E:\/xperia_filename_date_good\/'

string_len_to_match = len('IMG-20180411-WA0003.jpg')
extract_this = 'IMG-20'  # must contain this string in the extraction
start_extraction = 0  # this is a start at zero index not 1
strip_char_from_end = 0  # if zero then nothing is stripped
preview = False  # This if True will not perfrm the rename action but allow you to preview changes

extract_this = extract_this.lower()
extract_this_len = len(extract_this)
for filename in os.listdir(dpath):
    file_name, file_extension = os.path.splitext(filename)
    # filename_extracted = file_name[start_extraction:len(extract_this) + start_extraction]
    file_name = file_name.lower()
    # check if 'extract_this' is present from the 'start_extraction' position
    if file_name[start_extraction:len(extract_this) + start_extraction] == extract_this:
        print ('Matched: Filename <{}> Extension <{}>.'.format(file_name, file_extension))
        # Subtract the required characters 'extract_this' from given position 'start_extraction'
        file_name_a = file_name[0:start_extraction]
        file_name_b = file_name[start_extraction + len(extract_this):]
        new_filename = file_name_a + file_name_b
        # print('file_a <{}> file_b <{}> new_filename <{}>'.format(file_name_a, file_name_b, new_filename))
        # strip trailing characters
        new_filename = new_filename[0:len(new_filename) - strip_char_from_end]
        print ('New file name <{}{}>'.format(new_filename, file_extension))
        if preview == True:
            continue
        while True:
            try:
                os.rename(dpath + filename, dpath + new_filename + file_extension)
                break
            except:
                print '*ERROR* Duplicate File Name! Skipping'
