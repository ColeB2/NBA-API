from ui_functions import Widget
import pyfiglet

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbagameboxscore import BoxScore
from functions import get_full_name



class BoxScoreUI(Widget):
    """A class to represent an NBA box score.

    Attributes:
        B: BoxScore class which holds all stats/methods for boxscore
        boxscore_headers: Display headers for boxscore UI.
        data_headers: dict keys corosponding to boxscore headers.
        separator: list of strings used to separate data in nested list.
    """
    def __init__(self, date=None, gameId=None):
        self.B = BoxScore(date, gameId)

        self.boxscore_headers = ['NO', 'Name', 'MIN', 'FG', '3PT', 'FT','OR',
          'DR', 'TR', 'AST', 'STL', 'BLK', 'TOV', 'PF',  '+/-', 'PTS']

        self.data_headers = ['jersey', ('firstName', 'lastName'), 'min',
         ('fgm', 'fga'), ('tpm', 'tpa'), ('ftm', 'fta'), 'offReb', 'defReb',
         'totReb', 'assists', 'steals', 'blocks', 'turnovers', 'pFouls',
         'plusMinus', 'points']



    def display(self, horiz=True):
        """Prints the score and boxscore of the game to the console.

        Args:
        """
        if horiz:
            self.horizontal_display(
                (self.B.hTeam_player_stats, self.B.hTeam_totals),
                self.display_score, header=True)
            self.horizontal_display(
                (self.B.vTeam_player_stats, self.B.vTeam_totals), header=True)


    def display_score(self):
        """
        Prints the triCode and score of game to the console using ascii.
        """
        print(self.ascii_score(self.B.vTeam_game_data, self.B.hTeam_game_data))


    """HORIZONTAL DISPLAY METHODS"""
    def create_nested_list(self, data):
        """Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.

        Args:
            data: The data to be parsed through to create the lists.

        Returns:
            List of all the stats, all players values for said stats,
            a separator and totals of all said stats.

        """
        nested_list = []
        """Stat Header"""
        boxscore_headers, data_headers = self.set_data_headers(small='False')
        self.boxscore_headers = boxscore_headers
        self.data_headers = data_headers

        nested_list.append(self.boxscore_headers)

        NAMES = get_full_name()

        """Player Stats"""
        for player in data[0]:
            player_list = []
            for item in self.data_headers:
                if type(item) is tuple:
                    if item[0] == 'firstName':
                        first, last = f"{player['firstName']} ",\
                                      f"{player['lastName']}"
                        if NAMES == 'False':
                            first = f"{first[0:1]}."

                        player_list.append(f"{first} {last}")

                    else:
                        player_list.append(f"{player[item[0]]}-"
                                           f"{player[item[1]]}")
                else:
                    player_list.append(f"{player[item]}")
            nested_list.append(player_list)

        """Team Totals"""
        totals = self.get_totals(data[1])
        separator = self.create_separator('=', 19)
        nested_list.extend([separator, totals])

        return nested_list

    def create_separator(self, char, len_longest_name=19):
        name = self.create_name_separator(char, len_longest_name)

        separator = [ f"==", f"{name}", f"=====",
        f"======", f"======", f"======", f"===",f"===",f"===", f"===", f"===",
        f"===", f"===", f"===", f"===", f"===" ]

        return separator

    def create_name_separator(self, char, len_longest_name):
        if get_full_name() == 'True':
            len_longest_name = 24
        return f"{int(len_longest_name)*str(char)}"

    def create_name_separator(self, char, len_longest_name):
        self.get_longest_name()
        if get_full_name() == 'True':
            len_longest_name = 24
        return f"{int(len_longest_name)*str(char)}"

    def get_longest_name(self):
        """TODO:
        FIX, IMPROVE, IMPLMENT"""
        self.player_names = []
        if get_full_name() == 'True':
            for player in self.B.hTeam_player_stats:
                name = f"{player['firstName']} {player['lastName']}"
                self.player_names.append(name)
            for player in self.B.vTeam_player_stats:
                name = f"{player['firstName']} {player['lastName']}"
                self.player_names.append(name)
        else:
            for player in self.B.hTeam_player_stats:
                name = f"{player['firstName'][0:1]}. {player['lastName']}"
                self.player_names.append(name)
            for player in self.B.vTeam_player_stats:
                name = f"{player['firstName'][0:1]}. {player['lastName']}"
                self.player_names.append(name)
        longest_name = int()
        for player in self.player_names:
            if len(player) > longest_name:
                longest_name = len(player)





    def set_data_headers(self, small='True'):
        if small == 'True':
            boxscore_headers =  ['Name', 'TR', 'AST', 'STL', 'BLK', 'PTS']
            data_headers = [('firstName', 'lastName'), 'totReb', 'assists',
                                  'steals', 'blocks', 'points']
        else:
            boxscore_headers = ['NO', 'Name', 'MIN', 'FG', '3PT', 'FT','OR',
              'DR', 'TR', 'AST', 'STL', 'BLK', 'TOV', 'PF',  '+/-', 'PTS']
            data_headers = ['jersey', ('firstName', 'lastName'), 'min',
             ('fgm', 'fga'), ('tpm', 'tpa'), ('ftm', 'fta'), 'offReb', 'defReb',
             'totReb', 'assists', 'steals', 'blocks', 'turnovers', 'pFouls',
             'plusMinus', 'points']

        return boxscore_headers, data_headers


    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)


    def get_totals(self, team_totals):
        """Creates a list of totals to be added to the footer of boxscore.

        Args:
            team_totals: dict of given teams totals for the game.
        """
        name_sep = self.create_name_separator('-', len_longest_name=19)
        totals = [
            f"--", f"{name_sep}", f"{team_totals['min']}",
            f"{team_totals['fgm']}-{team_totals['fga']}",
            f"{team_totals['tpm']}-{team_totals['tpa']}",
            f"{team_totals['ftm']}-{team_totals['fta']}",
            f"{team_totals['offReb']}", f"{team_totals['defReb']}",
            f"{team_totals['totReb']}", f"{team_totals['assists']}",
            f"{team_totals['steals']}", f"{team_totals['blocks']}",
            f"{team_totals['turnovers']}", f"{team_totals['pFouls']}",
            f"{team_totals['plusMinus']}", f"{team_totals['points']}" ]

        return totals


    def ascii_score(self, *team):
        text_str = ''
        for team_data in team:
            text_str += f"{team_data['triCode']}   {team_data['score']}   "

        text = pyfiglet.figlet_format(text_str, font='small')
        return text



if __name__ == '__main__':
    boxscore = BoxScoreUI()
    boxscore.display()
