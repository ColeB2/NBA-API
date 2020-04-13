import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbascore import get_score_data, ScoreBoard

class TestScoreBoard(unittest.TestCase):

    def test_get_score_data(self):
        data = get_score_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        self.SB = ScoreBoard(date="20181212")

    def test_scoreboard_date(self):
        """Tests to assure date sets correctly when creating a scoreboard"""
        self.assertEqual(self.SB.date, '20181212')

    def test_number_of_games(self):
        """Tests to assure num games attribute contains correct value of 11"""
        self.assertEqual(self.SB.num_games, 11)

    def test_games(self):
        """Tests to assure the games extracts properly and is all their. Does
            so by assuring the last game of the day was TOR @ GSW"""
        self.assertEqual(len(self.SB.games), 11)
        self.assertEqual(self.SB.games[10]['vTeam']['triCode'], 'TOR')
        self.assertEqual(self.SB.games[10]['hTeam']['triCode'], 'GSW')


if __name__ == '__main__':
    unittest.main()
