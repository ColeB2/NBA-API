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
        """Tests get_fonf_division method to assure return values are proper.
            Does so by testing various teams of various divisions in Eastern
            conference."""
        res = self.TI.get_conf_division(team='SiXeRs')
        self.assertEqual(res, ('East','Atlantic'))
        res = self.TI.get_conf_division(team='cavaliers')
        self.assertEqual(res, ('East','Central'))
        res = self.TI.get_conf_division(team='hornets')
        self.assertEqual(res, ('East','Southeast'))

    def test_get_conf_division_west(self):
        """Tests get_fonf_division method to assure return values are proper.
            Does so by testing various teams of various divisions in Western
            conference."""
        res = self.TI.get_conf_division(team='Warriors')
        self.assertEqual(res, ('West','Pacific'))
        res = self.TI.get_conf_division(team='pelIcANS')
        self.assertEqual(res, ('West','Southwest'))
        res = self.TI.get_conf_division(team='blazers')
        self.assertEqual(res, ('West','Northwest'))

    def test_get_team_city(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='Toronto', id_option='city', id_return='urlName')
        exp = 'raptors'
        self.assertEqual(res, exp)

    def test_get_team_urlName(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='warriors', id_option='urlName', id_return='city')
        exp = 'Golden State'
        self.assertEqual(res, exp)

    def test_get_team_triCode(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='POR', id_option='triCode', id_return='city')
        exp = 'Portland'
        self.assertEqual(res, exp)

    def test_get_team_fullName(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='LA Clippers', id_option='fullname', id_return='city')
        exp = 'LA'
        self.assertEqual(res, exp)

    def test_get_team_teamId(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='1610612749', id_option='teamId', id_return='nickname')
        exp = 'Bucks'
        self.assertEqual(res, exp)

    def test_get_team_nickname(self):
        """Tests the get_team function, specifically the id_option/id_return
        paramters to assure that they return and fetch by the corect value."""
        res = self.TI.get_team(identifier='Raptors', id_option='nickname', id_return='tricode')
        exp = 'TOR'
        self.assertEqual(res, exp)



    def test_create_nba_list(self):
        """Tests to assure create_nba_list functions returns a list of of
            strings all with len of 3 characters long."""
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
