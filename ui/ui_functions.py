'''
Skeleton class for widget, all ui elements will inherit from, has basic UI
functions used to format and print to command line
'''
from datetime import datetime
from dateutil import tz


class Widget():
    def __init__(self):
        pass


    def convert_time(self, utc_time):
        """converts UTC timezone string to local time zone string.
        """
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        utc_time = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        utc_time= utc_time.replace(tzinfo=from_zone)
        local_time = utc_time.astimezone(to_zone)
        local_time = local_time.strftime('%I:%M %p')

        return local_time



if __name__ == '__main__':
    time = '2020-02-13T02:00:00.000Z'
    W = Widget()
    W.convert_time(time)
