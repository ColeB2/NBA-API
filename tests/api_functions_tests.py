import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from functions import get_data, get_today_date, get_date_before,\
    get_season_year, get_team, handle_team_url_name, get_color, get_full_name

import datetime

import unittest

class TestApiFucntions(unittest.TestCase):
    """unit test to test funtions found in functions.py"""

    def test_get_data_function(self):
        """Tests the get_data funtion to assure it returns a dictionary of data,
        with one of the keys being the _internal key."""
        url = f"http://data.nba.net/10s/prod/v1/today.json"
        data = get_data(url)
        self.assertNotEqual(len(data.keys()), 0)
        self.assertIn("_internal", data.keys())

    def test_date_functions(self):
        """Tests the get_today_data and get_date_before functions to assure that
        the formatting(YYYYMMDD) is correct and that it grabs approrpriate date
        """
        today = get_today_date()
        yest = get_date_before(today)
        datetime_obj = str(datetime.date.today())
        year = datetime_obj[0:4]
        mon = datetime_obj[5:7]
        day = datetime_obj[8:]

        self.assertEqual(today[0:4], year)
        self.assertEqual(today[4:6], mon)
        self.assertEqual(today[6:], day)
        self.assertEqual(get_date_before("20120319"), "20120318")

    def test_get_team(self):
        """Tests get_team function to assert that it gets a team value"""
        print(get_team())



if __name__ == '__main__':
    unittest.main()
