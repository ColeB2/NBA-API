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
from getconfiginfo import get_season, get_team



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
    def __init__(self, season=None):
        self.raw_data = get_team_data(season)
        self._internal = self.raw_data['_internal']
        self.league = self.raw_data['league']
        self.standard = self.league['standard']

        self.identifiers = {'division':'divName', 'conference':'confName'}


    def get_conf_division(self, team=None):
        if not team: team = get_team()
        for teams in self.standard:
            if teams['urlName'] == team.lower():
                return (teams['confName'], teams['divName'])
        print('Could not find division')



if __name__ == '__main__':
    TI = TeamInfo()
    print(f"{TI.raw_data.keys()}")
    print(f"{TI._internal.keys()}")
    print(f"{TI.league.keys()}")
    print(f"{TI.standard}")
    print(f"{TI.standard[0].keys()}")


    print(f"{TI.get_conf_division('raptors')}")
    print(f"{TI.get_conf_division()}")
