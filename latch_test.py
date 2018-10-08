#!/usr/bin/env python
from subprocess import call
import time

print "Latch Test"

def latch_channel(ichannel, slatch):
    channel = "CONTROL_PANEL_SKP_%d_PTL_%s_" % (ichannel, slatch)
    call(["G_station", "--msg", channel])
    time.sleep(0.1)

for i in range(1,4):
    latch_channel(i, "LATCHED")
for i in range(1,4):
    latch_channel(i, "UNLATCHED")
