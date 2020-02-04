'''
Skeleton class for widget, all ui elements will inherit from, has basic UI
functions used to format and print to command line
'''


class Widget():
    def __init__(self):
        pass




"""
def get_last_gameId(season=None, team=None):
    '''
    get_last_gameId(season, team)

    PARAMS : get_last_gameId(season, team)
    season : YYYY format, based on season start date, 2019 for 2019/20 season
    team   : lowercase team name, ex: raptors, sixers
    example: get_last_gameId(2019, 'raptors')

    RETURNS   : tutple (gameId, game_date)
    gameId    : numerical id number of the last game played
    game_date : date of last game played, format: YYYYMMDD
    '''
    if season == None:
        season = get_season()
    if team == None:
        team = get_team()


    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'


    data = get_data(url)
    gameId = 'No Game on '
    x = data['league']
    last_game = x['lastStandardGamePlayedIndex']

    y = x['standard'] #List of all game information
    gameId = y[last_game]['gameId']
    game_date = y[last_game]['gameUrlCode'][0:8]
    return gameId, game_date

def get_gameId(date=20200120, season=None, team=None):
    '''
    get_gameId(date, season, team)


    PARAMS : get_gameId(date, season, team)
    date   : YYYYMMDD format ex: 20200120 for 2020 January 20th
    season : YYYY format, based on season start date, 2019 for 2019/20 season
    team   : lowercase team name, ex: raptors, sixers
    example: get_gameId(20200120, 2019, 'raptors')

    RETURNS:
    gameId    : numerical id for the game at given date
    game_date : date inputed for given game
    example   : (0021900640, 20200120)
    '''
    if season == None:
        season = get_season()
    if team == None:
        team = get_team()

    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'


    data = get_data(url)
    gameId = 'No Game on ' + str(date)


    x = data['league']
    y = x['standard'] #List of all game information

    for i in range(len(y)):
        if str(date) == y[i]['gameUrlCode'][0:8]:
            gameId = y[i]['gameId']
    return gameId, date

"""
