from functions import get_data, get_today_date


def get_score_data(date=None):
    """Gets raw json data of all scores on a given date for all teams.

    Args:
        date: YYYYYMMDD format for day you want scores of.

    Returns:
        Dict of raw json data from data.nba.net.../scoreboard.json endpoint
    """
    if not date: date = get_today_date()

    url_start = 'http://data.nba.net/prod/v1/'
    url = str(url_start) + str(date) + str('/scoreboard.json')

    data = get_data(url)
    return data

class ScoreBoard():
    """A class to sort and hold data for NBA /scoredbord.json endpoint

    Attributes:

    """
    def __init__(self, date=None):
        self.date = date if date != None else get_today_date()

        self.raw_data = get_score_data(date=self.date)
        self._internal = self.raw_data['_internal']

        self.num_games = self.raw_data['numGames']

        self.games = self.raw_data['games'] #list of games

if __name__ == '__main__':

    SB = ScoreBoard(date=20200310)
    SB = ScoreBoard()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(SB.raw_data.keys())

    print('\n-----_internal---------------------------------------------------')
    print(SB._internal)

    print('\n-----num_games---------------------------------------------------')
    print(SB.num_games)

    print('\n-----games-------------------------------------------------------')
    print(SB.games)

    print(f"Games Keys: {SB.games[0].keys()}")
    print(SB.games[0])


    print('Test')
    print(SB.games[0]['isGameActivated'])
    print(SB.games[0]['period'])
    print(SB.games[-1]['hTeam'])
    print(SB.games[-1]['vTeam'])
    print(SB.games[0]['hTeam'])
    print(SB.games[-1]['hTeam'])
