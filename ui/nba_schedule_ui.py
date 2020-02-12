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


    def display(self):
        '''FIX HARD CODING'''
        """Main display call, to display specified schedules.

        Args:
            last_x: Boolean, decides whether to display last x games.
            next_x: Boolean, decides whether to display next x games.
            full_schedule: Boolean, decides whether to display full schedule.
        """
        if self.full: self.display_season_schedule()
        if self.last: self.display_last_x_games()
        if self.next: self.display_next_x_games()
        self.horizontal_display()

    def display_season_schedule(self):
        """Method used to display all regular season games to the console."""
        for game in enumerate(self.regular_season):
            self.display_game_information(game[0])
        print()


    '''Vertical Display'''
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



    '''Horizontal Display'''
    def home_or_away(self, game_data):
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

        if fave_score > opp_score:
            res = 'W'
        else:
            res = 'L'



        return res + ' ' + fave_score + '-' + opp_score


    def set_horiz_headers(self):
        pass

    def horizontal_display(self):
        table = []
        date = []
        vs_info = []
        res_info = []
        games = self.S.get_x_games()
        for game_idx in games:
            game = self.S.standard[game_idx]

            loc = self.home_or_away(game)
            opp = self.get_opponent(game, loc)
            vs_str = loc + ' ' + opp
            res_str = self.get_result(game, loc)
            print(res_str)
            print(vs_str)

            vs_info.append(vs_str)
            res_info.append(res_str)
        table.append(vs_info)
        table.append(res_info)
        print(tabulate(table, tablefmt='psql'))






if __name__ == '__main__':
    S = ScheduleUI(full=True)
    S.display()
