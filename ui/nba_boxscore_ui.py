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
    def display(self, combined=False, score=True, ascii=True,
        home=True, visitors=True, first=True):
        """Prints the score and boxscore of the game to the console.

        Args:
            combined: Bool, combine score @ top or above respective boxscores.
            score: Bool, to display the score of game or not.
            fancy: Bool, to display the score in ascii or not.
            home: Bool, to display home team boxscore
            visitors: Bool, to display away team boxscore.
        """
        if combined:
            if score: self.display_score(ascii=ascii, combined=combined)
            if visitors: self.display_boxscore(visitors=visitors, first=first)
            if home: self.display_boxscore(home=home, first=first)
        else:
            if score:
                self.display_score(ascii=ascii, combined=combined,
                    team_data=self.B.vTeam_game_data)
            if visitors: self.display_boxscore(visitors=True, first=first)
            if score:
                self.display_score(ascii=ascii, combined=combined,
                    team_data=self.B.hTeam_game_data)
            if home: self.display_boxscore(home=True, first=first)

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

        for k,v in team_totals.items():
            if k in self.footer_totals:
                print(k,v)

        return [separator, footer]

    '''GAME SCORE UI'''
    def ascii_score(self, *team):
        text_str = ''
        for team_data in team:
            text_str += team_data['triCode'] + '   ' + \
            team_data['score'] + '   '

        text = pyfiglet.figlet_format(text_str, font='small')
        return text

    def display_score(self, ascii=True, combined=True, team_data=None):
        """
        Prints the triCode and score of game on separate lines to the console.

        Args:
            ascii: Bool, whether to use ascii score or not
            combined: Bool, whether to combine scores, or put them with respect
                of their own boxscores.
            team_data: team data, if combined is false, required to display
                proper team data at proper spot.
        """
        if combined:
            if ascii:
                print(self.ascii_score(self.B.vTeam_game_data,
                                       self.B.hTeam_game_data))
            else:
                print(self.B.vTeam_game_data['triCode'], end=' ')
                print(self.B.vTeam_game_data['score'])
                print(self.B.hTeam_game_data['triCode'], end=' ')
                print(self.B.hTeam_game_data['score'])

        else:
            if ascii:
                print(self.ascii_score(team_data))
            else:
                print(team_data['triCode'], end=' ')
                print(team_data['score'])






if __name__ == '__main__':
    print('Create Box Score Object')
    boxscore = BoxScoreUI()
    print('Display Box Score Widget\n')
    boxscore.display()

    boxscore2 = BoxScoreUI()
    boxscore.display(first=False)
