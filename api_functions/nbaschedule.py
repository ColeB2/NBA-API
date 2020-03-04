from functions import get_data, get_today_date

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_info

def get_schedule_data(season=None, team=None):
    """Gets raw json data of given team schedule for given season.

    Args:
        season: year of season start date, YYYY format.
        team: teamUrl for given team -> team name, ex: raptors, sixers

    Returns:
        Dict of raw json data from data.nba.net.../schedule.json endpoint
    """
    if not season: season = get_info(('Values', 'season'))
    if not team: team = get_info(('Team', 'team'))

    url_start = 'http://data.nba.net/prod/v1/'
    url = url_start + str(season) + '/teams/' + str(team) + '/schedule.json'

    data = get_data(url)
    return data

class Schedule():
    """A class to sort and hold data for NBA /schedule.json endpoint

    Attributes:

    """
    def __init__(self, season=None, team=None):
        self.season = season if season != None \
                           else get_info(('Values', 'season'))
        self.team = team if team != None else get_info(('Team', 'team'))

        self.raw_data = get_schedule_data(season=self.season, team=self.team)
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']

        self.standard = self.league['standard'] #list of all games

        self.last_game_idx = self.league['lastStandardGamePlayedIndex']
        self.last_game = self.standard[self.last_game_idx]
        self.last_game_id = self.last_game['gameId']
        self.last_game_date = self.last_game['gameUrlCode'][0:8]
        self.last_game_id_date = (self.last_game_id, self.last_game_date)

    def get_gameId(self, date=None, season=None, team=None):
        """Gets game id for given date, season and team.

        Args:
            date: YYYYMMDD format for date of game.
            season: YYYY format, based on season start date.
            team: team name, ex: raptors, sixers, bulls etc.

        Returns:
            tuple of gameId and game_date.
        """
        gameId = None
        game_date = date

        for game in self.standard:
            if str(game_date) == str(game['gameUrlCode'][0:8]):
                gameId = game['gameId']

        return gameId, game_date

    def get_x_games(self, x=5, next=True, last_game=None, prev_game=True):
        """Method used to get data of next/last x games.

        Args:
            x: number of games to be retrieve
            next: Boolean value, set direction of, either next or last x games.
            last_game: index of last game played.
            prev_game: Boolean value, whether to include pervious game played.

        Returns:
            List of the all the games index.

        """
        if not last_game: last_game = self.last_game_idx
        dir = 1 if next else -1
        if not prev_game: last_game += dir
        games = []
        for game in range(last_game, last_game+(dir*x), dir):
            games.append(game)
        return games

if __name__ == '__main__':
    S = Schedule()

    y = S.get_gameId(date=20200120)
    print('Id by date: 20200120: ' + str(y))

    print()
    z = S.last_game_id_date
    print('Last game played raptors: ' + str(z))

    print('DECEMBER 12 2018:', end=" ")
    print(Schedule(season=2018).get_gameId(date=20181212))

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
    print(S.get_x_games())
