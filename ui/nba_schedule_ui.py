from ui_functions import Widget
from tabulate import tabulate
import calendar

from datetime import datetime
from dateutil import tz

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbaschedule import Schedule



class ScheduleUI(Widget):
    """A class to represent an NBA schedule.

    Attributes:
        schedule_headers: display headers for schedule UI

    """
    def __init__(self, season=None, team=None, last=True,
        next=True, full=False):
        self.season = season
        self.team = team

        self.last = last
        self.next = next
        self.full = full

        self.S = Schedule(season, team)

        self.regular_season = self.S.standard[len(self.S.standard)-82:]
        self.offset = len(self.regular_season) - len(self.S.standard)
        self.last_game_idx = self.S.last_game_idx + self.offset


    def display(self, horiz=True, full=False, last=False, next=False):
        """Main display call, to display specified schedules.

        Args:
            horiz: Bool, To choose horizontal display
            last: Boolean, decides whether to display last x games.
            next: Boolean, decides whether to display next x games.
            full: Boolean, decides whether to display full schedule. Only uses
                vertical display
        """
        if horiz: self.horizontal_display()
        if not horiz:
            if last: self.display_last_x_games()
            if next: self.display_next_x_games()
        if full: self.display_season_schedule()

    def display_season_schedule(self):
        """Method used to display all regular season games to the console."""
        for game in enumerate(self.regular_season):
            self.display_game_information(game[0])
        print()



    """HORIZONTAL DISPLAY METHODS"""
    def get_home_listing(self, game_data):
        """Finds out if chosen team is home team or not then returns a
        corrospoding string, 'VS' or '@'

        Args:
            game_data: dict data for given game.

        Returns:
            boolean, True if home team, False otherwise.
        """
        vs_str = ''
        if game_data['isHomeTeam']:
            vs_str = 'VS'
        else:
            vs_str = '@'
        return vs_str

    def get_opponent(self, game_data, location=None):
        """Gets the opponent TRI code for given game.

        Args:
            game_data: dict daa for given game.
            location: str, 'VS' or '@' based on home/away team.

        Returns:
            Tri code for the oposing team.
        """
        tri_code = ''
        if location == 'VS':
            tri_code = game_data['gameUrlCode'][9:12]
        else:
            tri_code = game_data['gameUrlCode'][12:]
        return tri_code


    def get_result(self, game_data, location=None):
        """Gets the result of given game.

        Args:
            game_data: dict data for given game.
            location: str, VS or @ based on if team is home or away

        Returns:
            string, containing results of game. Ex: W 137-126
        """
        res, fave_score, opp_score = '', '', ''
        if location == 'VS':
            fave_score = game_data['hTeam']['score']
            opp_score = game_data['vTeam']['score']
        else:
            fave_score = game_data['vTeam']['score']
            opp_score = game_data['hTeam']['score']



        if fave_score != '' and int(fave_score) > int(opp_score):
            res = 'W'
        else:
            res = 'L'

        if fave_score == '' and opp_score == '':
            game_time = game_data['startTimeUTC']
            X = self.convert_time(game_time)
            res = str(X)

        dash = '-' if fave_score != '' else ''


        return res + ' ' + fave_score + dash + opp_score

    def get_date(self, game_data):
        date_str = calendar.month_abbr[int(
            game_data['startDateEastern'][4:6])] + '/' + \
            game_data['startDateEastern'][6:] + '/' +  \
            game_data['startDateEastern'][2:4]

        return date_str

    def set_horiz_headers(self, data):
        date = []
        vs_info= []
        result_info = []
        for game_idx in data:
            game = self.S.standard[game_idx]

            date_str = self.get_date(game)
            home_listing_str = self.get_home_listing(game)
            opponent_str = self.get_opponent(game, home_listing_str)
            vs_str   = home_listing_str + ' ' + opponent_str
            result_str = self.get_result(game, home_listing_str)

            date.append(date_str)
            vs_info.append(vs_str)
            result_info.append(result_str)

        return date, vs_info, result_info

    def get_headers(self):
        """Sets up proper parameters to pass on to set_horiz_headers method,
        which creates the headers, so this method can return them."""
        games = self.S.get_x_games()
        games.extend(self.S.get_x_games(x=6, next=False, prev_game=False))
        games.sort()
        headers = self.set_horiz_headers(games)
        return headers




    """VERTICAL DISPLAY METHODS
    TODO: refactor, and remove hard coding"""
    def display_game_information(self, game):
        """Method used to print approrpiate information to the console. Prints,
        date, team tricode and score.

        Args:
            game: index value of game to be printed
        """
        print(calendar.month_abbr[int( \
              self.regular_season[game]['startDateEastern'][4:6])], end='/')
        print(self.regular_season[game]['startDateEastern'][6:], end='/')
        print(self.regular_season[game]['startDateEastern'][2:4],end= ' ')

        print(self.regular_season[game]['gameUrlCode'][9:12],end= ' ')
        print(self.regular_season[game]['vTeam']['score'], end= ' ')
        print(self.regular_season[game]['gameUrlCode'][12:],end= ' ')
        print(self.regular_season[game]['hTeam']['score'])



    def _display_x_helper(self, x, next=True, prev_game=True):
        """Method used by display_last/next_x_games, sets direction of based on
        boolean value, and calls display_game_information to display games, if
        the order specified.
        Utilizes Schedule.get_x_games() to retrieve the information.

        Args:
            x: number of games to be displayed
            next: Boolean value, on whether to display next x games, vs last x
            games
            prev_game: Boolean value, whether to include previous game or not in
            search.
        """
        games = self.S.get_x_games(x=x, next=next,
            last_game=self.last_game_idx, prev_game=prev_game)
        for game in games:
            self.display_game_information(game)
        print()

    def display_last_x_games(self, x=5):
        """Method used to display last x number of games to the console. Does so
        by calling _display_x_helper.
        Args:
            x: number of games to be displayed.
        """
        self._display_x_helper(x, next=False, prev_game=True)

    def display_next_x_games(self, x=3):
        """Method used to display next x number of games to the console. Does so
        by calling display_x_helper.


        Args:
            x: number of games to be displayed.
        """
        self._display_x_helper(x, next=True, prev_game=False)




if __name__ == '__main__':
    S = ScheduleUI()
    S.display(horiz=True)
