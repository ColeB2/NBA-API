"""
nbadivstandings.py - Contains functions and classes to handle the data from the
data.nba.net ... standings_division.json
"""
from functions import get_data
from nbateams import TeamInfo as TI

def get_divstandings_data():
    """Gets raw json data for leagues division standings.
    """
    url = 'https://data.nba.net/prod/v1/current/standings_division.json'
    data = get_data(url)
    return data


class DivStandings(object):
    """A class to sort and hold data for the NBA standing_division endpoint.

    Attributes:


    """
    def __init__(self, division=None):
        self.division=division

        self.raw_data = get_divstandings_data()
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']
        self.conference = self.standard['conference']
        self.east_conf = self.conference['east']
        self.west_conf = self.conference['west']


    def get_division(self, division=None, team=None):



if __name__ == '__main__':
    DS = DivStandings()
    print(f"-----raw_data breakdown---------------------\n{DS.raw_data.keys()}")
    print(f"-----_internal-----------------------------\n{DS._internal.keys()}")
    print(f"-----league-----------------------------------\n{DS.league.keys()}")
    print(f"-----standard-------------------------------\n{DS.standard.keys()}")

    print(f"{DS.standard['seasonYear']}\n{DS.standard['seasonStageId']}")
    print(f"{DS.conference.keys()}")
    print(f"{DS.east_conf.keys()}")
    print(f"{DS.west_conf.keys()}")
