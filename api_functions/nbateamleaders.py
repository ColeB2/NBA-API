from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_team, get_season

MAIN_FIVE_STATS = ['ppg', 'trpg', 'apg', 'bpg', 'spg']
main_five_stats = []

def get_team_leaders_data(team=None, season=None):
    """Gets raw json data for stat leaders for given team.

    Args:
        team: lowercase team name of team. ex: raptors, sixers, bulls
        season: Year of season start date. Ex: 2019 for the 2019/2020 season.

    Returns:
        Dict of raw json data from data.nba.net /leaders.json endpoint
    """
    if not team: team = get_team()
    if not season: season = get_season()

    url1 = 'http://data.nba.net/prod/v1/'
    url_end = '/leaders.json'
    url = str(url1) + str(season) + '/teams/' + str(team.lower()) + str(url_end)

    data = get_data(url)
    return data


class TeamLeaders(object):
    """A class to sort and hold data from NBA's /leaders.json endpoint

    Attributes:
        raw_data: dictionary of raw json data
        _internal: raw_data key of internal data
        league: data of various leagues
        standard: raw_data key, holds data of respective leaders
    """
    def __init__(self, team=None, season=None):
        self.team = team
        self.season = season

        self.raw_data = get_team_leaders_data(team=self.team,
                                              season=self.season)
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']

        self.leader_keys = ['ppg','trpg','apg','fgp','tpp','ftp','bpg','spg',
            'tpg','pfpg']
        self.leaders = self.standard
        self.leaders.pop('seasonStageId', None)



if __name__ == '__main__':
    TL = TeamLeaders()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(TL.raw_data.keys())

    print('\n-----_internal---------------------------------------------------')
    print(TL._internal.keys())

    print('\n-----league------------------------------------------------------')
    print(TL.league.keys())

    print('\n-----standard----------------------------------------------------')
    print(TL.standard.keys())
    print(TL.standard)
    print()
    print()
    print(TL.leaders)
    print('--UI TEST--')
    for stat, values in TL.leaders.items():
        #print(stat,values, end=' ')
        print(stat.upper() + '/Game', end=' ')
        print(values[0]['value'])
        print(values[0]['personId'])
    from tabulate import tabulate
    T1 =[ ['PASCAL', 'SIAKAM'], ['SERGE', 'IBAKA'],['KYLE', 'LOWRY']]
    H1 =['PTS/GAME: 23.7', 'REB/GAME: 8', 'FG_/GAME: 10']
    print(tabulate(T1, H1, tablefmt='psql'))
    TABLE= [
    ['PTS/GAME: 28', 'PASCAL SIAKAM', 'STL/GAME: 2', 'FRED VANFLEET',
    'REB/GAME: 8', 'SERGE IBAKA'],
    ['PTS/GAME: 28', 'PASCAL SIAKAM', 'STL/GAME: 2', 'FRED VANFLEET',
    'REB/GAME: 8', 'SERGE IBAKA'],
    ['PTS/GAME: 28', 'PASCAL SIAKAM', 'STL/GAME: 2', 'FRED VANFLEET',
    'REB/GAME: 8', 'SERGE IBAKA'],
    ['PTS/GAME: 28', 'PASCAL SIAKAM', 'STL/GAME: 2', 'FRED VANFLEET',
    'REB/GAME: 8', 'SERGE IBAKA']
    ]
    print(tabulate(TABLE, tablefmt='psql'))
    print()
    TABLE= [
    ['PTS/G: 28', 'REB/G 8', 'AST/G: 8', 'FG/G: 50%', '3PT/G',
    'FT/G: 85%', 'BLK/G: 0.9', 'STLS/G: 2'],

    ['P. Siakam', 'S. Ibaka', 'K. Lowry', 'F. VanFleet','M. Thomas',
    'D. Hernandez', 'S. Ibaka', 'F.Vanfleet']
    ]
    print(tabulate(TABLE, tablefmt='psql'))
