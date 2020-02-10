from ui_functions import Widget
from tabulate import tabulate
import calendar

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbascore import ScoreBoard
from functions import get_yesterday_date

'''
TODO: Fix Hardcoding, universal date formatter
'''

class ScoreBoardUI():
    """A class to represent an 'around the league' scoreboard for all teams.

    Attributes:
    """
    def __init__(self, date=None):
        self.SB = ScoreBoard()
        self.YSB = ScoreBoard(date=get_yesterday_date())


    def display(self, horiz=True):
        #tableY = self.set_horizontal_headers(self.YSB)
        tableT = self.set_horiz_headers(self.YSB, self.SB)
        self.format_date(tableT)
        print(tableT)
        #print(calendar.month_abbr[int(self.SB.date[4:6])], end=' ')
        #print(self.SB.date[6:] + ' ' + self.SB.date[:4])
    """HORIZONTAL DISPLAY"""
    def format_date(self, table):
        """Formats date string to fit the CLI of scoreboard"""
        date = calendar.month_abbr[int(self.YSB.date[4:6])]
        date = date + ' ' + self.YSB.date[6:] + ' ' + self.YSB.date[:4]
        #print(len(tabulate(table)))
        x = table.find('***')
        #print(x)
        y = table.find('\n')
        #print(y)
        while len(date) <= x-y+2:
            date = date + ' '
        date = date + calendar.month_abbr[int(self.SB.date[4:6])]
        date = date + ' ' + self.SB.date[6:] + ' ' + self.SB.date[:4]
        print(date)

    def set_horiz_headers(self, *data):
        top_team, bot_team = [], []
        for idx in range(len(data)):
            for game in data[idx].games:
                home = str(game['hTeam']['triCode'] + ' ' + game['hTeam']['score'])
                away = str(game['vTeam']['triCode'] + ' ' + game['vTeam']['score'])
                top_team.append(home)
                bot_team.append(away)

            if len(data) >= 2 and idx < len(data)-1:
                top_team.append('***')
                bot_team.append('***')

        table = []
        table.append(top_team)
        table.append(bot_team)
        return tabulate(table, tablefmt='psql')



    def horizontal_display(self):
        print(tabulate(table, tablefmt='psql'))

    """VERTICAL DISPLAY"""
    def vertical_display(self, today=True, yesterday=False):
        for game in self.SB.games:
            print(game['hTeam']['triCode'],game['hTeam']['score'], end=' ')
            print(game['vTeam']['triCode'], game['vTeam']['score'])

    def create_horiz_table(self):
        vTeam_headers = []
        hTeam_headers = []



if __name__ == '__main__':
    SB = ScoreBoardUI()
    SB.display()
