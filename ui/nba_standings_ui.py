from ui_functions import Widget

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbastandings import Standings
from nbateam import TeamInfo


class StandingsUI(Widget):
    """A class to represent nba divisional standings

    Attributes:

    """
    def __init__(self, division=None, conference=None, div_stand=False,
                team_info_obj=None):

        if team_info_obj:
            self.TI = team_info_obj
        else:
            self.TI = TeamInfo()

        self.S = Standings(div_stand=div_stand, division=division,
                conference=conference, team_info_obj=self.TI)
        self.DS = None

        self.standing_headers = [
        'Team','W','L','PCT','GB','HOME','AWAY', 'DIV',
        'CONF','L10','STRK'
        ]
        self.games_back = 'divGamesBehind' if div_stand else 'gamesBehind'


    def display(self, conference=None, division=None):
        if not conference and not division:
            self.games_back = 'gamesBehind'
            self.standing_data = self.S.get_standing_data()
        elif conference and not division:
            self.games_back = 'gamesBehind'
            self.standing_data = self.S.conference[conference]
        elif division and conference:
            self.games_back = 'divGamesBehind'
            if not self.DS:
                self.DS = Standings(div_stand=True, division=division,
                    conference=conference)
                self.standing_data = self.DS.get_standing_data()
            else:
                self.standing_data = self.DS.conference[conference][division]

        self.create_standing_data_keys()
        if division:
            self.horizontal_display(self.DS, header=True)
        else:
            self.horizontal_display(self.S, header=True)

    def create_standing_data_keys(self):
        self.standing_data_keys = [
        'teamId','win','loss','winPct',self.games_back,('homeWin', 'homeLoss'),
        ('awayWin','awayLoss'), ('divWin', 'divLoss'), ('confWin','confLoss'),
        ('lastTenWin','lastTenLoss'),('isWinStreak', 'streak')
        ]


    def create_nested_list(self, data):
        nested_list = []
        """Stats Header"""
        nested_list.append(self.standing_headers)

        """Information"""
        for team in self.standing_data:
            team_list = []
            for item in self.standing_data_keys:
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
    DS = StandingsUI(div_stand=True)
    DS.display()

    CS = StandingsUI()
    CS.display()
