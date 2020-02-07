from ui_functions import Widget
from tabulate import tabulate

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbascore import ScoreBoard

class ScoreBoardUI():
    """A class to represent an 'around the league' scoreboard for all teams.

    Attributes:
    """
    def __init__(self, date=None):
        self.SB = ScoreBoard(date)


    def display(self):
        for game in self.SB.games:
            print(game['hTeam']['triCode'],game['hTeam']['score'], end=' ')
            print(game['vTeam']['triCode'], game['vTeam']['score'])

    def set_horizontal_headers(self):
        pass

    def create_table(self):
        vTeam_headers = []
        hTeam_headers = []



if __name__ == '__main__':
    SB = ScoreBoardUI()
    SB.display()
