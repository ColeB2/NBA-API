import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbastandings import get_standings_data, Standings

class TestStandings(unittest.TestCase):

    def test_get_standing_data(self):
        data = get_standings_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        self.S = Standings(div_stand='True')

    def test_conference_data(self):
        print(self.S.east)
        print(self.S.west)

    def test_get_standing_data(self):
        info = self.S.get_standing_data()
        print(f"conf{self.S.conf} div{self.S.div}")
        print(f"info {info}")


    def test__get_conf_division(self):
        info = self.S._get_conf_division(team='raptors')
        info2 = self.S._get_conf_division(team='blazers')
        self.assertEqual(info, ('East','Atlantic'))
        self.assertEqual(info2, ('West', 'Northwest'))

if __name__ == '__main__':
    unittest.main()
