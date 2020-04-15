import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbateam import get_team_data, TeamInfo

class TestTeamInfo(unittest.TestCase):

    def test_get_team_data(self):
        data = get_team_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

if __name__ == '__main__':
    unittest.main()
