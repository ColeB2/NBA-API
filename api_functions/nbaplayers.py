from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season

def get_player_name(personId):
    '''
    Gets player name via personId

    param    : get_player_name(personId)
    personId : numerical code for the player ex '1627783' for Pascal Siakam
    example  : get_player_name('1627783')

    returns  : first and last name of the player as a string
    example  : 'Pascal Siakam'
    '''
    season_year = get_season()
    url_start = 'http://data.nba.net/prod/v1/'
    url_end = '/players.json'
    url = str(url_start) + str(season_year) + str(url_end)

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


if __name__ == '__main__':
    #'1627783' is personId for Pascal Siackam
    player_name = get_player_name('1627783')
    print(player_name)
