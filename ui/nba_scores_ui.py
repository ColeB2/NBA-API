from ui_functions import Widget
import calendar
from colorama import Fore, Back, Style

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbascore import ScoreBoard
from functions import get_date_before



class ScoreBoardUI(Widget):
    """A class to represent an 'around the league' scoreboard for all teams.

    Attributes:
         date: date in YYYYMMDD format for which day to get scores of.
         SB: Scoreboard object, to display the days scores.
         YSB: Scoreboard object, for the day before SBs, to show scores multiple
         days.
    """
    def __init__(self, date=None):
        self.date = date

        self.SB = ScoreBoard(date=date)
        self.YSB = ScoreBoard(date=get_date_before(date))



    def display(self, horiz=True):
        """Prints the scoreboard of games for today, and yesterday to the
        console

        Args:
            horiz: boolean on whether to display scoreboard horizontally if
            false, will display it vertically.

        """
        if horiz:
            self.horizontal_display((self.YSB, self.SB),
                                     self.horizontal_display_date,
                                     extra_args=(self.YSB, self.SB))
        else:
            self.vertical_display()



    """HORIZONTAL DISPLAY METHODS"""
    def create_nested_list(self, data):
        """Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.

        Args:

        Kwargs
            data: Raw scoreboard data created from the ScoreBoard class. Can be
            both just for todays date scores, and yesterdays scores.

        Returns:
            lList of lists, info, top_team, bot_team.
            info: status of game, whether it is over, @ half, or time during
                play.
            top_team: Home team triCode and score,
            bot_team: Away team triCode and score.
        """
        info = []
        top_team = []
        bot_team = []
        for idx in range(len(data)):
            for game in data[idx].games:
                COLOR = False
                if COLOR:
                    home, away = self.get_colored_score(game)
                else:
                    home = f"{game['hTeam']['triCode']} " \
                           f"{game['hTeam']['score'].rjust(3)}"

                    away = f"{game['vTeam']['triCode']} " \
                           f"{game['vTeam']['score'].rjust(3)}"

                top_team.append(home)
                bot_team.append(away)


                '''game status'''
                status = self.get_status(game)
                info.append(status)

        return [info, top_team, bot_team]

    def get_colored_score(self, game_data):
        hScore = game_data['hTeam']['score']
        vScore = game_data['vTeam']['score']

        hcol = ''
        vcol = ''

        if hScore != '' and vScore != '':
            if int(hScore) > int(vScore):
                hcol = Back.RED

            elif int(vScore) > int(hScore):
                vcol= Back.RED

        home = f"{game_data['hTeam']['triCode']} " \
               f"{hcol}{hScore}{Style.RESET_ALL}"

        away = f"{game_data['vTeam']['triCode']} " \
               f"{vcol}{vScore.rjust(3)}{Style.RESET_ALL}"

        return home, away

    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)


    def horizontal_display_date(self, data):
        """Calls the methods needed to format the date string before being
        displayed above the league wide scoreboard"""
        date_str = ''
        for idx in range(len(data)):

            if data[idx].num_games >=1:
                date_str += self.format_date(data[idx].date)
            date_str = self.format_date_spacing(date_str, data[idx].games)
        print(date_str)


    def format_date_spacing(self,date, games):
        """formats the date from YYYYMMDD format into MMM DD YYYY format

        Args:
            date: date of game in YYYYMMDD format

        Returns:
            string, formatted in abbreviated, MMM DD YYYY format
        """
        if len(date) != 0:
            date = f"{date}  "
        for i in range(len(games)-1):
            space = 10*' '
            date = f"{date}{space}"
        return date


    def get_status(self, game_data):
        """Gets the status of the games progress.

        Args:
            game_data: dict, filled with needed data for game.

        Returns:
            string, which represents the current status of the game.
        """
        status_str = str()
        if game_data['isGameActivated'] == False:
            if game_data['homeStartTime'] == '':
                status_str = '~~TBD~~'
            elif game_data['hTeam']['score'] == '' or \
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
                    status_str = f"End of {period}{self.period_suffix(period)}"
            else:
                status_str = f"{game_data['clock']} - " \
                             f"{period}{self.period_suffix(period)}"

        return status_str


    def period_suffix(self, period):
        """Sets the suffix given the game period.

        Args:
            period: int, based on which period the game is in.

        Returns:
            string of the suffix that corresponds to the period.
        """
        period_suffix = ['st', 'nd', 'rd', 'th']
        return period_suffix[int(period) - 1]


    """VERTICAL DISPLAY METHODS"""
    def vertical_display(self, today=True, yesterday=True):
        if yesterday:
            print(f"{self.format_date(self.YSB.date)}")
            for game in self.YSB.games:
                print( f"{self.get_status(game)} "
                       f"{game['hTeam']['triCode']} "
                       f"{game['hTeam']['score'].rjust(3)} "
                       f"{game['vTeam']['triCode']} "
                       f"{game['vTeam']['score'].rjust(3)}" )
        if today:
            print(f"{self.format_date(self.SB.date)}")
            for game in self.SB.games:
                print( f"{game['hTeam']['triCode']} " \
                       f"{game['hTeam']['score'].rjust(3)} " \
                       f"{game['vTeam']['triCode']} " \
                       f"{game['vTeam']['score'].rjust(3)}" )



if __name__ == '__main__':
    SB = ScoreBoardUI(date='20200107')
    SB.display()

    SB = ScoreBoardUI(date='20200210')
    SB.display(horiz=True)

    SB = ScoreBoardUI()
    SB.display(horiz=True)

    print('Vertical Display:')
    SB = ScoreBoardUI()
    SB.display(horiz=False)
