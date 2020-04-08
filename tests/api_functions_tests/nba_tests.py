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
        self.assertEqual(self.BS.date, '20200117')

    def test_boxscore_scores(self):
        test_hteam_totals = self.BS.hTeam_totals['points']
        answer_hteam_totals = '140'
        test_vteam_totals = self.BS.vTeam_totals['points']
        answer_vteam_totals = '111'

        self.assertEqual(test_hteam_totals, answer_hteam_totals)
        self.assertEqual(test_vteam_totals, answer_vteam_totals)

    def test_boxscore_prev_matchup(self):
        """Tests previous matchup for Washing Wizards 20200117 returns the
        correct gameId and date."""
        prev_matchup = {'gameId': '0021900423', 'gameDate': '20191220'}
        self.assertEqual(self.BS.previous_matchup, (prev_matchup))

    def test_boxscore_player_stats(self):
        player_stat_test = self.BS.vTeam_player_stats[0]['firstName']
        test_answer = 'Isaac'
        self.assertEqual(player_stat_test, test_answer)


if __name__ == '__main__':
    unittest.main()
