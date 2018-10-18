#!/usr/bin/env python
import datetime
import pytz

def str_to_date(str_date, date_format):
    try:
        return datetime.datetime.strptime(str_date, date_format)
    except ValueError:
        return None

def convert_from_zone(date_obj, zone_1, zone_2):
    old_timezone = pytz.timezone(zone_1)
    new_timezone = pytz.timezone(zone_2)
    return old_timezone.localize(date_obj).astimezone(new_timezone)

#requires the objects in UTC form as 20181012T095818.758873 style
def utc_str_date_obj_difference(utc_str_date_obj1, utc_str_date_obj2):
    a = datetime.datetime.strptime(utc_str_date_obj1, "%Y%m%dT%H%M%S")
    b = datetime.datetime.strptime(utc_str_date_obj2, "%Y%m%dT%H%M%S")
    return b-a

def date_str_difference(str_date_1, date_format_1, str_date_2, date_format_2):
    a = datetime.datetime.strptime(str_date_1, date_format_1)
    b = datetime.datetime.strptime(str_date_2, date_format_2)
    return date_obj_1-date_obj_2

def date_range_list(start_date_obj, end_date_obj):
    n = (end_date_obj-start_date_obj).days+1
    return [(start_date_obj + datetime.timedelta(days=x)).strftime("%Y%m%d") for x in range(0, n)]

if __name__ == "__main__":
    print '\n** Convert string date time to date time object directly as integers **'
    do = datetime.datetime(2018, 10 , 12, 02, 30, 19)
    print do

    print '\n** Convert string date to date object using split and int **'
    d = '2018-10-12'
    ds = d.split('-')
    do = datetime.datetime(int(ds[0]), int(ds[1]), int(ds[2]))
    print do

    print '\n** Convert string date to date object without int and split **'
    d = '2018-10-12'
    do = datetime.datetime.strptime(d, "%Y-%m-%d")
    print do
    d = '20181012'
    do = datetime.datetime.strptime(d, "%Y%m%d")
    print do
    d = '2018-10-12 02:30:19'
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do

    print '\n** test if date is valid using try & except **'
    d = '2018-10-33'
    ds = d.split('-')
    try:
        do = datetime.datetime(int(ds[0]), int(ds[1]), int(ds[2]))
    except ValueError:
        print 'Ho no the date {} is wrong'.format(d)

    print '\n** Make a UTC date object from a date string **'
    d = '2018-10-12 02:30:19'
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do
    do_utc = do.replace(tzinfo=pytz.timezone('UTC'))
    print do_utc
    '''NOTE: datetime.replace() does not handle daylight savings time correctly. The correct way is to use timezone.localize() instead. Using datetime.replace() is OK when working with UTC as shown above because it does not have daylight savings time transitions to deal with.'''

    print '\n** Make another timezone date object from a date string **'
    d = '2018-10-12 02:30:19'
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do
    do_us = do.replace(tzinfo=pytz.timezone('Europe/London'))
    print '{} [This Does not have daylight savings]'.format(do_us)

    print '\n** Make any other timezone date object from a date string using localize for correct daylight saving time **'
    d = '2018-10-12 02:30:19'
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do
    do_us = pytz.timezone('Europe/London').localize(do)
    print do_us

    print '\n** Convert time of one timezone to another from time string **'
    d = '2018-10-17 02:20:00' #UTC in string
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do
    str_old_zone = 'UTC'
    str_new_zone = 'Asia/Hong_Kong'
    old_timezone = pytz.timezone(str_old_zone)
    new_timezone = pytz.timezone(str_new_zone)

    new_datetime = old_timezone.localize(do).astimezone(new_timezone)
    print '{} {}'.format(new_datetime, str_new_zone)

    one_more_zone = pytz.timezone('Europe/London')
    new_datetime = old_timezone.localize(do).astimezone(one_more_zone)
    print '{} {}'.format(new_datetime, one_more_zone)

    print '\n** Add/subtract days to a date **'
    d = '2018-10-12 02:30:19'
    do = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    print do
    mdays = 10
    future_date = do+datetime.timedelta(days=mdays)
    print '{} {} days ahead'.format(future_date, mdays)

    mdays = -60
    past_date = do+datetime.timedelta(days=mdays)
    print '{} {} days behind'.format(past_date, mdays)

    print '\n** Number of days between to dates **'
    d1 = '2018-10-12 02:30:19'
    d1o = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = '2018-07-18 02:30:19'
    d2o = datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
    delta = d1o - d2o
    print 'Number of days between {} and {} is {} days.'.format(d1o, d2o,delta.days)

    print '\n** differenct between two times **'
    a = datetime.datetime(2018, 8, 12, 12, 0, 10)
    b = datetime.datetime(2018, 8, 12, 12, 4, 33)
    print b-a

    print '\n** Create Range of dates **'
    a = datetime.datetime(2018, 8, 12)
    b = datetime.datetime(2018, 8, 15)
    n = (b-a).days+1
    date_list = [(a + datetime.timedelta(days=x)).strftime("%Y%m%d") for x in range(0, n)]
    print date_list
