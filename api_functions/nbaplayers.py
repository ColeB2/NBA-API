from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season

def get_player_data(season=None):
    """Gets raw json data for all players
    """
    if not season: season = get_season()

    url_start = 'http://data.nba.net/prod/v1/'
    url = str(url_start) + str(season) + '/players.json'

    data = get_data(url)

    return data


    player_name = str()
    data = get_data(url)
    x = data['league']
    y = x['standard']
    for i in range(len(y)):
        if y[i]['personId'] == personId:
            first_name = str(y[i]['firstName'])
            last_name = str(y[i]['lastName'])
            player_name = first_name + ' ' + last_name
    return player_name

class PlayerInfo(object):
    """A class to sort and hold data for NBA players.json enpoint

    Attributes:
    """

    def __init__(self):
        self.raw_data = get_player_data()
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']

        self.standard = self.league['standard']

    def get_player_name(self, personId):
        """Retrieves player name via their personId
        """
        for player in self.standard:
            if player['personId'] == personId:
                first = str(player['firstName'])
                last = str(player['lastName'])
        return (first, last)



if __name__ == '__main__':
    print('Creating Player Info')
    PI = PlayerInfo()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    #print(PI.raw_data) #expensive, save info and use for later?
    print(PI.raw_data.keys())

    print('\n-----_internal---------------------------------------------------')
    print(PI._internal.keys())

    print('\n------league-----------------------------------------------------')
    print(PI.league.keys())

    print('\n-----standard----------------------------------------------------')
    #print(PI.standard) #expensive

    print('standard keys')
    print(PI.standard[0].keys())
