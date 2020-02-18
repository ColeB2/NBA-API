from ui_functions import Widget
from tabulate import tabulate

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbateamleaders import TeamLeaders
from nbaplayers import PlayerInfo

class TeamLeadersUI(Widget):
    """A class to represent an NBA teams team leaders.

    Attributes:
        T: TeamLeaders object which holds all stats/methods for team leaders.
    """
    def __init__(self, team=None, season=None):
        self.TL = TeamLeaders(team, season)
        self.PI = PlayerInfo()
        self.headers = ['PTS/G', 'REB/G', 'AST/G', 'FG%',
            '3PT%', 'FT%', 'BLK/G','STL/G', 'TO/G',
            'PF/G']
        self.data_headers = ['ppg', 'trpg', 'apg', 'fgp', 'tpp', 'ftp', 'bpg',
        'spg', 'tpg', 'pfpg']

    def display(self, horiz=True):
        """Prints the team leaders of chosen team to the console.

        Args:
            horiz: Boolean, decides whether to print horizontal or not.
        """
        if horiz:
            self.horizontal_display()


    def set_horiz_headers(self, data):
        """Sets the headers for a horizontal display so they can be used by the
        tabulate function.

        Args:


        """
        headers = self.headers.copy()
        leaders = []
        headers = []

        for key, value in data.leaders.items():
            if key in self.data_headers:
                idx = self.data_headers.index(key)

                header = f"{self.headers[idx]}: {value['value']}"
                headers.append(header)

                first, last = self.PI.get_player_name(value['personId'])
                leader = f"{first} {last}"
                leaders.append(leader)

        return [headers, leaders]

    def get_horiz_headers(self):
        headers = self.set_horiz_headers(self.TL)
        return headers



if __name__ == '__main__':
    TL = TeamLeadersUI()
    TL.display()
