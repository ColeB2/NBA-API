import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbateam import get_team_data, TeamInfo

class TestTeamInfo(unittest.TestCase):

    def test_get_team_data(self):
        data = get_team_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        self.TI = TeamInfo()

    def test_get_conf_division_east(self):
        res = self.TI.get_conf_division(team='SiXeRs')
        self.assertEqual(res, ('East','Atlantic'))
        res = self.TI.get_conf_division(team='cavaliers')
        self.assertEqual(res, ('East','Central'))
        res = self.TI.get_conf_division(team='hornets')
        self.assertEqual(res, ('East','Southeast'))

    def test_get_conf_division_west(self):
        res = self.TI.get_conf_division(team='Warriors')
        self.assertEqual(res, ('West','Pacific'))
        res = self.TI.get_conf_division(team='pelIcANS')
        self.assertEqual(res, ('West','Southwest'))
        res = self.TI.get_conf_division(team='blazers')
        self.assertEqual(res, ('West','Northwest'))

    def test_create_nba_list(self):
        res = self.TI.create_nba_list()
        for team in res:
            self.assertEqual(len(team), 3)

    def test_create_nba_list_2(self):
        """Tests to assure all 30 NBA teams(labeled by tri code) and in the
            teaminfo object list to assure the create_nba_list function is
            working correctly"""
        nba_teams = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN',
            'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL',
            'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC',
            'SAS', 'TOR', 'UTA', 'WAS']

        for team in nba_teams:
            self.assertIn(team, self.TI.teamsTRI)



if __name__ == '__main__':
    unittest.main()
