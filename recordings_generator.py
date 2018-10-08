#!/usr/bin/env python
from subprocess import call
from time import sleep
import time
import datetime
import random
import os
import re #for multiple delimter splitting

turretDirectory = 'turret-a2'
noOfDaysBack = 10
recordingsEachDay = 200
userName = 'Naten.Baptista'

print "Recordings generator"

'''
Main folder name "20170822T015946.780246-Naten.Baptista-Naten.Baptista-13118875729620131765"
data in folders "header", "logged", "media.wav"
header contains
{
    "id": "13118875729620131765",
    "quick_id": "13118875",
    "version": 3,
    "owner": {
        "O": "Bank A",
        "role": "User",
        "CN": "Naten.Baptista"
    },
    "participants": [{
        "name": "Naten.Baptista",
        "type": "user",
        "location": "192.168.110.119:33393",
        "display_info": "Naten Baptista"
    }, {
        "name": "gateway-a1",
        "type": "external",
        "location": "192.168.110.150:33290",
        "display_info": "400011"
    }],
    "line_info": [{
        "name": "400011",
        "type": "ARD"
    }],
    "begin": "20170822T015946.868215",
    "end": "20170822T015949.369734",
    "direction": "outgoing",
    "call_progress": "Received",
    "answer_devices": ["handset-left"]
}
'''

def recDay(backDays):
    today = datetime.datetime.now()
    back = datetime.timedelta(days = backDays)
    return (today-back)

# generate a bunch of dates backedated from the current date
def generateDates(mNoOfDaysBack):
    return [recDay(x) for x in range(0,mNoOfDaysBack)]

#generate buch of timestamps for each recording foler based on mRecordingsEachDay
def generateTimestampsFromDay(mDate, mRecordingsEachDay):
    #create a start time on this dat at 09:00:00
    startOfDay = datetime.datetime(mDate.year, mDate.month, mDate.day, 9, 0, 0)
    # then depending upon the mRecordingsEachDay
    # add that many time instances every 30 sec
    mList = []
    for x in range(mRecordingsEachDay):
        n = startOfDay+datetime.timedelta(seconds = 30*x)
        mList.append(n.strftime("%Y%m%dT%H%M%S.780246"))
    return mList

#generate a bung of folder list with the username and fake random VRI
def generateFolderList(mTimestampList, mUserName):
    mList = []
    for xn in mTimestampList:
        nFolder = '{}-{}-{}-{}'.format(xn, mUserName, mUserName, '13118875729620131765')
        mList.append(nFolder)
    return mList

def createHeaderFile(mPath, mFolder):
    timestamp, user1, user2, vri = mFolder.split('-')
    #print '{}{}{}'.format(timestamp[0:13], random.randint(10, 59), timestamp[15:])
    #print user1
    #print user2
    #print vri
    fData = '{"id":"'+vri+'","quick_id":"'+vri[0:8]+'","version":3,"owner"'+\
        ':{"O":"Bank A","role":"User","CN":"'+user1+\
        '"},"participants":[{"name":"'+user1+\
        '","type":"user","location":"192.168.110.119:44896","display_info":"'+user1+\
        '"},{"name":"gateway-a1","type":"external","location":"192.168.110.150:33290"'+\
        ',"display_info":"400002"}],"line_info":[{"name":"400002","type":"ARD"}],"begin":"'+timestamp+\
        '","end":"'+'{}{}{}'.format(timestamp[0:13], random.randint(10, 59), timestamp[15:])+\
        '","direction":"outgoing","call_progress":"Received","answer_devices":["handset-left"]}at'
    mFile = open(mPath+'/header', 'w')
    mFile.write(fData)
    mFile.close()

def createRecordingFiles(mPath, mFolder):
    open(mPath+'/media.wav', 'a').close()
    open(mPath+'/logged', 'a').close()
    createHeaderFile(mPath, mFolder)

daysList = generateDates(noOfDaysBack)
print daysList

#generate a list of all proper folder names
recFolders = []
for tDate in daysList:
    timestampList = generateTimestampsFromDay(tDate, recordingsEachDay)
    recFolders = recFolders+generateFolderList(timestampList, userName)

#make all the directories
for thisFolder in recFolders:
    print thisFolder
    recordingFolder = '/var/tmp/{}/recordings/{}'.format(turretDirectory, thisFolder)
    if not os.path.exists(recordingFolder):
        os.makedirs(recordingFolder)
    createRecordingFiles(recordingFolder, thisFolder)
