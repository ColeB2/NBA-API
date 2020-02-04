from functions import get_data
from nbaschedule import get_last_gameId

def get_boxscore_data(date=None, gameId=None):
    """Gets raw json data for given game.

    Args:
        date: The date of the given game using YYYYMMDD format.
        gameId: The gameId for given game. Acquired using a get_gameId fucntion.
    Returns:
        Dictionary of raw json data from the data.nba.net boxscore endpoint
    """
    if not date or not gameId:
        x = get_last_gameId()
        gameId, date = get_last_gameId()

    url_start = 'http://data.nba.net/prod/v1/'
    url = str(url_start) + str(date) + '/' + str(gameId) + '_boxscore.json'

    data = get_data(url)
    return data

class BoxScore():
    """A class to sort and hold data for NBA _boxscore endpoint

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



if __name__ == '__main__':
    B = BoxScore()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(B.raw_data.keys())
    print('\n-----_internal---------------------------------------------------')
    print(B._internal.keys())

    print('\n-----basicGameData-----------------------------------------------')
    print(B.basic_game_data.keys())
    print(B.basic_game_data['arena'])
    print(B.basic_game_data['hTeam'])
    print(B.basic_game_data['vTeam'])

    print('\n-----previousMatchup---------------------------------------------')
    print(B.previous_matchup.keys())

    print('\n-----STATS-------------------------------------------------------')
    print(B.stats.keys())
    print('\n-----STATS BREAKDOWN---------------------------------------------')
    print('timesTied: ' + B.stats['timesTied'])
    print('leadChanges:' + B.stats['leadChanges'])
    print('vTeam: ' + str(B.stats['vTeam'].keys()))
    print('vTeam Totals :'  + str(B.stats['vTeam']['totals']))
    print('hTeam: ' + str(B.stats['hTeam'].keys()))
    print('hTeam Totals :'  + str(B.stats['hTeam']['totals']))
    print('activePlayers :' + str(B.stats['activePlayers'][0].keys()))
    print('activePlayers :' + str(B.stats['activePlayers']))
