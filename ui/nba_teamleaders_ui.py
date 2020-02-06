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

    def set_horizontal_headers(self):
        headers = self.headers.copy()
        for i in enumerate(self.headers):
            idx = self.data_headers[i[0]]
            headers[i[0]] += ': ' + str(self.TL.leaders[idx][0]['value'])
        return headers

    def create_table(self, headers, horiz=True):
        if horiz: headers = self.set_horizontal_headers()
        table = list()
        table.append(headers)
        leaders = []
        for player in self.TL.leaders.values():
            first, last = (self.PI.get_player_name(player[0]['personId']))
            name_str = str(first) + ' ' + str(last)
            leaders.append(name_str)
        table.append(leaders)
        return table

if __name__ == '__main__':
    TL = TeamLeadersUI()
    #TL.create_table()
    print(tabulate(TL.create_table(TL.headers), tablefmt='psql' ))
