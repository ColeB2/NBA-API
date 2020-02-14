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

class ScoreBoardUI(Widget):
    """A class to represent an 'around the league' scoreboard for all teams.

    Attributes:
    """
    def __init__(self, date=None):
        self.date = date

        self.SB = ScoreBoard()
        self.YSB = ScoreBoard(date=get_yesterday_date())


    def display(self, horiz=True):
        """Prints the scoreboard of games for today, and yesterday to the
        console

        Args:
            horiz: boolean on whether to display scoreboard horizontally if
            false, will display it vertically.

        """
        if horiz:
            self.horizontal_display(self.horizontal_display_date)
        else:
            self.vertical_display()



    """HORIZONTAL DISPLAY METHODS"""
    def format_date_spacing(self,date, games):
        """formats the date from YYYYMMDD format into MMM DD YYYY format

        Args:
            date: date of game in YYYYMMDD format

        Returns:
            string, formatted in abbreviated, MMM DD YYYY format
        """
        for i in range(len(games)):
            date = date + 9*' '
        date += '  '
        return date


    def horizontal_display_date(self):
        """Calls the methods needed to format the date string before being
        displayed above the league wide scoreboard"""
        date_str = self.format_date(self.YSB.date)
        date_str = self.format_date_spacing(date_str, self.YSB.games)
        date_str += self.format_date(self.SB.date)
        print(date_str)

    def set_horiz_headers(self, *data):
        """Sets the heads for a horizontal display so they can be used by the
        tabulate function.

        Args:

        Kwargs
            data: Raw scoreboard data created from the ScoreBoard class. Can be
            both just for todays date scores, and yesterdays scores.

        Returns:
            list of lists, which contains game status, and home/away info.
        """
        info = []
        top_team = []
        bot_team = []
        for idx in range(len(data)):
            for game in data[idx].games:
                home = str(game['hTeam']['triCode'] + ' ' + game['hTeam']['score'])
                away = str(game['vTeam']['triCode'] + ' ' + game['vTeam']['score'])
                top_team.append(home)
                bot_team.append(away)


                '''game status'''
                status = self.get_status(game)
                info.append(status)

        return [info, top_team, bot_team]

    def period_suffix(self, period):
        """Sets the suffix given the game period.

        Args:
            period: int, based on which period the game is in.

        Returns:
            string of the suffix that corresponds to the period.
        """
        period_suffix = ['st', 'nd', 'rd', 'th']
        return period_suffix[int(period) - 1]

    def get_status(self, game_data):
        """Gets the status of the games progress.

        Args:
            game_data: dict, filled with needed data for game.

        Returns:
            string, which represents the current status of the game.
        """
        ##score == ' or '0' as sometimes it sets score to 0 before game starts.
        status_str = str()
        if game_data['isGameActivated'] == False:
            if game_data['hTeam']['score'] == '' or \
               game_data['hTeam']['score'] == '0':
                status_str = self.convert_time(game_data['startTimeUTC'])
            else:
                status_str = 'FINAL'
        else:
            period = game_data['period']['current']
            if game_data['period']['isEndOfPeriod']:
                if game_data['period']['isHalftime']:
                    status_str = 'HalfTime'
                else:
                    status_str = 'End of ' + str(period) + \
                        self.period_suffix(period)
            else:
                status_str = str(game_data['clock']) + \
                    ' - ' + str(period) + self.period_suffix(period)

        return status_str

    def get_headers(self):
        """Sets up proper parameters to pass on to set_horiz_headers method,
        which creates the headers, so this method can return them."""
        headers = self.set_horiz_headers(self.YSB, self.SB)
        return headers

    def horizontal_displayX(self):
        x = super().horizontal_display()
        print(x)



    """VERTICAL DISPLAY METHODS"""
    def vertical_display(self, today=True, yesterday=False):
        for game in self.SB.games:
            print(game['hTeam']['triCode'],game['hTeam']['score'], end=' ')
            print(game['vTeam']['triCode'], game['vTeam']['score'])





if __name__ == '__main__':
    SB = ScoreBoardUI()
    SB.display()
