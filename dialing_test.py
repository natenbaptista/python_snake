#!/usr/bin/env python
from subprocess import call
from time import sleep
import random
import re #for multiple delimter splitting

print "Dialing Load Test"

def latch_channel(ichannel, slatch):
    channel = "CONTROL_PANEL_SKP_%d_PTL_%s_" % (ichannel, slatch)
    call(["G_station", "--msg", channel])
    time.sleep(0.07)

def mSpeedial(number):
    call(["G_station", "--msg", "SPEEDIAL_"+number])

def mSleep(cSeconds):
    print cSeconds
    if 'RANDOM' in cSeconds:
        #sleep(float(cSeconds))
        print 'Random sleep'+cSeconds
        cSecT = re.split(' |,', cSeconds)
        #print cSecT[1], cSecT[2]
        sleep(random.randint(float(cSecT[1]), float(cSecT[2])))
        return
    sleep(float(cSeconds))


def mDialNumber(number):
    for cC in number:
        call(["G_station", "--msg", "DIAL_"+cC])
        sleep(0.25)
    call(["G_station", "--msg", "DIAL_11"])

def mDrop(handset):
    call(["G_station", "--msg", "ACTION_DROP_"+handset])

def mSwitch(handset):
    call(["G_station", "--msg", "ACTION_SWITCH_"+handset])

def cCommand(cmd):
    instrc = cmd.split('_')
    print instrc[0]
    if instrc[0] == 'SPEEDIAL':
        mSpeedial(instrc[1])
    elif instrc[0] == 'SLEEP':
        mSleep(instrc[1])
    elif instrc[0] == 'DIAL':
        mDialNumber(instrc[1])
    elif instrc[0] == 'DROP':
        mDrop(instrc[1])
    elif instrc[0] == 'SWITCH':
        mSwitch(instrc[1])
    else:
        pass




def runTest(msequence):
    print sequence
    while (1):
        for sq in sequence:
            cCommand(sq)
            sleep(0.07)

        sleep(random.randint(2,5))


sequence = [\
    'SWITCH_1',\
    'DROP_1',
    'SLEEP_0.5',\
    'DIAL_967180550',\
    'SLEEP_RANDOM 3,4',\
    'DROP_1',\
    'SLEEP_RANDOM 1,2'\
     ]

    #'SPEEDIAL_967180550',\
    #'SLEEP_RANDOM 3,7',\
    #'DROP_1',
    #'SLEEP_0.5',\
    #'DIAL_967180550',\
    #'SLEEP_RANDOM 3,7',\
    #'DROP_1',\
    #'SLEEP_0.05',\
    #'DROP_1',\
    #'SLEEP_0.05',\
    #'DROP_1',\
    #'SLEEP_0.05',\
    #'DROP_1',\
    #'SLEEP_0.06',\
    #'DROP_2',\
    #'SLEEP_0.05',\
    #'DROP_2',\
    #'SLEEP_0.05',\
    #'DROP_2',\

#sequence = ['SLEEP_RANDOM 3,7']
#sequence = ['SLEEP_3']
runTest(sequence)


