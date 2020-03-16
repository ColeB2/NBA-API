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
    def create_tabulate_table(self, data, header=None):
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


    def horizontal_display(self, data, *extra, extra_args=None, header=False):
        """Calls appropriate methods to create appropiate table to display
        horiontally across the CLI.

        Kwargs:
            *extra: funcions that can be called before the table gets printed
                tuple format, with func in first position(0) and rest of of
                items as args to the func
        """
        nested_list = self.get_nested_list(data)
        table = self.create_tabulate_table(nested_list, header)
        if extra:
            for func in extra:
                if extra_args:
                    func(extra_args)
                else:
                    func()
        print(table)


    def create_nested_list(self):
        """Abstract Method to be created
        Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.
        """
        print('Implement create_nested_list method')
        pass


    def get_nested_list(self):
        """Abstract Method to be created
        Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        print('Implement get_nested_list method')
        pass


    """VERTICAL DISPLAY METHODS"""
    """UTILITY METHODS"""
    def convert_time(self, utc_time):
        """converts UTC timezone string to local time zone string.
        """
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        try:
            utc_time = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')
            utc_time= utc_time.replace(tzinfo=from_zone)
            local_time = utc_time.astimezone(to_zone)
            local_time = local_time.strftime('%I:%M %p')

            ##Except handles when given a date, but no time. 2020 suspension
        except:
            utc_time = datetime.strptime(utc_time, '%Y-%m-%d')
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
