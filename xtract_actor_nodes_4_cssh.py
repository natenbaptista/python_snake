#!/usr/bin/env python
'''

    THIS SCRIPT SHOULD BE RUN ON THE RECIVING TURRETS TO AUTOMATICALLY PICK UP LINES

'''
from subprocess import call
from time import sleep
import os
import re #for multiple delimter splitting
print "Extract Actor nodes for CSSH"

def executeCssh(nodes):
    #os.system("cssh 192.168.110.{"+nodes+"}")
    print "cssh 192.168.110.{"+nodes+"}"

def readNodes(filepath):
    mfile = open(filepath, 'r')
    csshList = []
    for mline in mfile:
        if 'turret' in mline:
            q = re.split('\(|\)', mline)
            oclet = q[1].split('.')
            csshList.append(oclet[3])
    csshStr = ",".join(csshList)
    executeCssh(csshStr)

readNodes('nodes.txt')