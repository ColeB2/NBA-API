'''
Skeleton class for widget, all ui elements will inherit from, has basic UI
functions used to format and print to command line
'''
from datetime import datetime
from dateutil import tz
from tabulate import tabulate


class Widget():
    def __init__(self):
        pass


    """HORIZONTAL DISPLAY METHODS"""
    def create_horiz_table(self, data):
        """Creates the tabulate table given the headers from set_horiz_headers.

        Args:
            data: Data from set_horiz_headers

        Returns:
            tabulate object, which is a formatted string, to create a command
            line table.
        """
        table = []
        for headers in data:
            table.append(headers)
        return tabulate(table, tablefmt='psql')

    def set_horiz_headers(self):
        """Abstract Method to be created"""
        pass

    def get_headers(self):
        """Abstract Method to be created"""
        pass

    def horizontal_display(self):
        headers = self.get_headers()
        table = self.create_horiz_table(headers)
        print(table)


    """VERTICAL DISPLAY METHODS"""


    """UTILITY METHODS"""
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
