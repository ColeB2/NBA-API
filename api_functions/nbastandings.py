"""
nbadivstandings.py - Contains functions and classes to handle the data from the
data.nba.net ... standings_division.json, and standings_conference.json
"""
from functions import get_data
from nbateam import TeamInfo

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_team

def get_standings_data(division=False, conference=False):
    """Gets raw json data for leagues division/conference standings based on
    arguments.

    Args:
        division: Boolean value, True if want division standings data.
        conference: Boolean value, True if want conference standings data.

    Returns:
        Dict of raw json data from data.nba.net.../standings_XXX.json endpoint
            XXX is either division or conference.
    """
    standing = 'division' if division else 'conference'

    url = f"https://data.nba.net/prod/v1/current/standings_{standing}.json"

    data = get_data(url)
    return data


class Standings(object):
    """A class to sort and hold data for NBA standing_division.json endpoint.

    Attributes:


    """
    def __init__(self, division=False, conference=False, _team=None):
        self.div = division
        self.conf = conference

        self.TI = TeamInfo()

        self.raw_data = get_standings_data(division=self.div,
            conference=self.conf)

        self._internal = self.raw_data['_internal']

        self.league = self.raw_data['league']
        self.standard = self.league['standard']
        self.conference =self.standard['conference']


    def get_standing_data(self):
        data = self._get_conf_division()
        if self.div:
            chosen_standing = self.conference[data[0].lower()][data[1].lower()]
        elif self.conf:
            chosen_standing = self.conference[data[0].lower()]
        return chosen_standing


    def _get_conf_division(self, team=None):
        """Method to get division of given team.

        Args:
            team: team url, ie raptors, sixers, for team who division you want
                to acquire. If none, uses favourite team from config.
        """
        if not team: team = get_team()
        return self.TI.get_conf_division(team)




if __name__ == '__main__':
    print('DIVISION STANDINGS')
    DS = Standings(division=True)
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

    print('CONFERENCE STANDIGNS')
    CS = Standings(conference=True)
    print(f"-----raw_data breakdown---------------------\n{CS.raw_data.keys()}")
    print(f"-----_internal-----------------------------\n{CS._internal.keys()}")
    print(f"-----league-----------------------------------\n{CS.league.keys()}")
    print(f"-----standard-------------------------------\n{CS.standard.keys()}")
    print(f"{CS.standard['seasonYear']}\n{CS.standard['seasonStageId']}")
    print(f"{CS.conference.keys()}")
    print(f"{CS._get_conf_division()}")
    print('TEST')
    print(f"{CS._get_conf_division('1610612761')}")
    print(CS.get_standing_data())