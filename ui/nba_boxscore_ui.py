from ui_functions import Widget
from tabulate import tabulate
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
        boxscore_totals: display
    """
    def __init__(self, date=None, gameId=None):
        self.B = BoxScore(date, gameId)

        self.boxscore_headers = ['NO', 'Name', 'MIN', 'FG', '3PT', 'FT','OR',
          'DR', 'TR', 'AST', 'STL', 'BLK', 'TOV', 'PF',  '+/-', 'PTS']

        self.data_headers = ['jersey', ('firstName', 'lastName'), 'min',
         ('fgm', 'fga'), ('tpm', 'tpa'), ('ftm', 'fta'), 'offReb', 'defReb',
         'totReb', 'assists', 'steals', 'blocks', 'turnovers', 'pFouls',
         'plusMinus', 'points']

        self.footer_totals =  ['--', '-----------------------', 'min',
         ('fgm', 'fga'), ('tpm', 'tpa'), ('ftm', 'fta'), 'offReb', 'defReb',
         'totReb', 'assists', 'steals', 'blocks', 'turnovers', 'pFouls',
         'plusMinus', 'points']


    '''BOXSCORE UI'''
    def display(self, ascii=True):
        """Prints the score and boxscore of the game to the console.

        Args:
            combined: Bool, combine score @ top or above respective boxscores.
            score: Bool, to display the score of game or not.
            fancy: Bool, to display the score in ascii or not.
            home: Bool, to display home team boxscore
            visitors: Bool, to display away team boxscore.
        """
        self.horizontal_display(
            (self.B.hTeam_player_stats, self.B.hTeam_totals),
            self.display_score, header=True)
        self.horizontal_display(
            (self.B.vTeam_player_stats, self.B.vTeam_totals), header=True)

    def display_boxscore(self, home=False, visitors=False, first=True):
        """Prints the boxscore of the game to the console.

        Args:
            home: boolean, to display home team boxscore.
            visitors: boolean, to display visitor team boxscore.

        """
        if visitors:
            table = self.create_table(self.B.vTeam_player_stats, \
                self.B.vTeam_totals, first=first)
            print(tabulate(table, self.boxscore_headers, tablefmt = 'psql'))

        if home:
            table = self.create_table(self.B.hTeam_player_stats, \
                self.B.hTeam_totals, first=first)
            print(tabulate(table, self.boxscore_headers, tablefmt = 'psql'))


    def create_table(self, data, team_totals, first=True):
        """
        Creates a list, which is used to create table using the tabulate module.

        Args:
            data: data, which is used to create table.
              :ex: self.vTeam_player_stats
            team_totals: totals of given team, to display totals footer.
              :ex: self.hTeam_totals
            first: Boolean to chose between Full first name, or initial.


        Returns:
        A list which when combined with tabulate module, pretty prints a table
        of the games boxscore stats
        """
        table = []
        for player in data:
            new_row = []
            for index, stat in enumerate(self.data_headers):
                if type(stat) is tuple:
                    if stat[0] == 'firstName':
                        if first:
                            stat_str = f"{player[stat[0]]} {player[stat[1]]}"
                        else:
                            stat_str = f"{player[stat[0]][0:1]}. " \
                                       f"{player[stat[1]]}"
                    else:
                        stat_str = f"{player[stat[0]]}-{player[stat[1]]}"
                    new_row.append(stat_str)
                else:
                    stat_str = f"{player[stat]}"
                    new_row.append(stat_str)
            table.append(new_row)
        table.extend(self.totals_footer(team_totals))
        return table

    def totals_footer(self, team_totals):
        """Creates a list of totals to be added to the footer of boxscore.

        Args:
            team_totals: dict of given teams totals for the game.
        """
        separator =  [
        f"==", f"=======================", f"=====",
        f"======", f"======", f"======", f"===",f"===",f"===",
        f"===", f"===", f"===",
        f"===", f"===", f"===",
        f"==="]

        footer = [
            f"--", f"-----------------------", f"{team_totals['min']}",
            f"{team_totals['fgm']}-{team_totals['fga']}",
            f"{team_totals['tpm']}-{team_totals['tpa']}",
            f"{team_totals['ftm']}-{team_totals['fta']}",
            f"{team_totals['offReb']}", f"{team_totals['defReb']}",
            f"{team_totals['totReb']}", f"{team_totals['assists']}",
            f"{team_totals['steals']}", f"{team_totals['blocks']}",
            f"{team_totals['turnovers']}", f"{team_totals['pFouls']}",
            f"{team_totals['plusMinus']}", f"{team_totals['points']}" ]

        return [separator, footer]

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

    '''HORIZ display'''
    def set_horiz_headers(self, data):
        """


        """
        headers = []
        head = []

        """set boxscore HEADER"""
        for item in self.boxscore_headers:
            head.append(item)
        headers.append(head)

        """set player stats"""
        for player in data[0]:
            player_list = []
            for item in self.data_headers:
                if type(item) is tuple:
                    player_list.append(f"{player[item[0]]}-{player[item[1]]}")
                else:
                    player_list.append(f"{player[item]}")
            headers.append(player_list)

        """set footers"""
        footers = self.totals_footer(data[1])
        foot = []
        for i in range(len(footers)):
            foot = []
            for item in footers[i]:
                foot.append(item)

            headers.append(foot)

        return headers

    def get_horiz_headers(self, data):
        headers = self.set_horiz_headers(data)
        return headers




if __name__ == '__main__':
    boxscore = BoxScoreUI()
    boxscore.display()
