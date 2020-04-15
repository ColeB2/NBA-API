import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbastandings import get_standings_data, Standings

class TestStandings(unittest.TestCase):

    def test_get_standings_data(self):
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
        info2 = self.DS.get_standing_data()

    def test_more_get_Standing_data(self):
        """Further testing to to test inputs of self.div and self.conf in
            Standing obj and out get_standing_data handles it. Does so by
            acquiring data 3 different ways, and testing correct team is in the
            diviion that is returned"""
        Stand1 = Standings(div_stand='division', division='Atlantic', conference='East')
        stand1 = None
        for team in Stand1.get_standing_data():
            if team['teamSitesOnly']['teamKey'] == 'Toronto':
                stand1 = team['teamSitesOnly']['teamKey']
        self.assertEqual('Toronto', stand1)
        Stand2 = Standings(div_stand='division', division='Pacific')
        stand2 = None
        for team in Stand2.get_standing_data():
            if team['teamSitesOnly']['teamKey'] == 'Los Angeles':
                stand2 = team['teamSitesOnly']['teamKey']
        self.assertEqual('Los Angeles', stand2)

        Stand3 = Standings(div_stand='division', division='Southwest', conference='West')
        stand3 = None
        for team in Stand3.get_standing_data():
            if team['teamSitesOnly']['teamKey'] == 'Houston':
                stand3 = team['teamSitesOnly']['teamKey']
        self.assertEqual('Houston', stand3)



    def test__get_conf_division(self):
        info = self.CS._get_conf_division(team='raptors')
        info2 = self.DS._get_conf_division(team='blazers')
        self.assertEqual(info, ('East','Atlantic'))
        self.assertEqual(info2, ('West', 'Northwest'))

if __name__ == '__main__':
    unittest.main()
