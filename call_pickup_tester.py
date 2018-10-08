#!/usr/bin/env python
'''

    THIS SCRIPT SHOULD BE RUN ON THE RECIVING TURRETS TO AUTOMATICALLY PICK UP LINES

'''
from subprocess import call
from time import sleep
import time
import random
import re #for multiple delimter splitting
import logging
print "Pickup Load Test"

def mSpeedial(number):
    call(["G_station", "--msg", "SPEEDIAL_"+number])

def mSleep(cSeconds):
    print cSeconds
    if 'RANDOM' in cSeconds:
        #sleep(float(cSeconds))
        cSecT = re.split(' |,', cSeconds)
        #print cSecT[1], cSecT[2]
        mRandomSeconds = random.randint(float(cSecT[1]), float(cSecT[2]))
        print 'Random sleeping {} seconds @ {}'.format(mRandomSeconds, time.strftime('%H:%M:%S'))
        sleep(mRandomSeconds)
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

def mHold(handset):
    call(["G_station", "--msg", "ACTION_HOLD_"+handset])

def mAccess(handset):
    call(["G_station", "--msg", "ACCESS_"+handset])

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
    elif instrc[0] == 'HOLD':
        mHold(instrc[1])
    elif instrc[0] == 'ACCESS':
        mAccess(instrc[1])
    else:
        pass

#users the button range list
def runTestWithRange(mPositionRange):
    print mPositionRange
    nPositons = []
    for nRange in mPositionRange:
        nStart, nStop = nRange.split('-')
        for nPosition in range(int(nStart), int(nStop)+1):
            nPositons.append(str(nPosition))

    print nPositons
    mLength =  len(nPositons)
    while(1):
        nPositon = int(nPositons[random.randint(0,mLength-1)])
        cCommand('ACCESS_{}'.format((nPositon)))
        cCommand('SLEEP_RANDOM 10,20')
        if nPositon%2 == 0:
            cCommand('DROP_1')
        else:
            cCommand('HOLD_1')
        cCommand('SLEEP_RANDOM 2,4')

def make_call(line):
    number, position = line.split('_')
    cCommand('SPEEDIAL_'+number)
    cCommand('SLEEP_RANDOM 1,2')
    cCommand('HOLD_1')
    cCommand('SLEEP_RANDOM 2,4')

def drop_call(line):
    number, position = line.split('_')
    cCommand('ACCESS_{}'.format((int(position))))
    cCommand('SLEEP_RANDOM 1,2')
    cCommand('DROP_1')
    cCommand('SLEEP_RANDOM 2,4')


def runTest(mlines):
    print mlines
    logging.basicConfig(filename='outgoing.log', level=logging.INFO)
    total_calls = 0
    mLength =  len(mlines)
    while(1):
        number, position = mlines[random.randint(0,mLength-1)].split('_')
        print('Calling {} {} @ {}'.format(number, position, time.strftime('%H:%M:%S')))
        #logging.info('So should this')
        #print number
        #print position
        cCommand('ACCESS_{}'.format(position))
        cCommand('SLEEP_0.5')
        cCommand('DIAL_'+number)
        cCommand('SLEEP_RANDOM 30,60')
        if int(position)%25 == 0:
            cCommand('DROP_1')
        else:
            cCommand('HOLD_1')
        cCommand('SLEEP_RANDOM 1,2')




'''
 The mlines is an array which needs to be loaded with speedial number + button positions
 So in this case [Speeddial number]_[button position].
'''

