import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'ui')))

from ui_functions import Widget\


class TestWidgetsClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self. W = Widget()

    def test_create_tabulate_table(self):
        data = [[1,2,3], [4,5,6]]
        table = self.W.create_tabulate_table(data, header=False)
        exp_table = '+---+---+---+\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n+---+---+---+'
        self.assertEqual(table, exp_table)

    def test_convert_time(self):
        utc_time = '2020-04-20T16:30:00.00Z'
        #utc_time = '2020-04-20'
        new_time = self.W.convert_time(utc_time)
        exp_time = f"11:30 AM"
        self.assertEqual(new_time, exp_time)


if __name__ == '__main__':
    unittest.main()
