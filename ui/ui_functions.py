'''
Skeleton class for widget, all ui elements will inherit from, has basic UI
functions used to format and print to command line
'''


class Widget():
    def __init__(self):
        pass

    def pretty_print(obj, depth):
        '''Used to limit the length of strings
        params:
        obj   : information needed to be printed.
        depth : length limit of the created string.

        prints: string which is cut off at the depth
        '''
        print(str(obj)[:depth], end='|')




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

"""