mlines = [\
    '442074963001_1500',\
    '442074963001_1501',\
    '442074963001_1502',\
    '442074963001_1503',\
    '442074963002_1504',\
    '442074963002_1505',\
    '442074963002_1506',\
    '442074963002_1507',\
    '442074963003_1508',\
    '442074963003_1509',\
    '442074963003_1510',\
    '442074963003_1511',\
    '442074963004_1512',\
    '442074963004_1513',\
    '442074963004_1514',\
    '442074963004_1515',\
    '442074963005_1516',\
    '442074963005_1517',\
    '442074963005_1518',\
    '442074963005_1519',\
    '442074963006_1520',\
    '442074963006_1521',\
    '442074963006_1522',\
    '442074963006_1523',\
    '442074963007_1524',\
    '442074963007_1525',\
    '442074963007_1526',\
    '442074963007_1527',\
    '442074963008_1528',\
    '442074963008_1529',\
    '442074963008_1530',\
    '442074963008_1531',\
    '442074963009_1532',\
    '442074963009_1533',\
    '442074963009_1534',\
    '442074963009_1535',\
    '442074963010_1536',\
    '442074963010_1537',\
    '442074963010_1538',\
    '442074963010_1539',\
    '442074963011_1540',\
    '442074963011_1541',\
    '442074963011_1542',\
    '442074963011_1543',\
    '442074963012_1544',\
    '442074963012_1545',\
    '442074963012_1546',\
    '442074963012_1547',\
    '442074963013_1548',\
    '442074963013_1549',\
    '442074963013_1550',\
    '442074963013_1551',\
    '442074963014_1552',\
    '442074963014_1553',\
    '442074963014_1554',\
    '442074963014_1555',\
    '442074963015_1556',\
    '442074963015_1557',\
    '442074963015_1558',\
    '442074963015_1559',\
    '442074963016_1560',\
    '442074963016_1561',\
    '442074963016_1562',\
    '442074963016_1563',\
    '442074963017_1564',\
    '442074963017_1565',\
    '442074963017_1566',\
    '442074963017_1567',\
    '442074963018_1568',\
    '442074963018_1569',\
    '442074963018_1570',\
    '442074963018_1571',\
    '442074963019_1572',\
    '442074963019_1573',\
    '442074963019_1574',\
    '442074963019_1575',\
    '442074963020_1576',\
    '442074963020_1577',\
    '442074963020_1578',\
    '442074963020_1579',\
    '442074963021_1580',\
    '442074963021_1581',\
    '442074963021_1582',\
    '442074963021_1583',\
    '442074963022_1584',\
    '442074963022_1585',\
    '442074963022_1586',\
    '442074963022_1587',\
    '442074963023_1588',\
    '442074963023_1589',\
    '442074963023_1590',\
    '442074963023_1591',\
    '442074963024_1592',\
    '442074963024_1593',\
    '442074963024_1594',\
    '442074963024_1595',\
    '442074963025_1596',\
    '442074963025_1597',\
    '442074963025_1598',\
    '442074963025_1599',\
    '442074963026_1600',\
    '442074963026_1601',\
    '442074963026_1602',\
    '442074963026_1603',\
    '442074963027_1604',\
    '442074963027_1605',\
    '442074963027_1606',\
    '442074963027_1607',\
    '442074963028_1608',\
    '442074963028_1609',\
    '442074963028_1610',\
    '442074963028_1611',\
    '442074963029_1612',\
    '442074963029_1613',\
    '442074963029_1614',\
    '442074963029_1615',\
    '442074963030_1616',\
    '442074963030_1617',\
    '442074963030_1618',\
    '442074963030_1619',\
    '442074963031_1620',\
    '442074963031_1621',\
    '442074963031_1622',\
    '442074963031_1623',\
    '442074963032_1624',\
    '442074963032_1625',\
    '442074963032_1626',\
    '442074963032_1627',\
    '442074963033_1628',\
    '442074963033_1629',\
    '442074963033_1630',\
    '442074963034_1631',\
    '442074963034_1632',\
    '442074963034_1633',\
    '442074963034_1634',\
    '442074963035_1635',\
    '442074963035_1636',\
    '442074963035_1637',\
    '442074963035_1638',\
    '442074963036_1639',\
    '442074963036_1640',\
    '442074963036_1641',\
    '442074963036_1642',\
    '442074963037_1643',\
    '442074963037_1644',\
    '442074963037_1645',\
    '442074963037_1646',\
    '442074963038_1647',\
    '442074963038_1648',\
    '442074963038_1649',\
    '442074963038_1650',\
    '442074963033_1651',\
    '442074963039_1652',\
    '442074963039_1653',\
    '442074963039_1654',\
    '442074963039_1655',\
    '442074963040_1656',\
    '442074963040_1657',\
    '442074963040_1658',\
    '442074963040_1659',\
    '442074963041_1660',\
    '442074963041_1661',\
    '442074963041_1662',\
    '442074963041_1663',\
    '442074963042_1664',\
    '442074963042_1665',\
    '442074963042_1666',\
    '442074963042_1667',\
    '442074963043_1668',\
    '442074963043_1669',\
    '442074963043_1670',\
    '442074963043_1671',\
    '442074963044_1672',\
    '442074963044_1673',\
    '442074963044_1674',\
    '442074963044_1675',\
    '442074963045_1676',\
    '442074963046_1677',\
    '442074963047_1678',\
    '442074963048_1679',\
    '442074963049_1680',\
    '442074963050_1681',\
    '442074963051_1682',\
    '442074963051_1683',\
    '442074963051_1684',\
    '442074963051_1685',\
    '442074963052_1686',\
    '442074963052_1687',\
    '442074963052_1688',\
    '442074963052_1689',\
    '442074963053_1690',\
    '442074963053_1691',\
    '442074963053_1692',\
    '442074963053_1693',\
    '442074963054_1694',\
    '442074963054_1695',\
    '442074963054_1696',\
    '442074963054_1697',\
    '442074963055_1698',\
    '442074963055_1699',\
    ]
#mPositionRange = [\
    #'351-360',\
    #'363-365',\
    #]

runTest(mlines)
#runTestWithRange(mPositionRange)

