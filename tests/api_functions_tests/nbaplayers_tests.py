import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbaplayers import get_player_data, PlayerInfo

class TestPlayerInfo(unittest.TestCase):

    def test_get_player_data(self):
        data = get_player_data()
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    def test_create_PI_non_default_season(self):
        """Tests the ability to create a PlayerInfo object with non default
            season setting. Does so using first season in record 2012, and by
            checking that right information exists, and first player on record
            is 'Quincy'
            Works from 2012 to present."""
        season = '2012'
        self.PI = PlayerInfo(season=season)
        first_player = self.PI.standard[0]['firstName']
        self.assertEqual(self.PI.season, season)
        self.assertIsNotNone(self.PI.standard)
        self.assertEqual(first_player, 'Quincy')

    @classmethod
    def setUpClass(self):
        """Sets up the expensive procedure of creating the Player info Object"""
        self.PI = PlayerInfo()

    def test_PI_data(self):
        """Tests the PI object has data in its standard attribute"""
        self.assertIsNotNone(self.PI.standard)

    def test_PI_standard_dict(self):
        """Tests the keys of standard attribute and that 'firstName' exists"""
        PI_player_dict = self.PI.standard[0]
        self.assertIsNotNone(PI_player_dict, 'firstName')

    def test_get_player_name(self):
        """Tests get_player_name method and assures it works by getting
            Pascal Siakam from the PI object using his player ID"""
        pascal_siakam = self.PI.get_player_name('1627783')
        self.assertEqual(pascal_siakam, ('Pascal', 'Siakam'))

if __name__ == "__main__":
    unittest.main()
