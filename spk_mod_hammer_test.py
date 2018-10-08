#!/usr/bin/env python
from subprocess import call
from time import sleep

call(["G_station", "--msg", "20001" "CH_10_UNLATCH__"])

for mcount in range(0, 1000):
    text = "CH_10_LABEL_{}_".format(mcount)
    call(["G_station", "--msg", "20001", text])
    sleep(0.1)

