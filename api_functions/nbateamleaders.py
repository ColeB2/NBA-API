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

        self.leaders = self.create_dictionary(self.standard, self.leader_keys)

    def create_dictionary(self, dictionary, keys):
        """Creates a new dictionary from a dictionary only using the keys given.
        Contains conditional to add a value which is a list length 1, as a non
        list value


        Args:
            dictionary: dict, that is to be copied
            keys: keys of the dict to be copied
        """
        leaders_dict = {}
        for key, value in dictionary.items():
            if key in keys:
                if type(value) is list and len(value) == 1:
                    leaders_dict[key] = value[0]
                else:
                    leaders_dict[key] = value
        return leaders_dict



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
    print('--TEST--')
    print(TL.standard)
    print(TL.leaders)
