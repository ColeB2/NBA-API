import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))

from nbateamleaders import get_team_leaders_data, TeamLeaders

class TestTeamLeaders(unittest.TestCase):

    def test_get_team_leaders_data(self):
        data = get_team_leaders_data(team='bucks', season='2019')
        self.assertIsNotNone(data)
        self.assertIn("_internal", data.keys())

    @classmethod
    def setUpClass(self):
        """Object set up to prevent from having to create mutiple calls to NBA
            data website to use same data over and over again. Does so for the
            blazers during the 2015 seasons(appears to be earlier info have on
            hand.)"""
        self.TL = TeamLeaders(team='blazers', season='2015')

    def test_object_input(self):
        """Tests to assure the input values are correct for obj instantiation"""
        self.assertEqual(self.TL.team, 'blazers')
        self.assertEqual(self.TL.season, '2015')

    def test_leaders_attribute(self):
        """Tests to assure correct values were pulled from NBA website"""
        pts_leader = self.TL.leaders['ppg']['value']
        exp_pts_value = '26.5'
        reb_leader = self.TL.leaders['trpg']['value']
        exp_reb_value = '11.8'
        self.assertEqual(pts_leader, exp_pts_value)
        self.assertEqual(reb_leader, exp_reb_value)

    def test_create_dictionary(self):
        """Tests to assure create_dictionary method creates a dictionary
            correctly using the proper paramters"""
        new_dic = self.TL.create_dictionary(self.TL.standard, self.TL.MAIN_FIVE_STATS)
        for key in self.TL.MAIN_FIVE_STATS:
            self.assertIn(key, new_dic.keys())



if __name__ == '__main__':
    unittest.main()
