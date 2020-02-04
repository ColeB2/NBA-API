from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season, get_team

'''TODO: REMOVE UI elements, combine all 3, and use bool to select'''
def get_gameId(date=None, season=None, team=None):
    if season == None:
        season = get_season()
    if team == None:
        season = get_team()

    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'

    data = get_data(url)

    x = data['league']
    y = x['standard']

    if date == None:
        date = x['lastStandardGamePlayedIndex']

    gameId = y[last_game]['gameId']
    game_date = y[last_game]['gameUrlCode'][0:8]

    return gameId, game_date






def get_today_gameId(season=None, team=None):
    '''
    PARAMS : get_today_gameId(season, team)
    season : YYYY format, based on season start date, 2019 for 2019/2020 season
    team   : lowercase team name, ex: raptors, sixers
    example: get_today_gameId(2019, 'raptors')

    RETURNS   : tutple (gameId and TodayDate)
    gameId    : numberical id for the game today
    TodayDate : date of today in YYYYMMDD format
    example   : (0021900640, 20200120)
    '''
    if season == None:
        season = get_season()
    if team == None:
        team = get_team()

    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'

    data = get_data(url)
    x = data['league']
    y = x['standard']

    gameId = 'No Game Today'
    dateTime = data['_internal']['pubDateTime']
    TodayDate = dateTime[0:4] + dateTime[5:7] + dateTime[8:10]


    for i in range(len(y)):
        if TodayDate == y[i]['gameUrlCode'][0:8]:
            gameId = y[i]['gameId']
    return gameId, TodayDate


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



if __name__ == '__main__':
    x = get_today_gameId()
    print('Today Game ID and Date: ' + str(x))
    print()

    y = get_gameId(20200120)
    print('Id by date: 20200120: ' + str(y))

    print()
    z = get_last_gameId(season='2019', team='raptors')
    print('Last game played raptors: ' + str(z))
