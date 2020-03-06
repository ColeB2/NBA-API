from ui_functions import Widget

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbastandings import Standings
from nbateam import TeamInfo

class StandingsUI(Widget):
    """A class to represent nba divisional standings

    Attributes:

    """
    def __init__(self, division=False, conference=False, div=None, conf=None):
        self.S = Standings(division=division, conference=conference)
        self.standing_data = self.S.get_standing_data()
        self.TI = TeamInfo()

        self.div_headers = [
        'Team','W','L','PCT','GB','HOME','AWAY', 'DIV',
        'CONF','L10','STRK'
        ]

        if division: self.games_back = 'divGamesBehind'
        if conference: self.games_back = 'gamesBehind'

        self.div_data = [
        'teamId','win','loss','winPct',self.games_back,('homeWin', 'homeLoss'),
        ('awayWin','awayLoss'), ('divWin', 'divLoss'), ('confWin','confLoss'),
        ('lastTenWin','lastTenLoss'),('isWinStreak', 'streak')
        ]



    def display(self, horiz=True):
        self.horizontal_display(self.S, header=True)


    def create_nested_list(self, data):
        nested_list = []

        """Stats Header"""
        nested_list.append(self.div_headers)

        """Information"""
        for team in self.standing_data:
            team_list = []
            for item in self.div_data:
                if item == 'teamId':
                    team_list.append(
                        self.TI.get_team(team[item], item, 'nickname'))
                elif type(item) is tuple:
                    if item[0] == 'isWinStreak':
                        if team[item[0]] == True:
                            team_list.append(f"W{team[item[1]]}")
                        else:
                            team_list.append(f"L{team[item[1]]}")
                    else:
                        team_list.append(f"{team[item[0]]}-{team[item[1]]}")
                else:
                    team_list.append(f"{team[item]}")

            nested_list.append(team_list)
        return nested_list

    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)



if __name__ == '__main__':
    DS = StandingsUI(division=True)
    DS.display()

    CS = StandingsUI(conference=True)
    CS.display()
