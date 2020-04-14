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
        self.CS = Standings(div_stand='conference')
        self.DS = Standings(div_stand='division')

    def test_conference_data(self):
        """Tests to assure conference east and west data is correct. Does so by
            testing to see that Division standings is a dictionary of div names,
            and that conference standings is a list of teams."""
        self.assertEqual(type(self.CS.east), list)
        self.assertEqual(type(self.CS.west), list)
        east_div = ['southeast', 'atlantic', 'central']
        for div in east_div:
            self.assertIn(div, self.DS.east.keys())
        west_div = ['southwest', 'pacific', 'northwest']
        for div in west_div:
            self.assertIn(div, self.DS.west.keys())


    def test_get_standing_data(self):
        info = self.CS.get_standing_data()
        print(f"conf{self.CS.conf} div{self.CS.div}")
        print(f"info {info}")
        info2 = self.DS.get_standing_data()
        print(f"info2 {info2}")


    def test__get_conf_division(self):
        info = self.CS._get_conf_division(team='raptors')
        info2 = self.DS._get_conf_division(team='blazers')
        self.assertEqual(info, ('East','Atlantic'))
        self.assertEqual(info2, ('West', 'Northwest'))

if __name__ == '__main__':
    unittest.main()
