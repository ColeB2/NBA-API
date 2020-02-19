from ui_functions import Widget
import pyfiglet

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbagameboxscore import BoxScore



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

        self.separator = [ f"==", f"=======================", f"=====",
        f"======", f"======", f"======", f"===",f"===",f"===", f"===", f"===",
        f"===", f"===", f"===", f"===", f"===" ]


    '''BOXSCORE UI'''
    def display(self, ascii=True):
        """Prints the score and boxscore of the game to the console.

        Args:
        """
        self.horizontal_display(
            (self.B.hTeam_player_stats, self.B.hTeam_totals),
            self.display_score, header=True)
        self.horizontal_display(
            (self.B.vTeam_player_stats, self.B.vTeam_totals), header=True)

    '''HORIZ display'''
    def create_nested_list(self, data):
        """Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.

        Args:
            data: The data to be parsed through to create the lists.

        """
        headers = []
        """Stat Header"""
        headers.append(self.boxscore_headers)

        """Player Stats"""
        for player in data[0]:
            player_list = []
            for item in self.data_headers:
                if type(item) is tuple:
                    player_list.append(f"{player[item[0]]}-{player[item[1]]}")
                else:
                    player_list.append(f"{player[item]}")
            headers.append(player_list)

        """Team Totals"""
        totals = self.get_totals(data[1])
        headers.extend([self.separator, totals])

        return headers

    def get_nested_list(self, data):
        nested_list = self.create_nested_list(data)
        return nested_list

    def get_totals(self, team_totals):
        """Creates a list of totals to be added to the footer of boxscore.

        Args:
            team_totals: dict of given teams totals for the game.
        """
        totals = [
            f"--", f"-----------------------", f"{team_totals['min']}",
            f"{team_totals['fgm']}-{team_totals['fga']}",
            f"{team_totals['tpm']}-{team_totals['tpa']}",
            f"{team_totals['ftm']}-{team_totals['fta']}",
            f"{team_totals['offReb']}", f"{team_totals['defReb']}",
            f"{team_totals['totReb']}", f"{team_totals['assists']}",
            f"{team_totals['steals']}", f"{team_totals['blocks']}",
            f"{team_totals['turnovers']}", f"{team_totals['pFouls']}",
            f"{team_totals['plusMinus']}", f"{team_totals['points']}" ]

        return totals

    '''GAME SCORE UI'''
    def ascii_score(self, *team):
        text_str = ''
        for team_data in team:
            text_str += f"{team_data['triCode']}   {team_data['score']}   "

        text = pyfiglet.figlet_format(text_str, font='small')
        return text

    def display_score(self):
        """
        Prints the triCode and score of game to the console using ascii.
        """
        print(self.ascii_score(self.B.vTeam_game_data, self.B.hTeam_game_data))






if __name__ == '__main__':
    boxscore = BoxScoreUI()
    boxscore.display()
