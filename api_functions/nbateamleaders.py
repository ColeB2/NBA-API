from functions import get_data

from nbaplayers import get_player_name
from nbateam import get_team_url
from getconfiginfo import get_team, get_season

MAIN_FIVE_STATS = ['ppg', 'trpg', 'apg', 'bpg', 'spg']
main_five_stats = []

def get_team_leaders(team=None):
    '''
    PARAMS : get_team_leaders(team)
    team   : nname of team in variety of formats, sIxers, torOnto, Chicago Bulls
    EXAMPLE: get_team_leaders('ToRonTo')

    Returns a tuple of 2 lists which contain:
    1st list returns a tuple, with frist value being the stat, and the second
    value being a list containing a dictionary of the player id & value of stat.
    This list contains all the stats given.

    EXAMPE RETURN: ('ppg', [{'personId': '1627783', 'value': '25.1'}])

    '''
    if team == None:
        team = get_team()
    else:
        team = get_team_url(team)
    date = get_season()

    url1 = 'http://data.nba.net/prod/v1/'
    url_end = '/leaders.json'
    url = str(url1) + str(date) + '/teams/' + str(team.lower()) + str(url_end)

    all_stats = []

    data = get_data(url)
    x = data['league'] #dictionary of all options
    y = x['standard'] #dictionary of main league values


    '''Extracting information we need'''
    for key in y:
        all_stats.append((key, y[key]))
    return (all_stats[1:])


'''UI STUFF, MOVE REARRANGE'''
def print_team_leaders(team=None):
    team_leaders = get_team_leaders(team)

    for player in team_leaders:
        print(str(player[0]) + ' ' + str(player[1][0]['value']), end=' ')
        print(get_player_name(player[1][0]['personId']))

def my_pretty_print(obj, depth):
    print(str(obj)[:depth], end='|')


def pretty_print_team_leaders(team=None):
    team_leaders = get_team_leaders(team)

    print('STAT |VALUE|PLAYER NAME')
    print('-----------------------')
    for player in team_leaders:
        #stat = (str(player[0]) + ' ' + str(player[1][0]['value']))
        stat = str(player[0].upper() + 2 * ' ')
        value = str(player[1][0]['value'] + 4*' ')
        #print(player[0])
        #print(player[1][0])
        name = str((get_player_name(player[1][0]['personId'])))
        my_pretty_print(stat, 5)
        my_pretty_print(value, 5)
        print(name)
    print('----------------------')



if __name__ == '__main__':
    pretty_print_team_leaders()
    #print_team_leaders()
    #print()
    #print_team_leaders('laKerS')
