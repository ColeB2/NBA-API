from ui_functions import Widget
from tabulate import tabulate
import calendar

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbaschedule import Schedule



class ScheduleUI(Widget):
    """A class to represent an NBA schedule.

    Attributes:
        schedule_headers: display headers for schedule UI

    """
    def __init__(self, season=None, team=None):
        self.S = Schedule(season, team)


    def display(self, game_num=None):
        '''FIX HARD CODING'''
        """Prints the schedule of selected team to the console.

        Args:
            game_num: number of games wanting to display, default = All
        """
        if not game_num: game_num = len(self.S.regular_season)
        for game in enumerate(self.S.regular_season):
            if game[0] >= game_num:
                break
            print(calendar.month_abbr[int(game[1]['startDateEastern'][4:6])], end=' ')
            print(game[1]['startDateEastern'][6:], end=' ')
            print(game[1]['startDateEastern'][:4],end= ' ')

            print(game[1]['gameUrlCode'][9:12],end= ' ')
            print(game[1]['vTeam']['score'], end= ' ')
            print(game[1]['gameUrlCode'][12:],end= ' ')
            print(game[1]['hTeam']['score'])


if __name__ == '__main__':
    S = ScheduleUI()
    S.display()
    pass
