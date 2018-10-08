#!/usr/bin/env python

from time import sleep
import os

waction = [
    ["tickly", 0.5],
    ["tickle", 0.2],
    ["tickle", 0.2],
    ]

print os.getcwd()
for paction in waction:
    print paction[0]
    sleep(paction[1])