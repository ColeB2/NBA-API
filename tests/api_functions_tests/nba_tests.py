import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbagameboxscore import get_boxscore_data, BoxScore

class TestBoxScore(unittest.TestCase):

    def test_get_boxscore_data(self):
        data = get_boxscore_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    def test_BoxScore_given_date(self):
        BS = BoxScore(date='20200117')
        self.assertEqual(BS.date, '20200117')

if __name__ == '__main__':
    unittest.main()
