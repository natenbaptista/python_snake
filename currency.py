#! /usr/bin/python
import pycurl
import requests
import xml.etree.ElementTree as ET
import xmltodict, json
import collections
import ConfigParser

url = 'http://spreadsheets.google.com/feeds/list/0Av2v4lMxiJ1AdE9laEZJdzhmMzdmcW90VWNfUTYtM2c/2/public/basic'
r = requests.get(url)
#print r.text
#root = ET.fromstring(r.text)
#print root.tag
#for child in root:
    #print(child.tag, child.attrib, child.text)
o = xmltodict.parse(r.text)
#j = json.dumps(o)

currencies = ['USD', 'INR', 'JPY', 'HKD', 'PHP', 'SGD']

xCurrencies = collections.OrderedDict()
for cur in currencies:
    xCurrencies[cur] = [1.0, 1.0]

print xCurrencies
for entry in o['feed']['entry']:
    currency = ''
    xRate = 1.0
    for key, value in entry.iteritems():
        try:
            if key == 'title':
                currency = value['#text']
            if key == 'content':
                xRate = float(value['#text'][8:])
        except:
            pass
    #print '{}={}'.format(currency, xRate)
    if currency in xCurrencies:
        xCurrencies[currency][0] = xRate
        xCurrencies[currency][1] = float('{0:.6f}'.format(1/xRate))
print xCurrencies
