'''
Skeleton class for widget, all ui elements will inherit from, has basic UI
functions used to format and print to command line
'''
from datetime import datetime
from dateutil import tz
from tabulate import tabulate
import calendar


class Widget():
    def __init__(self):
        pass


    """HORIZONTAL DISPLAY METHODS"""
    def create_horiz_table(self, data, header=None):
        """Creates the tabulate table given the headers from a classes
        set_horiz_headers.

        Args:
            data: Data froman objects set_horiz_headers methods

        Returns:
            tabulate object, which is a formatted string, to create a command
            line table.
        """
        table = []
        for headers in data:
            table.append(headers)
        if header:
            return tabulate(table, headers="firstrow", tablefmt='psql')
        else:
            return tabulate(table, tablefmt='psql')

    def set_horiz_headers(self):
        """Abstract Method to be created
        Used by get_headers, to create/set the headers needed for horizontal
        display"""
        print('Implement set_horiz_headers')
        pass

    def get_horiz_headers(self):
        """Abstract Method to be created
        Gets the values returnd from set_horiz_headers method to be passed onto
        create_horiz_table"""
        print('Implement get_horiz_headers')
        pass

    def horizontal_display(self, data, *extra, header=False):
        """Calls appropriate methods to create appropiate table to display
        horiontally across the CLI.

        Kwargs:
            *extra: funcions that can be called before the table gets printed.
        """
        headers = self.get_horiz_headers(data)
        table = self.create_horiz_table(headers, header)
        if extra:
            for func in extra:
                func()
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

    def format_date(self, date):
        """Formats date given in YYYYMMDD format into a MMM/DD/YY format

        Args:
            date: str, date given in YYYYMMDD format

        Returns:
            string, formatted in MMM/DD/YY format"""
        date_str = calendar.month_abbr[int(date[4:6])] + \
            '/' + date[6:] + '/' + date[2:4]
        return date_str






if __name__ == '__main__':
    time = '2020-02-13T02:00:00.000Z'
    W = Widget()
    print(W.convert_time(time))
    print(W.format_date(time))
