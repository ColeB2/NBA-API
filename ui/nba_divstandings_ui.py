from ui_functions import Widget

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbadivstandings import DivStandings
from nbateam import TeamInfo

class DivStandingsUI(Widget):
    """A class to represent nba divisional standings

    Attributes:

    """
    def __init__(self, division=None):
        self.DS = DivStandings(division=division)
        self.TI = TeamInfo()

        self.div_headers = [
        'Team','W','L','PCT','GB','HOME','AWAY', 'DIV',
        'CONF','STRK','L10'
        ]

        self.div_data = [
        'teamId','win','loss','winPct','divGamesBehind',('homeWin', 'homeLoss'),
        ('awayWin','awayLoss'), ('divWin', 'divLoss'), ('confWin','confLoss'),
        ('isWinStreak', 'streak'),('lastTenWin','lastTenLoss')
        ]



    def display(self, horiz=True):
        pass

    def create_nested_list(self, data):
        nested_list = []

        """Stats Header"""
        nested_list.append(self.div_headers)

    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)


    def basic_print(self):
        for team in self.DS.east_conf['atlantic']:
            for k, v in team.items():
                print(f"{k}:{v}", end=' ')
            print()
            #print(team)
        #print(self.DS)



if __name__ == '__main__':
    DS = DivStandingsUI()
    DS.display()
    DS.basic_print()
