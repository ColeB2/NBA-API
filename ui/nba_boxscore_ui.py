from ui_functions import Widget
from tabulate import tabulate

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbagameboxscore import get_boxscore_data



class BoxScore(Widget):
    """A class to represent an NBA box score.

    Attributes:
        date: Date in YYYYMMDD format.
        gameId: gameId for the box score of given game.

        raw_data: dictionary of the raw json data.

        _internal: raw_data key of of iternal data.

        basic_game_data: raw_data key of base game data.
        vTeam_game_data:  visiting team basic game data.
        vTeam_game_data: visiting team basic game data.

        previous_matchup: raw_data key of stats from previous matchup.

        stats: raw_data key of the games stats.
        player_stats: list of game stats of each player in the game.
        vTeam_player_stats: list of all player stats for visiting team.
        hTeam_player_stats: list of all player stats for home team.
        vTeam_totals: dict of the totals of all stats for visiting team.
        hTeam_totals: dict of the totals of all stats for home team.

        boxscore_headers: Display headers for boxscore UI.
        data_headers: dict keys corosponding to boxscore headers.
        boxscore_totals: display


    """
    def __init__(self, date=None, gameId=None):
        self.date = date
        self.gameId = gameId

        self.raw_data = get_boxscore_data(date=self.date, gameId=self.gameId)
        self._internal = self.raw_data['_internal']

        self.basic_game_data = self.raw_data['basicGameData']
        self.vTeam_game_data = self.basic_game_data['vTeam']
        self.hTeam_game_data = self.basic_game_data['hTeam']

        self.previous_matchup = self.raw_data['previousMatchup']

        self.stats = self.raw_data['stats']
        self.player_stats = self.stats['activePlayers']
        self.vTeam_player_stats = [player for player in self.player_stats \
            if player['teamId'] == self.player_stats[0]['teamId']]
        self.hTeam_player_stats = [player for player in self.player_stats \
            if player['teamId'] == self.player_stats[-1]['teamId']]

        self.vTeam_totals = self.stats['vTeam']['totals']
        self.hTeam_totals = self.stats['hTeam']['totals']



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

    '''BOXSCORE'''
    def display(self, score=True, home=True, visitors=True):
        if score: self.display_score()

        if visitors:
            table = self.create_table(self.vTeam_player_stats, \
                self.vTeam_totals)
            print(tabulate(table, self.boxscore_headers, tablefmt = 'psql'))

        if home:
            table = self.create_table(self.hTeam_player_stats, \
                self.hTeam_totals)
            print(tabulate(table, self.boxscore_headers, tablefmt = 'psql'))

    def create_table(self, data, team_totals):
        """
        Creates a list, which is used to create table using the tabulate module.

        Args:
            data: data, which is used to create table.
              :ex: self.vTeam_player_stats
            team_totals: totals of given team, to display totals footer.
              :ex: self.hTeam_totals


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
                        stat_str = str(player[stat[0]]) +  \
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

    def test(self):
        pass

    '''SCOREBOARD'''
    def display_score(self, home=True, visitors=True):
        """Prints the triCode and score of game on separate lines."""
        if visitors:
            print(self.vTeam_game_data['triCode'], end=' ')
            print(self.vTeam_game_data['score'])
        if home:
            print(self.hTeam_game_data['triCode'], end=' ')
            print(self.hTeam_game_data['score'])






if __name__ == '__main__':
    print('Create Box Score Object')
    boxscore = BoxScore()
    print('Display Box Score Widget\n')
    boxscore.display()
