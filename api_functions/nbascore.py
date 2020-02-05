from functions import get_data, get_today_date


def get_score_data(date=None):
    """
    Gets the score of a given game given the gameId and the date
    Used in conjunction with get_today_gameId or get_last_gameId to aquire said
    gameId, and date

    param  : get_score(gameId, date)
    gameId : numberical code for give game, ex '0021900640'
    date   : date in YYYYMMDD format for given game

    EXAMPLE USES:
    req import  : from nbaschedule import get_last_gameId, get_today_gameId
    scores = get_last_gameId()
    my_score = get_score(gameId=scores[0], date=scores[1])
    returns     : score as well as prints to console
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
    from nbaschedule import Schedule
    S = Schedule()

    SB = ScoreBoard(date=20200204)
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(SB.raw_data.keys())

    print('\n-----_internal---------------------------------------------------')
    print(SB._internal)

    print('\n-----num_games---------------------------------------------------')
    print(SB.num_games)

    print('\n-----games-------------------------------------------------------')
    print(SB.games)

    print('Games Keys:')
    print(SB.games[0].keys())

    print('Test')
    print(SB.games[0]['vTeam'])
