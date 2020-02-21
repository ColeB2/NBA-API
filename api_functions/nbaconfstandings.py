"""
nbaconfstandings.py - Contains functions and classes to handle the data from the
data.nba.net ... standings_conference.json
"""
from functions import get_data
from nbateam import TeamInfo

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_team

def get_divstandings_data():
    """Gets raw json data for leagues division standings.
    """
    url = 'https://data.nba.net/prod/v1/current/standings_conference.json'
    data = get_data(url)
    return data


class ConfStandings(object):
    """A class to sort and hold data for NBA standing_conference.json endpoint.

    Attributes:

    """
    def __init__(self, conference=None, _team=None):
        self.TI = TeamInfo()

        self.raw_data = get_divstandings_data()
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']
        self.conference = self.standard['conference']

        self.standing_data = self.get_standing_data()

    def get_standing_data(self):
        data = self._get_conference()
        standing_data = self.conference[data[0].lower()]
        return standing_data

    def _get_conference(self, team=None):
        if not team: team = get_team()
        return self.TI.get_conf_division(team)



if __name__ == '__main__':
    CS = ConfStandings('east')

    print(CS.conference)
    print(CS.standing_data)
