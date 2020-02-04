from functions import get_data, get_today_date

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season, get_team

'''TODO: REMOVE UI elements, combine all 3, and use bool to select'''
def get_schedule_data(season=None, team=None):
    """Gets raw json data of given team schedule for given season.

    Args:
        season: year of season start date, YYYY format.
        team: teamUrl for given team -> team name, ex: raptors, sixers

    Returns:
        Dictionary of raw json data from data.nba.net schedule endpoint
    """
    if not season: season = get_season()
    if not team: team = get_team()

    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'

    data = get_data(url)
    return data

class Schedule():
    """A class to sort and hold data for NBA /schedule.json endpoint

    Attributes:

    """
    def __init__(self, season=None, team=None):
        self.season = season
        self.team = team

        self.raw_data = get_schedule_data(season=self.season, team=self.team)
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']

        self.last_game_idx = self.league['lastStandardGamePlayedIndex']
        self.last_game = self.standard[self.last_game_idx]
        self.last_game_id = self.last_game['gameId']
        self.last_game_date = self.last_game['gameUrlCode'][0:8]
        self.last_game_id_date = (self.last_game_id, self.last_game_date)

    def get_last_gameId(self, season=None, team=None):
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


def get_today_gameId(season=None, team=None):
    """
    PARAMS : get_today_gameId(season, team)
    season : YYYY format, based on season start date, 2019 for 2019/2020 season
    team   : lowercase team name, ex: raptors, sixers
    example: get_today_gameId(2019, 'raptors')

    RETURNS   : tutple (gameId and TodayDate)
    gameId    : numberical id for the game today
    TodayDate : date of today in YYYYMMDD format
    example   : (0021900640, 20200120)
    """
    data = get_schedule_data(season, team)
    x = data['league']
    y = x['standard']

    gameId = False
    date = get_today_date()

    for i in range(len(y)):
        if date == y[i]['gameUrlCode'][0:8]:
            gameId = y[i]['gameId']

    if gameId == False:
        for i in range(len(y)):
            if date == y[i]['gameUrlCode'][0:8]:
                pass

    return gameId, date


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






if __name__ == '__main__':
    S = Schedule()
    x = get_today_gameId()
    print('Today Game ID and Date: ' + str(x))
    print()

    y = get_gameId(20200120)
    print('Id by date: 20200120: ' + str(y))

    print()
    z = S.last_game_id_date
    print('Last game played raptors: ' + str(z))

    raw_data = get_schedule_data()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(raw_data.keys())
    print('\n-----internal----------------------------------------------------')
    _internal = raw_data['_internal']
    print(_internal.keys())

    print('\n-----league------------------------------------------------------')
    league = raw_data['league']
    print(league.keys())
    print('last...Game...Index: ' + str(league['lastStandardGamePlayedIndex']))

    print('\n-----standard----------------------------------------------------')
    standard = league['standard']
    #print(standard)

    print('\nSingle Game keys')
    print(standard[0].keys())
    print(standard[0]['gameUrlCode'])
    print(standard[0])

    print('\n-----LastGame----------------------------------------------------')
    print(S.last_game)
