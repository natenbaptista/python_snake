#!/usr/bin/env python
'''

    THIS SCRIPT WILL SCP TO MULTIPLE

'''
from subprocess import call
from time import sleep
import time
import random
import re #for multiple delimter splitting
import logging
print "SCP to muliple host"

mHosts = [\
    '192.168.110.135',\
    '192.168.110.137',\
    '192.168.110.133',\
    '192.168.110.188',\
    '192.168.110.211',\
    '192.168.110.209',\
    '192.168.110.190',\
    '192.168.110.213',\
    '192.168.110.191',\
    '192.168.110.195',\
    '192.168.110.194',\
    '192.168.110.187',\
    ]

for mHost in mHosts:
    call(["scp", "G_call_ctl.py", mHost+":"])
    #call(["scp", "call_dropper.py", mHost+":"])
