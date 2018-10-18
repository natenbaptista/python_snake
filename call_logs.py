#!/usr/bin/env python
import sys
import re
import sqlite3
import date_time
import csv

class sqlite:
    def __init__(self, database):
        print 'Trying to access "{}"'.format(database)
        self.conn = sqlite3.connect(database)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()
        #self.cur.execute('CREATE TABLE IF NOT EXISTS logs (start_time TEXT, direction TEXT, cli TEXT, vri TEXT)')
        #self.cur.execute("select name from sqlite_master where type='table'")
        #print self.cur.fetchall()

    def query(self, mdate):
        print mdate
        self.cur.execute("SELECT * FROM call_log WHERE begin_date LIKE '%s%%'" % mdate)
        return self.cur.fetchall()

    def __del__(self):
        print('Closing DB')
        self.conn.close()


def analyze_database(dbfile, start_date, end_date):
    print 'Analyzing DB "{}" from {} to {}'.format(dbfile, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    db = sqlite(dbfile)
    call_log = [['VRI', 'Start Date', 'End Date', 'Duration', 'Owner', 'Direction', 'CLI', 'Progress', 'Foward Reason' ,'Answered Line', 'Incoming Call']]

    date_list = date_time.date_range_list(start_date, end_date)
    print date_list

    for mdate in date_list:
        res = db.query(mdate)
        reslist = [list(record) for record in res] # Convert all the tupel record to list
        for record in reslist:
            duration = str(date_time.utc_str_date_obj_difference(record[2][0:15], record[3][0:15]))
            duration = (duration, '0'+duration) [len(duration) < 8]
            duration = (duration, duration[3:]) [duration[0:2] == '00']
            record.insert(4, "'"+duration)
            record[2] = date_time.convert_from_zone(date_time.str_to_date(record[2][0:15], "%Y%m%dT%H%M%S"), "UTC", "Asia/Hong_Kong").strftime("%Y-%m-%d %H:%M:%S")
            record[3] = date_time.convert_from_zone(date_time.str_to_date(record[3][0:15], "%Y%m%dT%H%M%S"), "UTC", "Asia/Hong_Kong").strftime("%Y-%m-%d %H:%M:%S")
            del record[0]
            record = ",".join(record)
        call_log = call_log+reslist

    #for record in call_log:
        #print record

    with open('call_logs_csv.csv', 'wb') as mycsv:
        wr = csv.writer(mycsv, quoting=csv.QUOTE_ALL)
        wr.writerows(call_log)
    del db


def argument_error(error_msg):
    print error_msg
    print '[Database file path] Start Date[YYYY-MM-DD] Optional End Date [YYYY-MM-DD]'
    sys.exit(1)

def make_date(strdate):
    x = date_time.str_to_date(strdate, "%Y%m%d")
    if x == None:
        print 'Bad date format {}.'.format(strdate)
        sys.exit(1)
    return x

if __name__ == "__main__":
    print 'Call Log V0.1'
    start = make_date(sys.argv[2])
    try:
        end = make_date(sys.argv[3])
    except:
        end = make_date(sys.argv[2])

    if not sys.argv[1:]:
        argument_error('No database file supplied.')

    if not sys.argv[2:]:
        argument_error('No Start Date supplied.')

    analyze_database(sys.argv[1], start, end)