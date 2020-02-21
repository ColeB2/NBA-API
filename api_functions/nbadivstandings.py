"""
nbadivstandings.py - Contains functions and classes to handle the data from the
data.nba.net ... standings_division.json
"""
from functions import get_data
from nbateam import TeamInfo

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_team

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
    def __init__(self, division=None, conference=None, _team=None):
        self.TI = TeamInfo()

        self.raw_data = get_divstandings_data()
        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']
        self.conference = self.standard['conference']
        self.east_conf = self.conference['east']
        self.west_conf = self.conference['west']

        self.standing_data = self.get_standing_data()


    def get_standing_data(self):
        data = self._get_conf_division()
        chosen_standing = self.conference[data[0].lower()][data[1].lower()]
        return chosen_standing


    def _get_conf_division(self, team=None):
        """Method to get division of given team.

        Args:
            team: team url, ie raptors, sixers, for team who division you want
                to acquire. If none, uses favourite team from config.
        """
        if not team: team = get_team()
        return (self.TI.get_conf_division(team))




if __name__ == '__main__':
    DS = DivStandings()
    print(f"-----raw_data breakdown---------------------\n{DS.raw_data.keys()}")
    print(f"-----_internal-----------------------------\n{DS._internal.keys()}")
    print(f"-----league-----------------------------------\n{DS.league.keys()}")
    print(f"-----standard-------------------------------\n{DS.standard.keys()}")

    print(f"{DS.standard['seasonYear']}\n{DS.standard['seasonStageId']}")
    print(f"{DS.conference.keys()}")

    print(f"{DS._get_conf_division()}")
    print('TEST')
    print(f"{DS._get_conf_division('1610612761')}")


    print(DS.get_standing_data())
