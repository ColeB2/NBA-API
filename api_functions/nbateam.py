'''
nbateam.py - Acquires NBA team code given either:
city: Atlanta
fullName: Chicago Bulls
tricode: DAL
nickname: Mavericks
teamid: 1610612744
'''
from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season



def get_team_data(season=None):
    """Gets raw json data for all teams.

    Args:
        season: Year of season start date. Ex: 2019 for the 2019/2020 season.

    Returns:
        Dict of raw json data from data.nba.net.../teams.json endpoint
    """
    if not season: season = get_season()
    url = 'http://data.nba.net/prod/v2/' + str(season) + '/teams.json'

    data = get_data(url)
    return data

class TeamInfo(object):
    """A class to sort and hold data from NBA's /team.json endpoint

    Attributes:


    """
    def __init__(self):
        pass



if __name__ == '__main__':
    # print(get_team_url('raptors'))
    # print(get_team_url('ToRoNtO RaPtOrS'))
    # print(get_team_url('ChicaGo Bulls'))
    # print(get_team_url('DAL'))
    # print(get_team_url('ToRoNtO'))
    # print(get_team_url('HAWKS'))
    # print(get_team_url('ATLANTA'))
    # print(get_team_url('Magic'))
    # print(get_team_url('FAIL'))
