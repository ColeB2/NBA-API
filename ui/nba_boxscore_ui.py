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
    def display(self, score=True, fancy=True, home=True, visitors=True):
        """Prints the score and boxscore of the game to the console.

        Args:
            score: boolean, to display the score of game or not.
            fancy: boolean, to display the score in ascii or not.
            home: boolean, to display home team boxscore
            visitors: boolean, to display away team boxscore.
        """
        if score: self.display_score(fancy=fancy)
        if visitors: self.display_boxscore(visitors=visitors)
        if home: self.display_boxscore(home=home)

    def display_boxscore(self, home=False, visitors=False):
        """Prints the boxscore of the game to the console.

        Args:
            home: boolean, to display home team boxscore.
            visitors: boolean, to display visitor team boxscore.

        """
        if visitors:
            table = self.create_table(self.B.vTeam_player_stats, \
                self.B.vTeam_totals)
            print(tabulate(table, self.boxscore_headers, tablefmt = 'psql'))

        if home:
            table = self.create_table(self.B.hTeam_player_stats, \
                self.B.hTeam_totals)
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
        table = list()
        for player in data:
            new_row = list()
            for index, stat in enumerate(self.data_headers):
                if type(stat) is tuple:
                    if stat[0] == 'firstName':
                        if first:
                            stat_str = str(player[stat[0]]) +  \
                                 ' ' + str(player[stat[1]])
                        else:
                            stat_str = str(player[stat[0]][0:1]) + '. ' \
                                 ' ' + str(player[stat[1]])
                    else:
                        stat_str = str(player[stat[0]]) +  \
                             '-' + str(player[stat[1]])
                    new_row.append(stat_str)
                else:
                    stat_str = str(player[stat])
                    new_row.append(stat_str)
            table.append(new_row)
        table.extend(self.totals_footer(team_totals))
        return table

    def totals_footer(self, team_totals):
        """Creates a list of totals to be added to the footer of boxscore.

        Args:
            team_totals: dict of given teams totals for the game.
        """
        separator =  ['==','=======================', '=====',
        '======', '======', '======', '===','===','===',
        '===', '===', '===',
        '===', '===', '===',
        '===']

        footer  = ['--','-----------------------', str(team_totals['min']),
        str(team_totals['fgm'] + '-' +team_totals['fga'] ),
        str(team_totals['tpm'] + '-' +team_totals['tpa'] ),
        str(team_totals['ftm'] + '-' +team_totals['fta'] ),
        str(team_totals['offReb']),str(team_totals['defReb']),
        str(team_totals['totReb']), str(team_totals['assists']),
        str(team_totals['steals']), str(team_totals['blocks']),
        str(team_totals['turnovers']), str(team_totals['pFouls']),
        str(team_totals['plusMinus']), str(team_totals['points'])]

        return [separator, footer]

    '''GAME SCORE UI'''
    def display_score(self, fancy=True):
        """
        Prints the triCode and score of game on separate lines to the console.

        Args:
            fancy: bool, on whether to use ascii score or not
        """
        if fancy:
            text = pyfiglet.figlet_format(
                self.B.vTeam_game_data['triCode'] + '   ' +\
                self.B.vTeam_game_data['score']   + '   ' + \
                self.B.hTeam_game_data['triCode'] + '   ' + \
                self.B.hTeam_game_data['score'],
                font='small')
            print(text)
        else:
            print(self.B.vTeam_game_data['triCode'], end=' ')
            print(self.B.vTeam_game_data['score'])
            print(self.B.hTeam_game_data['triCode'], end=' ')
            print(self.B.hTeam_game_data['score'])








if __name__ == '__main__':
    print('Create Box Score Object')
    boxscore = BoxScoreUI()
    print('Display Box Score Widget\n')
    boxscore.display()
