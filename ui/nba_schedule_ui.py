from ui_functions import Widget
import calendar

from datetime import datetime
from dateutil import tz

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbaschedule import Schedule



class ScheduleUI(Widget):
    """A class to represent an NBA team's schedule.

    Attributes:
        season:
        team:

        last:
        next:
        full:

        S:

        regular_season:
        offset:
        last_game_idx:

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
        if horiz: self.horizontal_display(self.get_nested_list_data())
        if not horiz:
            if last: self.display_last_x_games()
            if next: self.display_next_x_games()
        if full: self.display_season_schedule()


    """HORIZONTAL DISPLAY METHODS"""
    def create_nested_list(self, data):
        """Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.

        Args:
            data: The data to be parsed through to create the lists.

        Returns:
            List of lists, date, vs_info, result_info.
            date: list of the dates, formatted with spacing for given games.
            vs_info: list of strs, '@' or 'VS' based on whether team is home or
                away.
            result_info: list of str, based on results of the game, given as
                either a 'W' or 'L'
        """
        date = []
        vs_info= []
        result_info = []
        for game_idx in data:
            game = self.S.standard[game_idx]

            date_str = self.format_date(game['startDateEastern'])

            home_listing_str = self.get_home_listing(game)
            opponent_str = self.get_opponent(game, home_listing_str)
            vs_str = f"{home_listing_str} {opponent_str}"

            result_str = self.get_result(game, home_listing_str)

            date.append(date_str)
            vs_info.append(vs_str)
            result_info.append(result_str)

        return [date, vs_info, result_info]


    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)


    def get_nested_list_data(self):
        """Acquires/organizes the data to be used in the get_nested_list method
        """
        games = self.S.get_x_games()
        games.extend(self.S.get_x_games(x=6, next=False, prev_game=False))
        games.sort()
        return games


    def get_home_listing(self, game_data):
        """Finds out if chosen team is home team or not then returns a
        corrospoding string, 'VS' or '@'

        Args:
            game_data: dict data for given game.

        Returns:
            boolean, True if home team, False otherwise.
        """
        if game_data['isHomeTeam']:
            return 'VS'
        else:
            return '@'


    def get_opponent(self, game_data, location=None):
        """Gets the opponent TRI code for given game.

        Args:
            game_data: dict daa for given game.
            location: str, 'VS' or '@' based on home/away team.

        Returns:
            Tri code for the oposing team.
        """
        if location == 'VS':
            return game_data['gameUrlCode'][9:12]
        else:
            return game_data['gameUrlCode'][12:]


    def get_result(self, game_data, location):
        """Gets the result of given game.

        Args:
            game_data: dict data for given game.
            location: str, VS or @ based on if team is home or away

        Returns:
            string, containing results of game. Ex: W 137-126
        """
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
            res = f"{self.convert_time(game_data['startTimeUTC'])}"

        dash = '-' if fave_score != '' else ''

        return f"{res} {fave_score}{dash}{opp_score}"


    """VERTICAL DISPLAY METHODS"""
    def display_season_schedule(self):
        """Method used to display all regular season games to the console."""
        for game in enumerate(self.regular_season):
            self.display_game_information(game[0])
        print()


    def display_game_information(self, game):
        """Method used to print approrpiate information to the console. Prints,
        date, team tricode and score.

        Args:
            game: index value of game to be printed
        """
        month = calendar.month_abbr[int( \
            self.regular_season[game]['startDateEastern'][4:6])]
        day = self.regular_season[game]['startDateEastern'][6:]
        year = self.regular_season[game]['startDateEastern'][2:4]
        away = self.regular_season[game]['gameUrlCode'][9:12]
        away_score = self.regular_season[game]['vTeam']['score'].rjust(3)
        home = self.regular_season[game]['gameUrlCode'][12:]
        home_score = self.regular_season[game]['hTeam']['score'].rjust(3)
        print(f"{month}/{day}/{year} {away} {away_score} {home} {home_score}")


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

    print('VERTICAL')
    S = ScheduleUI()
    S.display(horiz=False, last=True, next=True)
