import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbaschedule import get_schedule_data, Schedule

class TestSchedule(unittest.TestCase):

    def test_get_schedule_data(self):
        data = get_schedule_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        self.S = Schedule(season='2018', team='raptors')

    def test_correct_season(self):
        self.assertEqual(self.S.season,'2018')

    def test_correct_team(self):
        self.assertEqual(self.S.team, 'raptors')

    def test_proper_data(self):
        self.assertIsNotNone(self.S.standard)

    def test_last_game_attributes(self):
        """Tests Schedule obj last_game attributes. Does so using seasonStageId,
            idx of last game(110, game 6 nba finals), and game id and date of
            final game of the season."""
        self.assertEqual(self.S.last_game['seasonStageId'], 4)
        self.assertEqual(self.S.last_game_idx, 110)
        self.assertEqual(self.S.last_game_id_date, ('0041800406', '20190613'))

    def test_get_gameId(self):
        """Tests get_gameId method for Schedule object"""
        pass

if __name__ == '__main__':
    unittest.main()
