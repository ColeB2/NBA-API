import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbagameboxscore import get_boxscore_data, BoxScore

class TestBoxScore(unittest.TestCase):

    def test_get_boxscore_data(self):
        data = get_boxscore_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        self.BS = BoxScore(date='20200117')

    def test_boxscore_date(self):
        """Tests to assure date sets correctly when creating boxscore"""
        self.assertEqual(self.BS.date, '20200117')

    def test_boxscore_scores(self):
        """Test to assure totals returns proper values, does so by checking the
            values for the home/visiting teams points."""
        test_hteam_totals = self.BS.hTeam_totals['points']
        answer_hteam_totals = '140'
        test_vteam_totals = self.BS.vTeam_totals['points']
        answer_vteam_totals = '111'

        self.assertEqual(test_hteam_totals, answer_hteam_totals)
        self.assertEqual(test_vteam_totals, answer_vteam_totals)

    def test_boxscore_prev_matchup(self):
        """Tests to assure previous_matchup returns proper gameId and date.
            Does so for the Raptors game vs Washington Wizards 20200117."""
        prev_matchup = {'gameId': '0021900423', 'gameDate': '20191220'}
        self.assertEqual(self.BS.previous_matchup, (prev_matchup))

    def test_boxscore_player_stats(self):
        """Test to assure player_stats returns containts the proper values.Does
             so by testing the 'firstName' value for both home and away teams"""
        test_v_player_stat = self.BS.vTeam_player_stats[0]['firstName']
        test_answer_v = 'Isaac'
        test_h_player_stat = self.BS.hTeam_player_stats[0]['firstName']
        test_answer_h = 'Pascal'
        self.assertEqual(test_v_player_stat, test_answer_v)
        self.assertEqual(test_h_player_stat, test_answer_h)

if __name__ == '__main__':
    unittest.main()
